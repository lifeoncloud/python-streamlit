from pymongo import MongoClient
import certifi

# 파이썬을 이용하여 MongoDB 데이터베이스 연결하기

# MongoDB 클러스터 연결 정보
CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<clustername>.vqisg.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
