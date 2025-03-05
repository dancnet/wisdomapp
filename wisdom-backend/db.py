import sqlite3
import os
from contextlib import contextmanager

DB_PATH = "./data/knowledge.db"

@contextmanager
def db_open():
    if not os.path.exists(DB_PATH):
        # Install database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        with open("knowledge.sql", "r") as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        yield conn, cur
    except Exception as e:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

class df:
    def __init__(self, model):
        self.columns = []
        self.values = []
        for key, value in model.items():
            if value != None:
                self.columns.append(key)
                self.values.append(value)
    @property
    def insert_statement(self):
        columns = ', '.join(self.columns)
        placeholders = ', '.join(['?' for _ in self.columns])
        values = tuple(self.values)
        return columns, placeholders, values
    @property
    def update_statement(self):
        columns_placeholders = ', '.join([f'{col} = ?' for col in self.columns])
        values = tuple(self.values)
        return columns_placeholders, values