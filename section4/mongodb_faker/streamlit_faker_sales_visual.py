import streamlit as st
from pymongo import MongoClient
import certifi
import pandas as pd
import matplotlib.pyplot as plt

# 가상 회사 매출 데이터 시각화하기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['database_faker']
collection = db['sales']


def get_sales_data():
    sales_data = collection.find()
    df = pd.DataFrame(sales_data)
    return df

# 데이터 조회
st.header('매출 데이터 조회')
st.subheader('매출 데이터 표')
df_sales = get_sales_data()
st.dataframe(df_sales)
st.write('---')

# 데이터 통계
st.subheader('매출 통계')
st.write('총 매출: ', df_sales['amount'].sum())
st.write('평균 매출: ', df_sales['amount'].mean())
st.write('---')

# 데이터 시각화
st.subheader('매출 시각화')
plt.figure(figsize=(10, 6))

## 전체 데이터 시각화
plt.bar(df_sales['product'], df_sales['amount'])
plt.xlabel('product')
plt.ylabel('amount')
plt.xticks(rotation=45)
st.pyplot(plt)

## 상위 20개 시각화
# top_sales = df_sales.nlargest(20, 'amount')
# plt.bar(top_sales['product'], top_sales['amount'])
# plt.xlabel('product')
# plt.ylabel('amount')
# plt.xticks(rotation=45)
# st.pyplot(plt)
