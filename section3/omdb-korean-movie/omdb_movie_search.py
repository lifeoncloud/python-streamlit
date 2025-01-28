import requests
import streamlit as st

def search_movies(title):
    # OMDB API 요청을 위한 URL
    url = f"http://www.omdbapi.com/?apikey=[API KEY]&t={title}"
    
    try:
        # API 요청 보내기
        response = requests.get(url, timeout=10)
        
        # 응답 데이터 확인
        data = response.json()
        
        if data["Response"] == "False":
            return None
        
        # 영화 정보 목록 추출
        movie_list = data["Search"]
        st.write(movie_list)
        return movie_list
    except requests.exceptions.RequestException as e:
        st.error(f"API 요청 중 오류가 발생했습니다: {e}")
        return None

# Streamlit 애플리케이션 시작
st.title("영화 검색 앱 - search")
movie_title = st.text_input("영화 제목을 입력하세요")

if st.button("검색"):
    if movie_title:
        movie_list_results = search_movies(movie_title)
        
        if movie_list_results is not None:
            st.subheader(f"검색 결과 {len(movie_list_results)} 개의 영화가 있습니다.")
            
            for movie in movie_list_results:
                details = get_movie_details(movie["imdbID"], api_key)
                title = movie["Title"]
                year = movie["Year"]
                poster = movie["Poster"]
                country = movie["Country"]
                language = movie["Language"]
                
                # 영화 정보 출력
                st.write("제목:", title)
                st.write("제작년도:", year)
                st.write("국가:", country)
                st.write("언어:", language)
                st.image(poster, caption=title)
                st.write("---")
        else:
            st.error("검색 결과를 찾을 수 없습니다.")
    else:
        st.warning("영화 제목을 입력하세요.")
