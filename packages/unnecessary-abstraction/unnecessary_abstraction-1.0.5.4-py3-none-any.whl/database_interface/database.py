from typing import Protocol
import psycopg2
import csv, math, shutil, pathlib, sqlite3
from collections import defaultdict
from .schema_objects import SQLSchema, SQLColumn
from .type_maps import SQLITE_TYPES, POSTGRES_TYPES, POSTGIS_TYPES, RECORD_INVERT_OPTIONS
from .errors import DatabaseTableError, DatabaseTypingError

class Database(Protocol):

    @property
    def db_conn(self) -> psycopg2.extensions.connection | sqlite3.Connection:
        ...
    @property
    def type_map(self) -> dict:
        ...
    @property
    def binding_char(self) -> str:
        ...

    @property
    def table_list_sql(self):
        ...

    @property
    def table_loc(self):
        ...

    @property
    def table_name(self):
        ...
    @table_name.setter
    def table_name(self, input):
        ...

    def create_table_statement(self, table_name:str, schema:SQLSchema) -> str:
        ...

    def infer_type(self, val:str) -> str:
        ...

    def get_schema(self, table_name:str) -> SQLSchema:
        ...
        
    def table_from_records(self, table_name:str, table_records:list[dict], col_overrides:list[SQLColumn]=[], schema_override:SQLSchema=None, deep_evaluation:bool=False) -> None:
        # self.table_name = table_name
        # if self.table_name in self.list_tables():
        #     raise DatabaseTableError("Table Exists", self.table_loc)
        
        schema:SQLSchema = schema_override
        if not schema_override:
            if deep_evaluation:
                schema = self.deep_schema_evaluation(table_records, col_overrides)
            else:
                schema = self.evaluate_schema(table_records, col_overrides)
        
        create_statement = self.create_table_statement(table_name, schema)
        self.execute_query(create_statement)
        self.records_to_table(table_name, table_records)

    def records_to_table(self, table_name:str, table_records:list[dict]) -> None:
        schema = self.get_schema(table_name)
        if schema:
            schema.filter_columns(list(table_records[0].keys()))
            
            insert_statement = self.insert_into_table_statement(table_name, schema)
            table_records_sql = [tuple(val for val in row.values()) for row in table_records]

            cur = self.db_conn.cursor()
            cur.executemany(insert_statement, table_records_sql)
            self.db_conn.commit()
        else:
            raise DatabaseTableError("Table Does not Exist", self.table_loc)
    
    def table_to_records(self, table_name:str, columns:str="*", where_clause:str="", return_schema=False) -> list[dict] | tuple[list[dict], SQLSchema]:
        self.table_name = table_name
        schema:SQLSchema = self.get_schema(table_name)
        table_data = self.get_table(table_name, columns, where_clause)

        if columns != "*":
            schema.filter_columns(columns.split(", "))
            
        records = []
        for row in table_data:
            record_row = {}
            for col_name, sql_col in schema.schema_map.items():
                record_row[col_name] = row[sql_col.position - 1]
            records.append(record_row)

        if return_schema:
            return records, schema
        else:
            return records



    ### DATABASE TASKS ###

    def execute_query(self, sql_statement:str) -> None:
        cur = self.db_conn.cursor()
        cur.execute(sql_statement)
        self.db_conn.commit()

    def create_blank_table(self, table_name:str, schema:SQLSchema) -> None:
        sql = self.create_table_statement(table_name, schema)
        self.execute_query(sql)

    def drop_table(self, table_name) -> None:
        self.execute_query(f"DROP TABLE IF EXISTS {table_name}")
    
    def list_tables(self) -> list[str]:
        cur = self.db_conn.cursor()
        cur.execute(self.table_list_sql)
        res = cur.fetchall()
        return [table[0] for table in res]

    def get_table(self, table_name:str, columns:str="*", where_clause:str="") -> list[tuple]:
        select_statement = self.select_table_statement(table_name, columns, where_clause)
        cur = self.db_conn.cursor()
        cur.execute(select_statement)
        return cur.fetchall()

    ### DATABASE TASKS ###


    ### TABLE ALTERATIONS ###

    def update_with_unique_records(self, table_name:str, records:list[dict], unique_key_col:str) -> None:
        cur = self.db_conn.cursor()
        for row in records:
            update_statement = self.create_update_statement(table_name, row, f"WHERE {unique_key_col}='{row[unique_key_col]}'")
            cur.execute(update_statement)
        self.db_conn.commit()

    def delete_rows(self, table_name:str, where_clause:str) -> None:
        delete_statement = self.create_delete_statement(table_name, where_clause)
        self.execute_query(delete_statement)

    def delete_all_records(self, table_name:str) -> None:
        self.table_name = table_name
        self.execute_query(f"DELETE FROM {self.table_loc};")

    def add_column(self, table_name:str, col_name:str, data_type:SQLITE_TYPES | POSTGRES_TYPES | POSTGIS_TYPES) -> None:
        self.table_name = table_name
        self.execute_query(f"ALTER TABLE {self.table_loc} ADD {col_name} {self.type_map[data_type]};")
    
    def drop_column(self, table_name:str, col_name:str) -> None:
        self.table_name = table_name
        self.execute_query(f"ALTER TABLE {self.table_loc} DROP COLUMN {col_name}")
    
    def rename_column(self, table_name:str, col_name:str, new_col_name:str) -> None:
        self.table_name = table_name
        self.execute_query(f"ALTER TABLE {self.table_loc} RENAME COLUMN {col_name} TO {new_col_name}")

    def rename_table(self, table_name:str, new_table_name:str) -> None:
        self.table_name = table_name
        self.execute_query(f"ALTER TABLE {self.table_loc} RENAME TO {new_table_name}")
        
    ### TABLE ALTERATIONS ###


    ### STATEMENT BUILDERS ###

    def select_table_statement(self, table_name:str, columns:str="*", where_clause:str="") -> str:
        self.table_name = table_name
        statement = f"SELECT {columns} FROM {self.table_loc}"
        if where_clause:
            statement += f" {where_clause}"
        statement += ";"
        return statement
    
    def create_update_statement(self, table_name:str, record_row:dict, where_clause:str) -> str:
        self.table_name = table_name
        statement = f"UPDATE {self.table_loc} SET "
        for col_name, value in record_row.items():
            statement += f"{col_name}='{value}', "
        statement = statement[:-2] + " " + where_clause + ";"
        return statement

    def create_delete_statement(self, table_name:str, where_clause:str="") -> str:
        self.table_name = table_name
        statement = f"DELETE FROM {self.table_loc}"
        if where_clause:
            statement += f" {where_clause}"
        statement += ";"
        return statement

    def insert_into_table_statement(self, table_name:str, schema:SQLSchema) -> str:
        self.table_name = table_name
        statement = f"INSERT INTO {self.table_loc} ("
        bindings = ""
        for col_name, sql_col in schema.schema_map.items():
            statement += f"{col_name}, "
            bindings += f"{self.binding_char}, "
        statement = statement[:-2] + f") VALUES (" + bindings[:-2] + ");"
        return statement

    ### STATEMENT BUILDERS ###

    #### CSV Functions #####

    def rename_duplicate_columns(self, fieldname_list:list[str]) -> list[str]:
        d = defaultdict(list)
        [d[name].append(seq) for seq, name in enumerate(fieldname_list)]
        for col, count in d.items():
            if len(count) > 1:
                for seq, index in enumerate(count[1:]):
                    fieldname_list[index] = f"{fieldname_list[index]}_{seq+2}"
        return fieldname_list
    

    
    def records_to_csv(self, records:list[dict], csv_name:str, csv_path:str=".") -> None:
        headers = records[0].keys()
        with open(f"{csv_path}\\{csv_name}.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            writer.writerows(records)

    def append_csv_to_table(self, table_name:str, csv_path:str) -> None:
        records = self.csv_to_records(csv_path)
        self.records_to_table(table_name, records)

    def csv_to_records(self, csv_path:str) -> list[dict]:
        csv_path:pathlib.Path = pathlib.Path(csv_path)
        with open(csv_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            if len(reader.fieldnames) != len(set(reader.fieldnames)):
                reader.fieldnames = self.rename_duplicate_columns(reader.fieldnames)
            records = [row for row in reader]
        
        for row in records:
            for key, val in row.items():
                if val == '':
                    row[key] = None
        return records

    def csv_to_table(self, csv_path:str, col_overrides:list[SQLColumn]=[], schema_override:SQLSchema=None) -> None:
        csv_name = pathlib.Path(csv_path).stem
        records = self.csv_to_records(csv_path)
        self.table_from_records(csv_name, records, col_overrides, schema_override)

    def table_to_csv(self, table_name:str, file_name:str="", save_path:str=".", columns:str="*", where_clause:str="") -> None:
        table_records= self.table_to_records(table_name, columns, where_clause)
        headers:dict = table_records[0]
        headers = headers.keys()
        if not file_name:
            file_name = table_name

        with open(f"{save_path}\\{file_name}.csv", 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(table_records)

    ### CSV Functions #####



    ### Record/Schema inspection functions ####
    def invert_records(self, records:list[dict] | dict[list], mode:RECORD_INVERT_OPTIONS) -> list[dict] | dict[list]:
        
        if mode == "list[dict] to dict[list]" and type(records) == list:
            new_data = {col: [] for col, data in records[0].items()}
            for row in records:
                for col, data in row.items():
                    new_data[col].append(data)
            return new_data
        
        elif mode == "dict[list] to list[dict]" and type(records) == dict:
            row_size = list(records.keys())
            row_size = len(records[row_size[0]])
            new_data = [{col: records[col][i] for col in records} for i in range(row_size)]
            return new_data

    def deep_schema_evaluation(self, records:list[dict] | dict[list], col_overrides:list[SQLColumn]=[]) -> SQLSchema:
        records:dict[list] = self.invert_records(records, "list[dict] to dict[list]")

        schema = []
        overide_col_list = tuple(col.name for col in col_overrides)
        
        for pos, (col_name, col_data) in enumerate(records.items(), 1):
            if col_name in overide_col_list:
                col:SQLColumn = col_overrides[overide_col_list.index(col_name)]
                schema.append(SQLColumn(name=col.name, 
                                        data_type=self.type_map[col.data_type], 
                                        position=pos, 
                                        is_primary_key=col.is_primary_key, 
                                        foreign_key=col.foreign_key, 
                                        is_unique=col.is_unique, 
                                        check_constraint=col.check_constraint,
                                        not_null=col.nullable))
            else:
                col_type = tuple(self.infer_type(x)for x in col_data if x != None)
                if len(set(col_type)) > 1:
                    raise DatabaseTypingError("Column not Valid", col_name)
                schema.append(SQLColumn(name=col_name, data_type=col_type[0], position=pos))

        return SQLSchema(schema)

    def evaluate_schema(self, records:list[dict], col_overrides:list[SQLColumn]=[]) -> SQLSchema:

        def find_non_null_record(records:list[dict], col_name:str):
            for row in records:
                if row[col_name]:
                    return row[col_name]
            return "empty_col_default_to_string"

        schema = []
        top_row:dict = records[0]
        overide_col_list = tuple(col.name for col in col_overrides)

        for pos, (col_name, col_val) in enumerate(top_row.items()):
            if col_name in overide_col_list:
                col:SQLColumn = col_overrides[overide_col_list.index(col_name)]
                schema.append(SQLColumn(name=col.name, 
                                        data_type=self.type_map[col.data_type], 
                                        position=pos, 
                                        is_primary_key=col.is_primary_key, 
                                        foreign_key=col.foreign_key, 
                                        is_unique=col.is_unique, 
                                        check_constraint=col.check_constraint,
                                        not_null=col.nullable))
            else:
                if col_val:
                    d_type = self.infer_type(col_val)
                else:
                    d_type = self.infer_type(find_non_null_record(records, col_name))
                schema.append(SQLColumn(name=col_name, data_type=d_type, position=pos))

        return SQLSchema(schema)
    


    def print_table(self, table_name:str, col_width:int=12, start_row:int=0, 
                    print_limit:int=20, columns:str="*", where_clause:str="") -> None:

        def get_terminal_size():
            size = shutil.get_terminal_size(fallback=(80, 20))
            return size.columns, size.lines

        def write_margin(option:str, table:str, col_count:int, COL_WIDTH:int, concat_col:int):
            if option == "Top Header":
                leftmost = "┌─────┐"
                rightmost = "┐"
            elif option == "Bottom Header":
                leftmost = "\n│─────┼"
                rightmost = "┼"
            elif option == "Bottom Margin":
                leftmost = "└─────┘"
                rightmost = "┘"

            table += leftmost
            for i in range(col_count):
                dashs = ""
                if i == concat_col:
                    dashs = "───"
                else:
                    for k in range(COL_WIDTH):
                        dashs += "─"
                table += dashs + rightmost

            if option == "Bottom Header":
                table = table[:-1] + "│\n"

            return table

        def get_table_attributes(schema:SQLSchema, max_cols:int) -> tuple[list[dict], int, list[str], int]:
            if max_cols == 1:
                records, schema = self.table_to_records(table_name, schema.col_name_list[0], where_clause, return_schema=True)
                col_count = schema.col_count
                col_names = schema.col_name_list
                concat_col = -1
            elif schema.col_count > max_cols:
                size = math.floor(max_cols / 2)
                front = schema.col_name_list[:size]
                back = schema.col_name_list[(0-size):]
                col_filter = ", ".join(front) + ", " +  ", ".join(back)
                records, schema = self.table_to_records(table_name, col_filter, where_clause, return_schema=True)
                col_names = front + ["..."] + back
                col_count = len(col_names)
                concat_col = col_names.index("...")
            else:
                records, schema = self.table_to_records(table_name, columns, where_clause, return_schema=True)
                col_count = schema.col_count
                col_names = schema.col_name_list
                concat_col = -1
            
            return records, col_count, col_names, concat_col

        PRINT_TABLE = ""

        terminal_x, terminmal_y = get_terminal_size()
        if col_width < 7:
            COL_WIDTH = 7
        elif col_width > terminal_x - 9:
            COL_WIDTH = terminal_x - 10
        else:
            COL_WIDTH = col_width
        
        max_cols = math.floor(((terminal_x - 9) / (COL_WIDTH + 1)))
        schema = self.get_schema(table_name)
        if columns != "*":
            schema.filter_columns(columns.split(", "))
            records, col_count, col_names, concat_col = get_table_attributes(schema, max_cols)
        else:
            records, col_count, col_names, concat_col = get_table_attributes(schema, max_cols)

            
        PRINT_TABLE = write_margin("Top Header", PRINT_TABLE, col_count, COL_WIDTH, concat_col)

        # Table Column Header #
        PRINT_TABLE += f"\n│     │"
        for col in col_names:
            if col == "...":
                PRINT_TABLE += col.center(3) + "│"
            else:
                if len(col) > COL_WIDTH:
                    col = col[:COL_WIDTH-4] + "..."
                    PRINT_TABLE += col.center(COL_WIDTH) + "│"
                else:
                    PRINT_TABLE += col.center(COL_WIDTH) + "│"
        # Table Column Header #

        PRINT_TABLE = write_margin("Bottom Header", PRINT_TABLE, col_count, COL_WIDTH, concat_col)

        # Table Records #
        for pos, row in enumerate(records[start_row:]):
            PRINT_TABLE += "│" + str(pos + start_row).center(5)
            for col in col_names:
                if col == "...":
                    PRINT_TABLE += "│" + "...".center(3)
                else:
                    data = str(row[col])
                    if len(data) > (COL_WIDTH - 4):
                        data = data[:(COL_WIDTH - 4)] + "..."
                    PRINT_TABLE += "│" + data.center(COL_WIDTH)
            PRINT_TABLE = PRINT_TABLE + "│\n"
            if pos >= print_limit:
                break
        # Table Records #

        PRINT_TABLE = write_margin("Bottom Margin", PRINT_TABLE, col_count, COL_WIDTH, concat_col)

        
        print(PRINT_TABLE)
