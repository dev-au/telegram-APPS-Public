import sqlite3


class Database:
    def __init__(self, path_to_db):
        self.path_to_db = f"{path_to_db}/main.db"

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            user_id int NOT NULL,
            user_language varchar,
            PRIMARY KEY (user_id)
            );
"""
        self.execute(sql, commit=True)

    def add_user(self, user_id: int, user_language: str):
        sql = """
        INSERT INTO Users(user_id, user_language) VALUES(?, ?)
        """
        self.execute(sql, parameters=(user_id, user_language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_lang(self, user_id, lang):
        sql = f"""UPDATE Users SET user_language=? WHERE user_id=?"""
        return self.execute(sql, parameters=(lang, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def delete_user(self, user_id):
        sql = f"""
        DELETE FROM Users WHERE user_id=?
        """
        return self.execute(sql, user_id, commit=True)
