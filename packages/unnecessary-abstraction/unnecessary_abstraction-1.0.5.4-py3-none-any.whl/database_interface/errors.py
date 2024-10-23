from typing import Literal


TABLE_ERRORS = Literal["Table Exists", "Table Does not Exist"]

class DatabaseTableError(Exception):
    def __init__(self, error:TABLE_ERRORS, table_name:str) -> None:
        
        self.message:str = ""
        if error == "Table Exists":
            self.message:str = f"Table '{table_name}' is already a table in the database."
        elif error == "Table Does not Exist":
            self.message:str = f"Table '{table_name}' does not exist"

        super().__init__(self.message)


TYPE_ERRORS = Literal["Column not Valid", "JSON didn't serialize"]
PY_DICT_ERROR = """
Your data contains a python dictionary that cannot be formed into a JSON.
Check the values of your dictionary to find what is causing json.dumps()
to error out and convert as necessary. PostgreSQL doesn't have any type
to support this data structure.
"""

class DatabaseTypingError(Exception):
    def __init__(self, error:TYPE_ERRORS, col_name:str) -> None:

        if error =="Column not Valid":
            self.message:str = f"{col_name} has mixed datatypes contained in its column"
        elif error == "JSON didn't serialize":
            self.message:str = PY_DICT_ERROR

        super().__init__(self.message)
