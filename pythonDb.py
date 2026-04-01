
import sqlite3
conn = sqlite3.connect('mydatabase.db')
print("Opened database successfully")
cursor = conn.cursor()
sql_create_table = """
CREATE TABLE IF NOT EXISTS students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    VARCHAR(50) NOT NULL,
    grade   INTEGER,
    section CHAR(1)
)
"""
conn.execute(sql_create_table)
conn.commit()
print("Table created successfully")

sql_insert = "INSERT INTO students(name,grade,section) VALUES (?,?,?)"
record = ("Dinesh", 85, 'A')
cursor.execute(sql_insert, record)
conn.commit()


# Multiple record at once

sql_insert=" INSERT INTO students(name,grade,section) VALUES (?,?,?)"
records = [
    ("Dinesh raj", 90, 'A'),
    ("Kripa", 85, 'B'),
    ("Aagyaven", 95, 'A')
]
cursor.executemany(sql_insert, records)
conn.commit()
print("Records inserted successfully")