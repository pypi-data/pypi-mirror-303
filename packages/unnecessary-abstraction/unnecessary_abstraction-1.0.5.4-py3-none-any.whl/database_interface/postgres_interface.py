from .database import Database
import psycopg2
import json
from uuid import UUID
from datetime import datetime

from .schema_objects import SQLColumn, SQLSchema
from .type_maps import POSTGRES_TYPE_MAP, POSTGRES_TYPES
from .errors import DatabaseTypingError, DatabaseTableError


class PostgreSQL(Database):
    def __init__(self, db_name:str, username:str, password:str, namespace:str, host="localhost", port=5432):
        self.__db_conn = psycopg2.connect(database=db_name, user=username, password=password, host=host, port=port)
        self.__binding_char = "%s"
        self.__type_map = POSTGRES_TYPE_MAP
        self.__namespace = namespace

    @property
    def db_conn(self):
        return self.__db_conn
    
    @property
    def type_map(self) -> dict:
        return self.__type_map
    
    @property
    def binding_char(self) -> str:
        return self.__binding_char
    
    @property
    def table_list_sql(self) -> str:
        return f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{self.__namespace}'"
    
    @property
    def table_loc(self) -> str:
        return f"{self.__namespace}.{self.__table}"
    @property
    def table_name(self):
        return self.__table
    @table_name.setter
    def table_name(self, input):
        self.__table = input

    @property
    def current_namespace(self):
        return self.__namespace
    
    @current_namespace.setter
    def current_namespace(self, input:str):
        self.__namespace = input

    def alter_column(self, table_name:str, col_name:str, data_type:POSTGRES_TYPES) -> None:
        self.table_name = table_name
        cur = self.db_conn.cursor()
        sql_statement = f"ALTER TABLE {self.table_loc} ALTER COLUMN {col_name} {self.type_map[data_type]}"
        cur.execute(sql_statement)
        self.db_conn.commit()

    def get_schema(self, table_name:str) -> SQLSchema:
        self.table_name = table_name
        GET_COL_SCHEMA = f"SELECT column_name, data_type, ordinal_position, is_nullable FROM information_schema.columns WHERE table_schema='{self.__namespace}' AND table_name='{table_name}'"
        cur = self.db_conn.cursor()
        cur.execute(GET_COL_SCHEMA)
        res = cur.fetchall()
        col_list = []

        if not res:
            raise DatabaseTableError("Table Does not Exist", self.table_loc)
        else:
            for col in res:
                if col[3] == 'YES':
                    nullable = True
                else:
                    nullable = False
                col_list.append(SQLColumn(col[0], col[1], col[2], nullable))

            schema = SQLSchema(col_list)
            return schema
        
    def create_namespace(self, name:str):
        statement = "CREATE SCHEMA " + name + ";"
        cur = self.db_conn.cursor()
        cur.execute(statement)
        self.db_conn.commit()

    def create_database(self, db_name:str, owner:str="", clone_from:str=""):
        statement = "CREATE DATABASE " + db_name
        if owner or clone_from:
            statement += " WITH"
            if clone_from:
                statement += " TEMPLATE " + clone_from
            if owner:
                statement += " OWNER " + owner
        
        statement += ";"
        cur = self.db_conn.cursor()
        cur.execute(statement)
        self.db_conn.commit()

    def create_table_statement(self, table_name:str, schema:SQLSchema) -> str:
        statement = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for_keys = ""

        for col_name, sql_col in schema.schema_map.items():
            statement += f"{col_name} {self.__type_map[sql_col.data_type]}"
            if sql_col.is_primary_key:
                statement = statement + f" PRIMARY KEY"
            if sql_col.is_unique and not sql_col.is_primary_key:
                statement = statement + f" UNIQUE"
            if not sql_col.nullable and not sql_col.is_primary_key:
                statement = statement + f" NOT NULL"
            if sql_col.check_constraint:
                statement = statement + f" {sql_col.check_constraint}"
            if sql_col.foreign_key:
                statement = statement + f" REFERENCES {sql_col.foreign_key['references_table']} ({sql_col.foreign_key['references_col']})"
            statement = statement + ", "
        if for_keys:
            statement += for_keys
        statement = statement[:-2] + f");"
        return statement

    def infer_type(self, val) -> str:
        def is_datetime(x) -> bool:
            try:
                datetime.fromisoformat(x)
                return True
            except ValueError:
                return False
            
        def string_jsonable(x) -> bool:
            try:
                json.loads(x)
                return True
            except (TypeError, OverflowError, json.decoder.JSONDecodeError):
                return False
        def dict_jsonable(x) -> bool:
            try:
                json.dumps(x)
                return True
            except (TypeError, OverflowError, json.decoder.JSONDecodeError):
                return False

        if type(val) == int:
            return "integer"
        elif type(val) == float:
            return "decimal"
        elif type(val) == bool:
            return "text"
        elif type(val) == UUID:
            return "uuid"
        elif type(val) == datetime:
            return "timestamp"
        elif type(val) == str:
            val:str
            split = val.split(".")
            if len(split) == 2 and split[0].isnumeric() and split[1].isnumeric():
                if len(split[1]) > 8:
                    return "double precision"
                else:
                    return "real"
            elif val.isnumeric():
                if val == "0":
                    return "numeric"
                else:
                    return "integer"
            elif is_datetime(val):
                if datetime.fromisoformat(val).tzinfo:
                    return "timestamp with time zone"
                else:
                    return "timestamp"
            elif string_jsonable(val):
                return "json"
            else:
                return "text"
        elif type(val) == dict:
            if dict_jsonable(val):
                return "json"
            else:
                raise DatabaseTypingError("JSON didn't serialize")

