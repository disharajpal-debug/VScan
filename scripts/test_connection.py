#!/usr/bin/env python
"""
Test MongoDB connection and admin login.
"""
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DATABASE_NAME", "vscan")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "admin@c4i4.org")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "AdminPass123!")

print("=" * 60)
print("Testing MongoDB Connection & Admin Login")
print("=" * 60)

print(f"\n1. Testing MongoDB connection...")
print(f"   MONGO_URI: {MONGO_URI[:50]}...")
print(f"   DATABASE: {DB_NAME}")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Force connection attempt
    client.admin.command("ping")
    print("   ✅ MongoDB Connected Successfully!")

    db = client[DB_NAME]
    users_col = db["users"]
    cards_col = db["cards"]

    # Count documents
    user_count = users_col.count_documents({})
    card_count = cards_col.count_documents({})

    print(f"\n2. Database Statistics:")
    print(f"   ✅ Users in database: {user_count}")
    print(f"   ✅ Cards in database: {card_count}")

    # Check for admin user
    print(f"\n3. Checking Admin User...")
    admin_user = users_col.find_one({"email": ADMIN_EMAIL})
    if admin_user:
        print(f"   ✅ Admin user found: {ADMIN_EMAIL}")
        print(f"   ✅ Admin role: {admin_user.get('role', 'N/A')}")
        print(f"   ✅ Admin name: {admin_user.get('name', 'N/A')}")
    else:
        print(f"   ⚠️  Admin user NOT found. Creating...")
        bcrypt = Bcrypt()
        hashed = bcrypt.generate_password_hash(ADMIN_PASSWORD).decode("utf-8")
        users_col.insert_one(
            {
                "name": "Administrator",
                "employee_id": "admin_001",
                "email": ADMIN_EMAIL,
                "password": hashed,
                "role": "admin",
            }
        )
        print(f"   ✅ Admin user created successfully!")

    print(f"\n4. Admin Login Credentials:")
    print(f"   Email: {ADMIN_EMAIL}")
    print(f"   Password: {ADMIN_PASSWORD}")
    print(f"   ✅ Ready to use!")

    print("\n" + "=" * 60)
    print("✅ ALL CHECKS PASSED - System Ready!")
    print("=" * 60)

except Exception as e:
    print(f"\n   ❌ MongoDB Connection Failed!")
    print(f"   Error: {str(e)}")
    print("\n" + "=" * 60)
    print("TROUBLESHOOTING:")
    print("1. Check if MongoDB Atlas IP Whitelist includes your IP")
    print("2. Check if cluster is running (not paused)")
    print("3. Verify MONGO_URI is correct in .env")
    print("=" * 60)
