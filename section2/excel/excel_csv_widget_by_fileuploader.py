import streamlit as st
import pandas as pd

st.subheader("엑셀 파일 업로드하기")
# 파일 업로더 위젯을 이용하여 엑셀 파일 출력하기
uploaded_xlsx = st.file_uploader("xlsx 파일 업로드", type=["xlsx"])
if uploaded_xlsx is not None:
    df = pd.read_excel(uploaded_xlsx)
    st.write(df)


# 파일 업로더 위젯을 이용하여 csv파일 출력하기
uploaded_csv = st.file_uploader("csv 파일 업로드", type=["csv"])
if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.write(df)
