import sqlite3

class Database:
    def __init__(self, db_name="people.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                where_met TEXT,
                notes TEXT
            )
        """)
        self.connection.commit()