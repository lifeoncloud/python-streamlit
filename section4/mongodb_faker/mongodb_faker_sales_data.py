from pymongo import MongoClient
import certifi
from faker import Faker

# 가상 회사 매출 데이터 200개 생성하기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

# 데이터베이스 및 컬렉션 선택하기
db = client['database_faker']
collection = db['sales']

fake = Faker()

for _ in range(200):
    # 1단계: sale 이라는 dictionary에 데이터 200개 생성하기
    sale = {
        'company' : fake.company(),
        'product' : fake.word(),
        'amount' : fake.random_int(min=3000, max=10000)
    }
    # 2단계: 'sales' collection에 한번에 다 집어넣기
    collection.insert_one(sale)
        
print("가상 회사 매출 데이터를 생성 후 저장했습니다.")
