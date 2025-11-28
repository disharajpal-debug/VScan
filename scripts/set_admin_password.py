from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
from flask_bcrypt import Bcrypt
from flask import Flask
app=Flask(__name__)
bcrypt=Bcrypt(app)
MONGO_URI=os.environ.get('MONGO_URI','mongodb://localhost:27017/')
DB_NAME=os.environ.get('DATABASE_NAME','vscan')
client=MongoClient(MONGO_URI)
db=client[DB_NAME]
users=db['users']
email='admin@c4i4.org'
new_pw='AdminPass123!'
hashed=bcrypt.generate_password_hash(new_pw).decode('utf-8')
res=users.update_one({'email':email},{'$set':{'password':hashed}})
print('Matched:',res.matched_count,'Modified:',res.modified_count)
print('Password set to:', new_pw)
