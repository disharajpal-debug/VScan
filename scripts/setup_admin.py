#!/usr/bin/env python
"""
Helper script to create or update an admin user.
Usage:
  python scripts/setup_admin.py --email admin@example.com --password "MyPass123!"
  python scripts/setup_admin.py  # defaults to admin@c4i4.org with auto-generated password
"""

from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.environ.get("DATABASE_NAME", "visiting_card")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]

bcrypt = Bcrypt()

def setup_admin(email="admin@c4i4.org", password=None):
    """Create or update an admin user."""
    email = email.lower().strip()
    
    if not password:
        # Generate a default password if not provided
        import secrets
        password = secrets.token_urlsafe(12)
        print(f"Generated password: {password}")
    
    # Hash the password
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Check if user exists
    user = users_collection.find_one({"email": email})
    
    if user:
        # Update existing user
        users_collection.update_one(
            {"email": email},
            {
                "$set": {
                    "password": hashed,
                    "role": "admin",
                    "name": "Administrator"
                }
            }
        )
        print(f"✓ Updated existing admin user: {email}")
    else:
        # Create new admin user
        import time
        users_collection.insert_one({
            "name": "Administrator",
            "employee_id": f"admin_{int(time.time())}",
            "email": email,
            "password": hashed,
            "role": "admin"
        })
        print(f"✓ Created new admin user: {email}")
    
    print(f"✓ Admin user is ready to log in!")
    print(f"  Email: {email}")
    print(f"  Password: {password}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up an admin user")
    parser.add_argument("--email", default="admin@c4i4.org", help="Admin email (default: admin@c4i4.org)")
    parser.add_argument("--password", help="Admin password (auto-generated if not provided)")
    
    args = parser.parse_args()
    setup_admin(args.email, args.password)
