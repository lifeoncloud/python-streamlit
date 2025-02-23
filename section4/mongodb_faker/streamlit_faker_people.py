import streamlit as st
from pymongo import MongoClient
import certifi

# Streamlit 활용 mongodb에 가짜 정보 추가 및 조회 웹 서비스

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['database_faker']
collection = db['people']

# 필드 선택 옵션
fields = {
        '이름': 'name', 
        '이메일': 'email',
        '주소': 'address'
        }


# 검색 필드 선택
selected_field = st.selectbox('검색할 필드 선택', list(fields.keys()))

# 검색어 입력
search_term = st.text_input('검색어 입력')

# 검색 결과 출력
st.subheader('검색 결과')
results = collection.find({fields[selected_field]: {'$regex': search_term, '$options': 'i'}})
for result in results:
    st.write(result)
