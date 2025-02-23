from pymongo import MongoClient
import certifi
from faker import Faker

# 가상 사용자 데이터 20개 생성하기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['database_faker']
collection = db['people']

fake = Faker()

for _ in range(20):
    # 1단계: person 이라는 dictionary에 데이터 20개 생성하기
    person = {
        'name' : fake.name(),
        'address' : fake.address(),
        'email' : fake.email(),
        'phone' : fake.phone_number()
    }
    # 2단계: 'people' collection에 한번에 다 집어넣기
    collection.insert_one(person)

print("가상 사용자 데이터를 생성 후 저장했습니다.")
