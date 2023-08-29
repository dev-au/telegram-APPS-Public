from .main import db


class Models:
    class STRING_LONG_TEXT:
        SQL_OPERATION: str

        def __init__(self, not_null: bool = False, primary_key: bool = False):
            self.SQL_OPERATION = "TEXT"
            if not_null:
                self.SQL_OPERATION += " NOT NULL"
            if primary_key:
                self.SQL_OPERATION += " PRIMARY KEY"

    class STRING_SHORT_TEXT:
        SQL_OPERATION: str

        def __init__(self, max_length: int = 64, not_null: bool = False, primary_key: bool = False):
            self.SQL_OPERATION = "VARCHAR"
            if max_length > 255:
                print("VARCHAR MAX LENGTH IS 255")
                max_length = 255
            if max_length != 0:
                self.SQL_OPERATION += f"({max_length})"

            if not_null:
                self.SQL_OPERATION += " NOT NULL"
            if primary_key:
                self.SQL_OPERATION += " PRIMARY KEY"

    class INTEGER_NUMBER:
        SQL_OPERATION: str

        def __init__(self, max_length: int = 16, not_null: bool = False, primary_key: bool = False):
            self.SQL_OPERATION = "INTEGER"
            if max_length != 0:
                self.SQL_OPERATION += f"({max_length})"
            if not_null:
                self.SQL_OPERATION += " NOT NULL"
            if primary_key:
                self.SQL_OPERATION += " PRIMARY KEY"

    class STRING_LIST:
        SQL_OPERATION: str

        def __init__(self):
            self.SQL_OPERATION = "TEXT"
