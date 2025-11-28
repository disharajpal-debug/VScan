# 🚀 Visiting Card Reader - Setup and Run Guide

## Prerequisites

- Python 3.10+ installed
- MongoDB running locally on `localhost:27017` (or configured in `.env`)
- (Optional) Gmail account with App Password for email functionality

---

## Step 1: Activate Virtual Environment

```powershell
# Navigate to project directory
cd C:\Users\admin\Visiting_card_reader

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

**Note:** Your prompt should now show `(venv)` at the beginning.

---

## Step 2: Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs all required packages:
- Flask 2.3.3
- MongoDB driver
- Google Sheets integration
- Email sending capabilities
- And more...

---

## Step 3: Configure Environment Variables

The `.env` file has been created with all necessary configurations. Update it with your credentials:

### Critical Settings to Update:

**File:** `.env`

```bash
# GEMINI_API_KEY - Your Google Gemini API key (already set)
GEMINI_API_KEY=your_actual_key_here

# SMTP Configuration (for email notifications)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password_here  # Use Gmail App Password, not regular password
SENDER_EMAIL=your_email@gmail.com

# MongoDB Configuration (change if not running locally)
MONGO_URI=mongodb://localhost:27017/

# Flask Secret Key (already set - keep as is for development)
FLASK_SECRET_KEY=60eb852b9adf0e0ab32c320554b7efc316ac1cce3cf8ea34f7ad15fa13a86928

# Other Settings (leave as is unless you have specific needs)
FLASK_ENV=development
DATABASE_NAME=visiting_card
DB_COLLECTION_NAME=cards
GEMINI_MODEL=gemini-2.0-flash
SESSION_COOKIE_SECURE=False
```

### How to Get Gmail App Password:
1. Enable 2-Factor Authentication on Google Account
2. Go to https://myaccount.google.com/apppasswords
3. Select "Mail" and "Windows Computer"
4. Copy the generated password to `.env`

---

## Step 4: Start MongoDB

**Option A: If MongoDB is installed as a service**

```powershell
# Start MongoDB service
net start MongoDB

# Or using mongo commands
mongod
```

**Option B: If MongoDB is not installed**

Download from: https://www.mongodb.com/try/download/community

---

## Step 5: Run the Application

### Development Mode:

```powershell
# Make sure you're in the project directory and venv is activated
python back.py
```

**Output should show:**
```
 * Serving Flask app 'back'
 * Debug mode: off
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

### Access the Application:

Open your browser and go to:
```
http://localhost:5000
```

---

## Step 6: Create Your First Account

1. Click **"Sign Up"** on the login page
2. Enter:
   - **Name:** Your full name
   - **Employee ID:** 4-digit number (e.g., 1001)
   - **Email:** Your email
   - **Password:** Must have:
     - 8+ characters
     - Uppercase letter
     - Lowercase letter
     - Number
     - Special character (!@#$% etc.)
   - **Confirm Password:** Repeat password
3. Click **Sign Up** → You'll be redirected to login
4. Login with email or employee ID

---

## Step 7: Test the Application

### Upload a Visiting Card:

1. Click **Upload** tab
2. Drag & drop a visiting card image or click to browse
3. Supported formats: JPG, JPEG, PNG
4. Click **Extract Details**
5. Wait for AI to extract information
6. Review and save the card

### View All Cards:

1. Click **All Cards** tab
2. See all scanned/shared cards in a table
3. Search, edit, delete, or export cards
4. Export options: CSV, Excel, PDF

### Personal Cards (if not admin):

1. Click **Personal Cards** tab
2. See only your scanned cards
3. Share cards with everyone (toggle Share button)

---

## Troubleshooting

### Issue: MongoDB Connection Error

**Error:** `pymongo.errors.ServerSelectionTimeoutError`

**Solution:**
1. Check if MongoDB is running: `mongosh` or `mongo`
2. If not installed, download from mongodb.com
3. Update `MONGO_URI` in `.env` if running on different host/port

### Issue: Gemini API Key Error

**Error:** `GEMINI_API_KEY not found in environment variables`

**Solution:**
1. Open `.env` file
2. Verify `GEMINI_API_KEY` is set correctly
3. Don't forget to save the file
4. Restart the application

### Issue: Port 5000 Already in Use

**Error:** `OSError: [Errno 10048] Only one usage of each socket address`

**Solution:**

```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Or change port in back.py (last line):
# app.run(debug=False, host="0.0.0.0", port=5001)  # Change 5000 to 5001
```

### Issue: SMTP/Email Not Working

**Check:**
1. Gmail App Password is correct (not regular password)
2. 2FA is enabled on Gmail account
3. SMTP_SERVER and SMTP_PORT are correct
4. SENDER_EMAIL matches your Gmail

### Issue: Can't Extract Card Details

**Check:**
1. Image is clear and readable
2. Image format is JPG, JPEG, or PNG
3. File size is reasonable (under 10MB)
4. Gemini API key is valid
5. Internet connection is working

---

## Environment Variables Reference

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | development | Flask environment mode |
| `FLASK_SECRET_KEY` | - | Secret key for session encryption |
| `GEMINI_API_KEY` | - | Google Gemini API key |
| `GEMINI_MODEL` | gemini-2.0-flash | AI model to use |
| `MONGO_URI` | mongodb://localhost:27017/ | MongoDB connection string |
| `DATABASE_NAME` | visiting_card | Database name |
| `DB_COLLECTION_NAME` | cards | Collection name |
| `SMTP_SERVER` | smtp.example.com | Email server |
| `SMTP_PORT` | 587 | Email server port |
| `SMTP_USERNAME` | your_email@example.com | Email username |
| `SMTP_PASSWORD` | - | Email password or app password |
| `SENDER_EMAIL` | your_email@example.com | From email address |
| `PRIVILEGED_USER` | ashutosh.lab@c4i4.com | Admin user email |
| `SESSION_COOKIE_SECURE` | False | HTTPS only (True in production) |
| `SESSION_COOKIE_HTTPONLY` | True | JavaScript cannot access cookie |
| `SESSION_COOKIE_SAMESITE` | Lax | CSRF protection level |

---

## Production Deployment

For production deployment:

1. **Update `.env`:**
   ```bash
   FLASK_ENV=production
   SESSION_COOKIE_SECURE=True  # Requires HTTPS
   ```

2. **Use Gunicorn instead of Flask:**
   ```powershell
   gunicorn -w 4 -b 0.0.0.0:5000 back:app
   ```

3. **Run behind Nginx/Apache** for SSL/TLS

4. **Use production MongoDB** with authentication

5. **Set up proper error logging and monitoring**

---

## File Structure

```
Visiting_card_reader/
├── back.py                          # Main Flask application
├── google_sheets_integration.py     # Google Sheets integration
├── requirements.txt                 # Python dependencies
├── .env                            # Environment variables (KEEP SECURE!)
├── .gitignore                      # Git ignore file
├── README.md                       # Project documentation
├── SETUP_AND_RUN.md               # This file
├── venv/                           # Virtual environment
├── uploads/                        # Uploaded card images
├── templates/                      # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── forgot_password.html
│   ├── reset_password.html
│   ├── personal_cards.html
│   └── logout_redirect.html
├── static/                         # Static files (CSS, images, fonts)
│   ├── green_theme.jpg
│   ├── c4i4-logo.png
│   └── representation-ecology-sustainability.jpg
└── __pycache__/                   # Python cache (auto-generated)
```

---

## Quick Start (TL;DR)

```powershell
# 1. Activate environment
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure .env (update SMTP and API keys)
# Edit .env file with your credentials

# 4. Start MongoDB (ensure it's running)
mongod

# 5. Run the app
python back.py

# 6. Open browser to http://localhost:5000
```

---

## Support & Debugging

**Enable Debug Logging:**

Edit `back.py` and change:
```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Set debug=True
```

**View Logs:**

Logs will appear in the console where you ran `python back.py`

---

**Last Updated:** November 24, 2025
**Version:** 1.0
**Status:** ✅ Ready for Development

