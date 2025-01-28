import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

select_query = '''
    SELECT * FROM users WHERE id >= 2
'''

cursor.execute(select_query)
# 데이터 쿼리 결과 값중 모든 row를 가져온다
rows = cursor.fetchall()

for row in rows:
    # select_query에 해당하는 row를 print 한다
    print(row)

conn.close()
