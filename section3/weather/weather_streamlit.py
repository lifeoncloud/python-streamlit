import requests
import streamlit as st

# 현재 날씨 가져오기 : https://openweathermap.org/current
# 참고 용어 : latitude(위도), longitude(경도)

def main():
    # Streamlit 앱
    st.title("도시 날씨 알리미")
    city = st.text_input("도시 이름을 작성하세요(영문): ")
    api_key = "MY_API_KEY_MY_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # city 변수가 main()함수 안에 선언되어야 한다.
    
    response = requests.get(url)
    weather_data = response.json()
    
    if st.button("도시 날씨 조회하기"):
        if weather_data["cod"] == 200:
            st.write(f"=== {city} 의 날씨를 알려드립니다. ===")
            st.write(f"현재 온도는 {weather_data["main"]["temp"]} 도 입니다.")
            st.write(f"체감 온도는 {weather_data["main"]["feels_like"]} 도 입니다.")
        else:
            st.warning("날씨 정보를 가려오는 중 오류가 발생했습니다.")
            st.info("도시 이름을 영문으로 정확하게 입력해주세요.")

if __name__ == "__main__":
    main()
