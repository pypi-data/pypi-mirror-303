import json
from uuid import UUID
from .postgres_interface import PostgreSQL
from .schema_objects import SQLColumn, SQLSchema
from .type_maps import POSTGIS_TYPE_MAP


class PostGIS(PostgreSQL):
    def __init__(self, db_name:str, username:str, password:str, schema:str, host:str="localhost", port:int=5432):
        super().__init__(db_name, username, password, schema, host, port)
        self.__type_map = POSTGIS_TYPE_MAP



