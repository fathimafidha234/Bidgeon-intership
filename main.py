import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT NOT NULL,
        marks   REAL,
        grade   TEXT
    )
''')

# Insert
cursor.execute('INSERT INTO students (name, marks) VALUES (?, ?)', ('Ravi', 85.5))
conn.commit()

# Select
cursor.execute('SELECT * FROM students WHERE marks > ?', (75,))
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

