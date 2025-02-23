import streamlit as st
from pymongo import MongoClient
import certifi

# Streamlit 활용하여 Mongodb 데이터 추가 및 조회

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['database_test']
collection = db['mycollection']

st.title('MongoDB 데이터 추가 및 조회')

st.header('데이터 추가하기')

title = st.text_input("제목")
author = st.text_input('작성자')
content = st.text_input('내용')

if st.button('추가'):
    data = {'author': author, 'title': title, 'content': content}
    collection.insert_one(data)
    st.success('데이터가 정상적으로 추가되었습니다.')

st.write('---')

st.header('데이터 조회하기')

data = collection.find()

for item in data:
    st.write('작성자:', item['author'])
    st.write('제목: ', item['title'])
    st.write('내용: ', item['content'])
    st.write('---')
