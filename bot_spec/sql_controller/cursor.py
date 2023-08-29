from typing import Union, List
from .main import db
from .models import Models
import sqlite3


class TableController:
    TABLE_NAME: str

    def __init_subclass__(cls):
        variable_values = {name: value for name, value in cls.__dict__.items() if not name.startswith("__")}

        cls.TABLE_NAME = cls.__name__
        columns = variable_values
        compiled_columns = str()
        for name, value in columns.items():
            compiled_columns += f"{name} {value.SQL_OPERATION},"

        table = f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}({compiled_columns[:-1]});"
        db.execute(table, commit=True)

    def add_row(self, **kwargs):
        columns = str()
        values = str()
        for name, value in kwargs.items():
            columns += f"{name},"
            if type(value) == str:
                values += f"""'{value}',"""
            elif type(value) == int:
                values += f"{value},"
            elif type(value) == list:
                sort_value = str()
                for i in value:
                    sort_value += f"{i}$"
                values += f"""'{sort_value[:-1]}',"""

        db.execute(
            f"INSERT INTO {self.TABLE_NAME}({columns[:-1]}) VALUES({values[:-1]});",
            commit=True
        )

    def delete_row(self, **kwargs):
        columns = str()
        values = str()
        for name, value in kwargs.items():
            columns += f"{name},"
            if type(value) == str:
                values += f"""'{value}'#"""
            elif type(value) == int:
                values += f"{value}#"
            elif type(value) == list:
                sort_value = str()
                for i in value:
                    sort_value += f"{i}$"
                values += f"""'{sort_value[:-1]}'#"""

        command = str()
        ind = 0
        for column in columns[:-1].split(","):
            command += f"{column}={values[:-1].split('#')[ind]}"
            if ind + 1 != len(columns[:-1].split(",")):
                command += "AND"
            ind += 1
        db.execute(
            f"DELETE FROM {self.TABLE_NAME} WHERE {command};",
            commit=True
        )

    def clear_table(self):
        db.execute(f"DELETE FROM {self.TABLE_NAME} WHERE TRUE;", commit=True)

    def drop_table(self):
        db.execute(f"DROP TABLE {self.TABLE_NAME};")

    def select_row(self, **kwargs):
        columns = str()
        values = str()
        for name, value in kwargs.items():
            columns += f"{name},"
            if type(value) == str:
                values += f"""'{value}'#"""
            elif type(value) == int:
                values += f"{value}#"
            elif type(value) == list:
                sort_value = str()
                for i in value:
                    sort_value += f"{i}$"
                values += f"""'{sort_value[:-1]}'#"""

        command = str()
        ind = 0
        for column in columns[:-1].split(","):
            command += f"{column}={values[:-1].split('#')[ind]}"
            if ind + 1 != len(columns[:-1].split(",")):
                command += "AND"
            ind += 1
        result = db.execute(
            f"SELECT * FROM {self.TABLE_NAME} WHERE {command};",
            fetchone=True
        )

        return result

    def select_rows(self, **kwargs):
        columns = str()
        values = str()
        for name, value in kwargs.items():
            columns += f"{name},"
            if type(value) == str:
                values += f"""'{value}'#"""
            elif type(value) == int:
                values += f"{value}#"
            elif type(value) == list:
                sort_value = str()
                for i in value:
                    sort_value += f"{i}$"
                values += f"""'{sort_value[:-1]}'#"""

        command = str()
        ind = 0
        for column in columns[:-1].split(","):
            command += f"{column}={values[:-1].split('#')[ind]}"
            if ind + 1 != len(columns[:-1].split(",")):
                command += "AND"
            ind += 1

        result = db.execute(
            f"SELECT * FROM {self.TABLE_NAME} WHERE {command}",
            fetchall=True
        )
        return result

    def select_all_rows(self):
        result = db.execute(
            f"SELECT * FROM {self.TABLE_NAME} WHERE TRUE",
            fetchall=True
        )
        return result

    def update_row(self, find_row: dict, edit_column: str, edit_row: Union[str, int]):
        columns = str()
        values = str()
        for name, value in find_row.items():
            columns += f"{name},"
            if type(value) == str:
                values += f"""'{value}',"""
            elif type(value) == int:
                values += f"{value},"
            elif type(value) == list:
                sort_value = str()
                for i in value:
                    sort_value += f"{i}$"
                values += f"""'{sort_value[:-1]}',"""
        command = str()
        ind = 0
        for column in columns[:-1].split(","):
            command += f"{column}={values[:-1].split(',')[ind]}"
            if ind + 1 != len(columns[:-1].split(",")):
                command += "AND"
            ind += 1
        if type(edit_row) == str:
            edit_row = f"""'{edit_row}'"""
        elif type(edit_row) == list:
            sort_value = str()
            for i in edit_row:
                sort_value += f"{i}$"
            edit_row = f"""'{sort_value[:-1]}'"""
        db.execute(
            f"UPDATE {self.TABLE_NAME} SET {edit_column}={edit_row} WHERE {command};",
            commit=True
        )

    def update_rows(self, edit_column: str, edit_row: Union[str, int, list]):
        if type(edit_row) == str:
            edit_row = f"""'{edit_row}'"""
        elif type(edit_row) == list:
            sort_value = str()
            for i in edit_row:
                sort_value += f"{i}$"
            edit_row = f"""'{sort_value[:-1]}'"""
        db.execute(
            f"UPDATE {self.TABLE_NAME} SET {edit_column}={edit_row} WHERE TRUE;",
            commit=True
        )

    def count_table_data(self):
        return db.execute(f"SELECT COUNT(*) FROM {self.TABLE_NAME};", fetchone=True)[0]

    def clear_table_data(self):
        db.execute(f"DELETE FROM {self.TABLE_NAME} WHERE TRUE;", commit=True)

    def drop_table(self):
        db.execute(f"DROP TABLE {self.TABLE_NAME};", commit=True)
