"""
Set a user's role. Example:
  python .\scripts\set_role.py --email user@example.com --role admin
"""
import os
import argparse
from pymongo import MongoClient

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.environ.get('DATABASE_NAME', 'visiting_card')
COLLECTION_NAME = os.environ.get('DB_COLLECTION_NAME', 'users')

parser = argparse.ArgumentParser()
parser.add_argument('--email', required=True)
parser.add_argument('--role', required=True, choices=['admin','user'])
args = parser.parse_args()

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users = db[COLLECTION_NAME]

res = users.update_one({'email': args.email.lower()}, {'$set': {'role': args.role}})
if res.matched_count == 0:
    print('No such user. Use signup page to create user first.')
else:
    print(f"Updated {args.email} to role '{args.role}'")
