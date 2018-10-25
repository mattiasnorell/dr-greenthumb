import sqlite3
from providers.Settings import Settings
from Singleton import Singleton

class SqliteDatabase(metaclass=Singleton):

    def __init__(self):
        
        print("Database up and running")
        settings = Settings()
        
        self.conn = sqlite3.connect(settings.config.database.path)
        self.curs = self.conn.cursor()

    def query(self, query, params):
        return self.curs.execute(query, params)

    def __del__(self):
        self.conn.close()