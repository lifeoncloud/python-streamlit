import streamlit as st
from pymongo import MongoClient
import certifi

# 선택한 데이터베이스와 컬렉션의 문서 조회하기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())


# 데이터베이스 및 컬렉션 선택하기
database_names = client.list_database_names()

st.title("MongoDB의 데이터베이스 정보")
st.header("데이터베이스 선택하기")
selected_database = st.selectbox("데이터베이스 목록:", database_names)


if selected_database:
    st.write(f"선택한 데이터 베이스 이름 : {selected_database}")
    st.write("---")
    db = client[selected_database]
    collection_names = db.list_collection_names()    
    
    
    st.header("컬렉션 선택하기")
    selected_collection = st.selectbox("컬렉션 목록:", collection_names)
    if selected_collection:
        st.write(f"선택한 컬렉션 이름 : {selected_collection}")
        collection = db[selected_collection]
        st.write("---")

        
        st.subheader(f"{selected_collection}컬렉션의 상위 10개 문서")
        documents = collection.find().limit(10)
        
        for document in documents:
            st.write(document)
