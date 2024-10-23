import logging
import sqlite3
from pathlib import Path
log = logging.getLogger(__name__)


class SQLite:
    def __init__(self, db_name="hive.db"):
        if Path(db_name).exists():
            self.con = sqlite3.connect(db_name)
        else:
            self.con = sqlite3.connect(db_name)
            with self.con:
                self.con.execute("""
                    CREATE TABLE AGGREGATED (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        data json,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                    );
                """)

    def get_data(self):
        with self.con:
            return list(self.con.execute("SELECT * FROM AGGREGATED ORDER BY datetime(timestamp) DESC"))

    def add_data(self, data):
        with self.con:
            return self.con.execute(f"INSERT INTO AGGREGATED (data) VALUES ('{data}')")
