import requests
import streamlit as st


def search_movie(title):
    # OMDB API 요청을 위한 URL
    url = f"http://www.omdbapi.com/?apikey=[API KEY]&t={title}"
    
    # API 요청 보내기
    response = requests.get(url)
    
    # 응답 데이터 json 형태로 확인
    data = response.json()
    # st.write(data)
    
    if data["Response"] == "False":
        return None
    
    # 영화 정보 추출
    # st.write(data)
    movie_title = data["Title"]
    # movie_year = data["Year"]
    movie_poster = data["Poster"]
    movie_country = data["Country"]
    movie_language = data["Language"]
    
    # # 테스트
    # st.write(data)
    return movie_title, movie_poster, movie_country, movie_language

# Streamlit 애플리케이션 시작
st.title("영화 검색 앱 - title, 국가")
movie_title = st.text_input("영화 제목을 입력하세요")

# 한국어 영화 찾기
if st.button("한국어 영화 검색"):
    if movie_title:
        movie_data = search_movie(movie_title)
        if movie_data is not None:
            title, poster, country, language = movie_data
            if "Korean" in language:
                # 영화 정보 출력
                st.subheader("한국어 영화 검색 결과")
                st.write("제목:", title)
                # st.write("제작년도:", year)
                st.write("국가:", country)
                st.write("언어:", language)
                # 포스터 정보에서 use_column_width는 deprecated되었음
                st.image(poster, caption=title)
            else:
                st.error("한국어 영화 검색 결과를 찾을 수 없습니다.")
        else:
            st.error("검색 결과를 찾을 수 없습니다.")
    else:
        st.warning("영화 제목이 없어서 검색을 못해요.")



# 한국영화 찾기
if st.button("한국영화 검색"):
    if movie_title:
        movie_data = search_movie(movie_title)
        if movie_data is not None:
            title, poster, country, language = movie_data
            if country == "South Korea":
                # 영화 정보 출력
                st.subheader("한국영화 검색 결과")
                st.write("제목:", title)
                # st.write("제작년도:", year)
                st.write("국가:", country)
                st.write("언어:", language)
                # 포스터 정보에서 use_column_width는 deprecated되었음
                st.image(poster, caption=title)
            else:
                st.error("한국영화 검색 결과를 찾을 수 없습니다.")
        else:
            st.error("검색 결과를 찾을 수 없습니다.")
    else:
        st.warning("영화 제목이 없어서 검색을 못해요.")
