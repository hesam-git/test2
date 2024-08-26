import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute( """
                            CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY,
                            name text, family text, address text, phone text)
                            """)
        self.con.commit()


db1 = Database('d:/mydata8.db')        