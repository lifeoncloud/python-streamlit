import streamlit as st
import sqlite3

conn = sqlite3.connect('memo.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS memos (contents TEXT)''')

st.title("메모장 애플리케이션")

memo = st.text_area("메모 입력", height=200)
save_button = st.button("저장")

if save_button:
    cursor.execute('INSERT INTO memos VALUES (?)', (memo,))
    conn.commit()
    st.success('메모가 저장되었습니다.')
    

st.subheader('저장된 메모')
cursor.execute('SELECT * FROM memos')

# fetch all은 모든 것들을 가져온다.
saved_memos = cursor.fetchall()

if saved_memos:
    for saved_memo in saved_memos:
        st.write(saved_memo[0])
else:
    st.info('저장된 메모가 없습니다.')


conn.close()
