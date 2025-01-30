import requests

# 현재 날씨 가져오기 : https://openweathermap.org/current
# 참고 용어 : latitude(위도), longitude(경도)

api_key = "MY_API_KEY_MY_API_KEY"
city = input("도시 이름을 작성하세요(영문): ")
# url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}&units=metric"
# &units=metric : 화씨 -> 섭씨로 변경
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
weather_data = response.json()

print(f"=== {city} 의 날씨를 알려드립니다. ===")
print(f"현재 온도는 {weather_data["main"]["temp"]} 도 입니다.")
print(f"체감 온도는 {weather_data["main"]["feels_like"]} 도 입니다.")
