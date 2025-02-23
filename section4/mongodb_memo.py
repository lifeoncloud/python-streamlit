from pymongo import MongoClient
import certifi
import streamlit as st
from datetime import datetime, time

# Streamlit 활용 스케줄까지 포함된 메모장 만들기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net//?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['db_schedules']
collection = db['schedules']


def create_schedule(title, date, task, priority):
    datetime_obj = datetime.combine(date, time.min)
    schedule = {
        'title': title,
        'date': datetime_obj,
        'task': task,
        'priority': priority
    }
    collection.insert_one(schedule)


st.title('스케줄 메모 앱')

st.subheader('새로운 스케줄 추가하기')

title = st.text_input('제목')
date = st.date_input('날짜')
task = st.text_area('해야 할 일')
priority = st.selectbox('우선순위', ['낮음', '보통', '높음'])

if st.button('저장'):
    create_schedule(title, date, task, priority)
    st.success('스케줄이 저장되었습니다.')

st.write('---')
st.subheader('저장된 스케줄 목록')
schedules = collection.find()
for schedule in schedules:
    # json 형식으로 출력된다.
    # st.write(item) 
    
    # datetime 객체를 날짜 형식으로 변환하여 출력
    schedule_date = schedule['date'].date()
    st.write('제목:', schedule['title'])
    st.write('날짜:', schedule_date)
    st.write('해야 할 일:', schedule['task'])
    st.write('우선순위:', schedule['priority'])
    st.write('---')
