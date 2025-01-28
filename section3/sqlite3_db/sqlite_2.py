import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

insert_query = '''
    INSERT INTO users (name, email)
    VALUES (?, ?)
'''
# VALUES에 static하게 입력도 가능하나, 추후 재사용하기 어렵다.
data = ('kim', 'kim@c.com')
cursor.execute(insert_query, data)

# commit은 생성/변경/삽입시 저장하는 역할
conn.commit()
conn.close()
