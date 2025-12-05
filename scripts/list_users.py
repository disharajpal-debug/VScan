from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.environ.get("DATABASE_NAME", "vscan")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users = list(db["users"].find({}, {"password": 0}))
print("Users:")
for u in users:
    print(u)
