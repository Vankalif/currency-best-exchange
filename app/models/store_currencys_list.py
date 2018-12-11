import sqlite3
from app.utils.paths import db_path, sql_scripts_path
from app.utils.sql_scripts_reader import read_sql


def store(currencys: dict) -> bool:
    with sqlite3.connect(db_path() / 'main.db') as connection:
        cursor = connection.cursor()
        cursor.execute(read_sql(sql_scripts_path() / 'currencys_model.sql'))

        for curr_key, curr_val in zip(currencys.keys(), currencys.values()):
            cursor.execute("INSERT INTO currencys VALUES (?, ?)", (curr_key, curr_val))
