import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

delete_query = '''
    DELETE FROM users WHERE id = ?
'''

# 2외에 아무 값도 지정하지 않겠다
data = (2,)
cursor.execute(delete_query, data)

conn.commit()
conn.close()
