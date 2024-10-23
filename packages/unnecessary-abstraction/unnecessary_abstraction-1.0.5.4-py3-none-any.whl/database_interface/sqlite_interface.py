from .database import Database
import sqlite3
import csv
from uuid import UUID
from datetime import datetime
import pathlib

from .schema_objects import SQLColumn, SQLSchema
from .type_maps import SQLITE_TYPE_MAP
from .errors import DatabaseTableError

class SQLite(Database):
    def __init__(self, sqlite_path:str, foreign_keys_on=False):
        super().__init__()
        parse_path = sqlite_path.split(".")
        if len(parse_path) == 1:
            sqlite_path = sqlite_path + ".db"
            self.__db_conn = sqlite3.Connection(sqlite_path)
        if len(parse_path) >= 2 and parse_path[-1] in ["sqlite", "db"]:
                self.__db_conn = sqlite3.Connection(sqlite_path)
        else:
            raise Exception("Your file naming is jacked up, end the db file with .db or .sqlite")
        
        self.__binding_char = "?"
        self.__type_map = SQLITE_TYPE_MAP
        if foreign_keys_on:
            cur = self.db_conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            resp = cur.execute("PRAGMA foreign_keys")
            print(f"Foreign Keys for {sqlite_path}:", bool(resp.fetchall()[0][0]))
    
    @property
    def db_conn(self) -> sqlite3.Connection:
        return self.__db_conn
    @property
    def type_map(self) -> dict:
        return self.__type_map
    @property
    def binding_char(self) -> str:
        return self.__binding_char

    @property
    def table_list_sql(self) -> str:
        return "SELECT name FROM sqlite_master"

    @property
    def table_loc(self) -> str:
        return self.__table
    @property
    def table_name(self) -> str:
        return self.__table
    @table_name.setter
    def table_name(self, input):
        self.__table = input

    def get_schema(self, table_name:str) -> SQLSchema:
        self.table_name = table_name
        cur = self.db_conn.cursor()
        res = cur.execute(f"PRAGMA table_info({self.table_loc})").fetchall()
        if not res:
            raise DatabaseTableError("Table Does not Exist", self.table_loc)
        
        return SQLSchema([SQLColumn(name=row[1], data_type=row[2], position=(row[0] + 1), nullable=bool(row[3]), is_primary_key=bool(row[5])) for row in res])
    
    def infer_type(self, val) -> str:
        if type(val) == int:
            return "integer"
        elif type(val) == float:
            return "real"
        elif type(val) == bool:
            return "text"
        elif type(val) == UUID:
            return "uuid"
        elif type(val) == datetime:
            return "text"
        else:
            val:str
            split = val.split(".")
            if len(split) == 2 and split[0].isnumeric() and split[1].isnumeric():
                return "real"
            elif val.isnumeric():
                if val == "0":
                    return "numeric"
                else:
                    return "integer"
            else:
                return "text"
    
    def create_table_statement(self, table_name:str, schema:SQLSchema) -> str:
        statement = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for_keys = ""
        for col_name, sql_col in schema.schema_map.items():
            statement += f"{col_name} {self.__type_map[sql_col.data_type]}"
            if sql_col.is_primary_key:
                statement = statement + f" PRIMARY KEY"
            if not sql_col.nullable:
                statement = statement + f" NOT NULL"
            if sql_col.foreign_key:
                for_keys += f"FOREIGN KEY({sql_col.name}) REFERENCES {sql_col.foreign_key['references_table']} ({sql_col.foreign_key['references_col']}), "
            statement = statement + ", "
        if for_keys:
            statement += for_keys
        statement = statement[:-2] + f")"
        return statement
    