import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

update_query = '''
    UPDATE users SET name = ? where id = ?
'''

data = ('choi', 2)
cursor.execute(update_query, data)

conn.commit()
conn.close()
