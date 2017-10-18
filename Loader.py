import sqlite3
import csv


class Loader:
    def __init__(self, _csv, _db):
        self.csv = _csv
        self.data_base = _db
        self.conn = None
        self.db = None
        self.create_table = """CREATE TABLE IF NOT EXISTS Rates (ExName text NOT NULL, Quantity float NOT NULL, 
                                                                 Rate float NOT NULL);"""
        self.erase_table = """DELETE FROM Rates"""

        self.__data_base_init()

    def __data_base_init(self):
        self.conn = sqlite3.connect(self.data_base)
        self.db = self.conn.cursor()

        self.db.execute(self.create_table)
        self.db.execute(self.erase_table)

    def save_to_db(self):
        with open(self.csv, "r", newline='', encoding='utf8') as in_file:
            csv_reader = csv.reader(in_file, delimiter=',')

            for row in csv_reader:
                row[1] = float(row[1])
                row[2] = float(row[2])
                self.db.execute('INSERT INTO Rates VALUES (?,?,?)', row)

        self.conn.commit()
        self.conn.close()



