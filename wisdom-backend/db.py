import sqlite3
from contextlib import contextmanager

@contextmanager
def db_open():
    conn = sqlite3.connect('knowledge.db')
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