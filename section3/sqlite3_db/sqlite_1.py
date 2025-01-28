import sqlite3

conn = sqlite3.connect('database.db')
# cursor는 가리킨다는 의미
cursor = conn.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
'''

cursor.execute(create_table)

conn.commit()
conn.close()
