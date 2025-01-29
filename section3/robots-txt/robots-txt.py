import streamlit as st
import requests

def main(url):
    robot_url = f'{url}/robots.txt'
    response = requests.get(robot_url)
    st.text(response.text)

if __name__ == "__main__":
    st.title("사이트 정보 검색")
    url = st.text_input("사이트 URL을 입력하세요:")
    
    if st.button("검색"):
        main(url)
