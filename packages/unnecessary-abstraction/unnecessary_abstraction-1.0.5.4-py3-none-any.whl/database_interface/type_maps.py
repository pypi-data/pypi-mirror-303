from typing import Literal
import copy


RECORD_INVERT_OPTIONS = Literal["list[dict] to dict[list]", "dict[list] to list[dict]"]

SQLITE_TYPES = Literal["text", "real", "integer", "numeric"]

POSTGRES_TYPES = Literal["integer", "smallint", "bigint", "real", "double precision", "decimal", "numeric", "text", 
                         "timestamp with time zone", "timestamp", "date", "time with time zone", "time", "interval", 
                         "uuid", "json", "jsonb", "boolean"]

POSTGIS_TYPES = Literal["integer", "smallint", "bigint", "real", "double precision", "decimal", "numeric", "text", 
                         "timestamp with time zone", "timestamp", "date", "time with time zone", "time", "interval", 
                         "uuid", "json", "jsonb", "boolean", "geometry"]

POSTGRES_TYPE_MAP = {"integer": "integer", 
                     "smallint": "smallint", 
                     "bigint": "bigint", 
                     "real": "real", 
                     "double precision": "double precision", 
                     "decimal": "decimal", 
                     "numeric": "numeric", 
                     "smallserial": "smallserial", 
                     "serial": "serial", 
                     "bigserial": "bigserial", 
                     "geometry": "text", 
                     "text": "text", 
                     "timestamp": "timestamp", 
                     "timestamp with time zone": "timestamp with time zone", 
                     "boolean": "boolean",
                     "date": "date", 
                     "time with time zone": "time with time zone", 
                     "time": "time", "interval": "interval",
                     "uuid": "uuid DEFAULT gen_random_uuid()", 
                     "json": "json", 
                     "jsonb": "jsonb",
                     "TEXT": "text", 
                     "REAL": "real", 
                     "INTEGER": "integer", 
                     "NUMERIC": "numeric"}

POSTGIS_TYPE_MAP = copy.copy(POSTGRES_TYPE_MAP)
POSTGIS_TYPE_MAP["geometry"] = "geometry"
#POSTGIS_TYPE_MAP["point"] = "point"


SQLITE_TYPE_MAP = {"integer": "integer", 
                   "smallint": "integer", 
                   "bigint": "integer", 
                   "real": "real", 
                   "double precision": "real", 
                   "decimal": "real", 
                   "numeric": "numeric",  
                   "smallserial": "integer", 
                   "serial": "integer", 
                   "bigserial": "integer", 
                   "geometry": "text", 
                   "text": "text", "timestamp": "text", 
                   "timestamp with time zone": "text",
                   "date": "text", 
                   "time with timezone": "text", 
                   "time": "text", 
                   "boolean": "text",
                   "uuid": "text", 
                   "interval": "text",  
                   "json": "text", 
                   "jsonb": "text",
                   "TEXT": "text", 
                   "REAL": "real", 
                   "INTEGER": "integer", 
                   "NUMERIC": "numeric"}