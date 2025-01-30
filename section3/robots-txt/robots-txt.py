import streamlit as st
import requests

def main(url):
    robot_url = f'{url}/robots.txt'
    response = requests.get(robot_url)
    
    st.subheader("검색 결과")
    st.success("robots.txt 파일을 확인했습니다!")
    
    st.text(f"{url} 의 robots.txt 파일 내용은 다음과 같습니다.")
    st.write("---")
    st.text(response.text)

if __name__ == "__main__":
    st.title("사이트의 robots.txt 검색하기")
    url = st.text_input("사이트 URL을 입력하세요(예시 : https://example.com)")
    
    if st.button("검색"):
        main(url)
