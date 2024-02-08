import sqlite3


def create_db():
    with open('register.sql', 'r', encoding='utf-8') as fh:
        query = fh.read()

    with sqlite3.connect('register.db') as con:
        cur = con.cursor()
        cur.executescript(query)


if __name__ == "__main__":
    create_db()
