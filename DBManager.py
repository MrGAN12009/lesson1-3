import sqlite3

from Bron import Bron

class DBManager:
    def __init__(self):
        self.path = "db.db"
        self.connect = None
        self._init()



    def _init(self) -> None:
        '''Инициализация БД'''
        self._connect()
        c = self.connect.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(100) NOT NULL,
                    description VARCHAR(100) NOT NULL,
                    datetime DATETIME NOT NULL,
                    count INT NOT NULL,
                    price REAL NOT NULL,
                    location VARCHAR(100) NOT NULL);""")
        c.execute("""CREATE TABLE IF NOT EXISTS broni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INT NOT NULL,
            name VARCHAR(100) NOT NULL,
            count INT NOT NULL);""")

        self.connect.commit()
        return

    def add_event(self, title, description, datetime, count, price, location):
        try:
            self._connect()
            c = self.connect.cursor()
            c.execute("""INSERT INTO events 
                        (title, description, datetime, count, price, location)
                        VALUES(?, ?, ?, ?, ?, ?)""",
                      (title, description, datetime, count, price, location))
            self.connect.commit()
            return True
        except BaseException as e:
            print(e)
            return False

    def add_broni(self, event_id:int, bron: Bron):
        try:
            self._connect()
            c = self.connect.cursor()
            c.execute("""INSERT INTO broni (event_id, name, count) VALUES(?, ?, ?)""",
                      (event_id, bron.name, bron.count))

            self.connect.commit()
            return True
        except BaseException as e:
            print(e)
            return False


    def _connect(self):
        if self.connect is None:
            self.connect = sqlite3.connect(self.path)
            return self.connect
        return self.connect

    def _close(self):
        if self.connect is not None:
            self.connect.close()