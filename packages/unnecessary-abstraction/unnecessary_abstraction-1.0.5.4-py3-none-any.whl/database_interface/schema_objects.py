from typing import Literal, TypedDict

TYPES = Literal["integer", "smallint", "bigint", "real", "double precision", "decimal", "numeric", "smallserial", 
                "serial", "bigserial", "text", "timestamp with time zone", "timestamp", "date", "time with time zone", 
                "time", "interval", "uuid", "json", "jsonb", "geometry"]

class ForeignKey(TypedDict):
    references_table:str
    references_col:str


class SQLColumn:
    __slots__ = ('name', 'data_type', 'position', 'nullable', 'is_primary_key', 'foreign_key', 'is_unique', 'check_constraint')
    def __init__(self, name:str, data_type:TYPES, position:int = 0, 
                 nullable=True, is_unique:bool=False, is_primary_key:bool = False, 
                 foreign_key:ForeignKey=None, check_constraint:str=""):
        
        self.name:str = name
        self.data_type:TYPES = data_type
        self.position:int = position
        self.nullable:bool = nullable
        self.is_unique:bool = is_unique
        self.is_primary_key:bool = is_primary_key
        self.foreign_key:ForeignKey = foreign_key
        self.check_constraint:str = check_constraint

    def __repr__(self) -> str:
        text = f"{self.name} (data_type: {self.data_type}, position: {self.position}, nullable: {self.nullable}, unique: {self.is_unique}, "
        if self.is_primary_key:
            text += f"Primary Key, "
        if self.foreign_key:
            text += f"Foreign Key: references {self.foreign_key['references_table']} ({self.foreign_key['references_col']}, "
        if self.check_constraint:
            text += f"Check Constraint: {self.check_constraint}, "
        
        text = text[:-2] + ")"
        return text

class SQLSchema:
    def __init__(self, sql_cols:list[SQLColumn]):
        self.__schema:dict[str, SQLColumn] = {row.name : row for row in sql_cols}

        self.validate_schema()

    @property
    def schema_map(self) -> dict[str, SQLColumn]:
        return self.__schema
    @schema_map.setter
    def schema_map(self, input):
        self.__schema = input
    
    @property
    def col_name_list(self) -> list[str]:
        return [col.name for key, col in self.schema_map.items()]
    @property
    def positions_list(self) -> list[int]:
        return [col.position for key, col in self.schema_map.items()]
    @property
    def col_positions(self) -> dict[str, int]:
        return {key:col.position for key, col in self.schema_map.items()}
    @property
    def col_count(self) -> int:
        return len(self.__schema)
    
    def order_by_loc(self):
        for pos, col_name in enumerate(self.schema_map.keys()):
            self.schema_map[col_name].position = pos + 1

    def order_by_pos_id(self):
        temp_schema = {}
        sort_pos = sorted(self.col_positions.items(), key=lambda x: x[1])
        for col in sort_pos:
            temp_schema[col[0]] = self.schema_map[col[0]]
        
        self.schema_map = temp_schema
        
    def add_column(self, col:SQLColumn):
        self.schema_map[col.name] = col

    def drop_column(self, col_name):
        del self.schema_map[col_name]
    
    def filter_columns(self, col_name_list:list):
        extract_map = {}
        for col_name in col_name_list:
            extract_map[col_name] = self.get_col(col_name)
        self.schema_map = extract_map
        self.order_by_loc()
    
    def validate_schema(self):
        pos_list = sorted(self.positions_list)
        if pos_list == list(range(min(pos_list), max(pos_list)+1)) and pos_list[0] == 1:
            self.order_by_pos_id()
        else:
            self.order_by_loc()
    
    def get_col(self, col_name:str) -> SQLColumn:
        return self.schema_map[col_name]
    
    def __repr__(self) -> str:
        PRINT_TABLE = ""
        for col_name, sql_col in self.schema_map.items():
            PRINT_TABLE += f"{sql_col}\n"
        
        return PRINT_TABLE


