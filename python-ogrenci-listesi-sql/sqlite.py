import sqlite3

conn = sqlite3.connect("datatable.db")

conn.execute('''CREATE TABLE OGRENCILER (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NAME TEXT NOT NULL,
		SURNAME TEXT NOT NULL,
		AGE INT NOT NULL,
		WORK TEXT NOT NULL
		);''')

conn.close()
