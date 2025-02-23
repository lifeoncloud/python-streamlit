import streamlit as st
from pymongo import MongoClient
import certifi
from datetime import datetime, time

# streamlit 활용 사이드바 선택 위젯을 이용한 상품 등록 목록 페이지

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['product_database']
collection = db['products']

# 사이드바 메뉴
st.sidebar.title('메뉴')
selection = st.sidebar.radio("이동할 페이지", ("상품 등록", "상품 목록"))

if selection == "상품 등록":
    st.title("상품 등록 페이지")
    
    product_name = st.text_input("상품 이름")
    registration_date = st.date_input("등록 날짜")
    registration_datetime = datetime.combine(registration_date, datetime.now().time())
    image_upload = st.file_uploader("이미지 업로드")
    product_price = st.number_input("상품 가격")
    
    if st.button('상품 등록하기'):
        product = {
            "상품 이름" : product_name,
            "등록 날짜" : registration_datetime,
            "상품 이미지" : image_upload.read(),
            "상품 가격" : product_price
        }
        collection.insert_one(product)
        st.success('상품이 등록되었습니다.')

else : 
    st.title("상품 목록 페이지")
    products = collection.find()
    for product in products:
        st.write('상품 이름:', product['상품 이름'])
        st.write('등록 날짜:', product['등록 날짜'])
        st.write('상품 가격:', product['상품 가격'])
        st.image(product["상품 이미지"])
        st.write('---')
        
    
