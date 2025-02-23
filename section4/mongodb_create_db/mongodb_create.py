from pymongo import MongoClient
import certifi

# 파이썬을 이용한 MongoDB 데이터베이스 생성 및 데이터 추가하기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['database_test']
collection = db['mycollection']

# 컬렉션에 데이터 삽입하기
post = {"title": "n번째 포스트", "content": "안녕하세요! Lorem Ipsum!", "author": "Various Artists"}
post_id = collection.insert_one(post).inserted_id
print("삽입된 문서 ID:", post_id)

# 컬렉션에 "author" 정보로 데이터 검색하기
result = collection.find_one({"author": "Various Artists"})
print("검색된 문서:", result)
