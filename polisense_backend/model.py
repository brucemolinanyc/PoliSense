import sqlite3


class Model:

    def __init__(self, datapath):
        self.database = datapath

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, type, value, traceback):
        if not type:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def add_task(self):
        pass

    def lookup_task(self, id):
        pass