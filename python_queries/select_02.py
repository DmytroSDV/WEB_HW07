# -- Знайти студента із найвищим середнім балом з певного предмета.

import sqlite3
import os

my_dir = os.path.dirname(os.path.abspath(__file__))
path_to_sql = os.path.join(my_dir, "../sql_queries/select_02.sql")
path_to_db = os.path.join(my_dir, "../register.db")


def execute_query():
    with open(path_to_sql, 'r', encoding='utf-8') as fh:
        query = fh.read()

    with sqlite3.connect(path_to_db) as con:
        cur = con.cursor()
        cur.execute(query)
        return cur.fetchall()


result = execute_query()
for res in result:
    print(res)
