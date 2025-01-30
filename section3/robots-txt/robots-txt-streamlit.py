import streamlit as st
import pandas as pd
import requests

def check_robots_txt(url):
    robot_url = f'{url}/robots.txt'
    response = requests.get(robot_url)
    return 'Yes' if response.status_code == 200 else 'No'

def main():
    st.title("사이트의 robots.txt 유무 확인하기")

    # csv 파일 업로드
    st.subheader("csv 파일 업로드")
    uploaded_file = st.file_uploader("사이트 URL이 포함된 csv파일을 업로드하세요", type=["csv"])

    if uploaded_file is not None:
        # csv 파일 읽기
        df = pd.read_csv(uploaded_file)

        # 'robots.txt 존재 여부' 열 추가하기
        df['robots.txt 존재 여부'] = df['URL'].apply(check_robots_txt)
        
        # 화면에 구분선 추가하기
        st.write("---")

        # 결과 출력하기
        st.subheader("사이트의 robots.txt 유무 확인 결과")
        st.dataframe(df)

if __name__ == "__main__":
    main()
