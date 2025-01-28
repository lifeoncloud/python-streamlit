import streamlit as st
from faker import Faker
import pandas as pd

# Faker 라이브러리 설치 필요
# pip3 install Faker

# pandas 라이브러리 설치 필요
# pip3 install pandas

fake = Faker()
st.title("가짜 데이터 정보 생성")

if "data" not in st.session_state:
    st.session_state["data"] = []

num_users = st.number_input("생성한 사용자 수", min_value=1, max_value=100)

if st.button("사용자 생성하기"):
    for _ in range(num_users):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        st.write(f"이름: {name}")
        st.write(f"이메일: {email}")
        st.write(f"주소: {address}")
        st.write("==============")
        st.session_state["data"].append({"이름": name, "이메일": email, "주소": address})

# 엑셀로 저장하기
if st.button("엑셀로 저장하기"):
    if not st.session_state["data"]:
        st.warning("생성된 사용자가 없습니다.")
    else:
        df = pd.DataFrame(st.session_state["data"])
        df.to_excel("생성사용자.xlsx", index=False)
        st.success("엑셀 파일 정상적으로 생성되었습니다.")

# csv파일로 저장하기
if st.button("csv로 저장하기"):
    if not st.session_state["data"]:
        st.warning("생성된 사용자가 없습니다.")
    else:
        df = pd.DataFrame(st.session_state["data"])
        df.to_csv("사용자파일.csv", index=False)
        st.success("csv 파일이 정상적으로 생성되었습니다.")

