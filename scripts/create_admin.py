"""
Simple helper script to mark an existing user as admin (set role to 'admin').
Usage:
  & .\venv\Scripts\Activate.ps1; python .\scripts\create_admin.py --email admin@example.com

If the user does not exist, the script will print instructions to create the user via the web signup.
"""

import os
import argparse
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
# Use same defaults as the app
DB_NAME = os.environ.get("DATABASE_NAME", "vscan")
COLLECTION_NAME = os.environ.get("DB_COLLECTION_NAME", "users")

parser = argparse.ArgumentParser()
parser.add_argument("--email", required=True, help="Email of user to promote to admin")
args = parser.parse_args()

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users = db[COLLECTION_NAME]

email = args.email.lower()
user = users.find_one({"email": email})
if not user:
    # create a lightweight admin user with random password
    from flask_bcrypt import generate_password_hash
    import secrets

    random_pwd = secrets.token_urlsafe(12)
    try:
        hashed = generate_password_hash(random_pwd).decode("utf-8")
    except Exception:
        # fallback if flask_bcrypt not available in this context
        from bcrypt import hashpw, gensalt

        hashed = hashpw(random_pwd.encode("utf-8"), gensalt()).decode("utf-8")
    user_doc = {
        "name": "Administrator",
        "employee_id": f'admin_{int(__import__("time").time())}',
        "email": email,
        "password": hashed,
        "role": "admin",
    }
    users.insert_one(user_doc)
    print(
        f"Created admin user {email} with a random password. Use the web 'forgot password' flow to reset if needed."
    )
else:
    users.update_one({"email": email}, {"$set": {"role": "admin"}})
    print(f"User {email} updated to role 'admin'.")
