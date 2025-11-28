# 🚀 Visiting Card Reader is Running!

## ✅ Application Status

Your application is now **LIVE** and ready to use!

```
✓ Flask Server Running
✓ Listening on: http://localhost:5000
✓ Also accessible from: http://192.168.10.158:5000
```

---

## 🌐 Quick Access

### Local Access:
- **Main URL:** http://localhost:5000
- **Alternative:** http://127.0.0.1:5000

### Network Access (from other devices):
- **URL:** http://192.168.10.158:5000

---

## 📝 First Steps

### 1. **Create Account**
   - Go to http://localhost:5000
   - Click **"Sign Up"**
   - Fill in your details
   - Password must contain: uppercase, lowercase, number, special character

### 2. **Login**
   - Use email or employee ID
   - Enter password

### 3. **Upload Visiting Card**
   - Click **"Upload"** tab
   - Drag & drop an image or click to browse
   - Select image (JPG, JPEG, or PNG)
   - Click **"Extract Details"**
   - Wait for AI to extract information
   - Review and save

### 4. **View All Cards**
   - Click **"All Cards"** tab
   - Search, edit, delete cards
   - Export to CSV, Excel, or PDF

---

## 🔧 Configuration

Your `.env` file is already set up with:

```
✓ GEMINI_API_KEY - Configured
✓ FLASK_SECRET_KEY - Set
✓ MongoDB URI - localhost:27017
✓ SMTP - Ready (update with your credentials)
```

### Optional: Configure Email Notifications

To enable password reset emails:

1. Open `.env`
2. Update these values:
   ```
   SMTP_SERVER=smtp.gmail.com
   SMTP_USERNAME=your_email@gmail.com
   SMTP_PASSWORD=your_app_password
   SENDER_EMAIL=your_email@gmail.com
   ```
3. Restart the application

---

## 🛑 How to Stop the Server

In the terminal where the application is running:

```
Press CTRL+C
```

The server will shut down gracefully.

---

## 🚀 How to Restart

### Option 1: Using PowerShell (Easiest)
```powershell
.\run.ps1
```

### Option 2: Using Command Prompt
```cmd
run.bat
```

### Option 3: Manual (PowerShell)
```powershell
.\venv\Scripts\Activate.ps1
python back.py
```

### Option 4: Manual (Command Prompt)
```cmd
venv\Scripts\activate.bat
python back.py
```

---

## 📊 Features Available

### ✅ Implemented Features:
- User authentication (signup/login)
- AI-powered card detail extraction
- Card management (CRUD operations)
- Search & filter functionality
- Export to CSV, Excel, PDF
- Password reset via email
- Personal card sharing
- Google Sheets integration (admin only)
- Duplicate detection
- Responsive UI design

### 🔐 Security Features:
- Password hashing (bcrypt)
- Session management
- CSRF protection
- Input validation
- SQL injection prevention (using MongoDB)

---

## 📂 Project Structure

```
Visiting_card_reader/
├── back.py                              # Main Flask app
├── google_sheets_integration.py         # Google Sheets sync
├── requirements.txt                     # Dependencies
├── .env                                 # Configuration (SECRET!)
├── .gitignore                          # Git ignore rules
├── SETUP_AND_RUN.md                    # Detailed setup guide
├── run.ps1                             # PowerShell startup script
├── run.bat                             # Batch startup script
├── templates/                          # HTML pages
│   ├── index.html                      # Main app
│   ├── login.html
│   ├── signup.html
│   ├── personal_cards.html
│   ├── forgot_password.html
│   ├── reset_password.html
│   └── logout_redirect.html
├── static/                             # Images, CSS
│   ├── c4i4-logo.png
│   ├── green_theme.jpg
│   └── representation-ecology-sustainability.jpg
├── uploads/                            # Uploaded card images (auto-generated)
├── venv/                               # Virtual environment
└── __pycache__/                       # Python cache (auto-generated)
```

---

## 🐛 Troubleshooting

### Application won't start?

**Check MongoDB:**
```powershell
# Test MongoDB connection
mongosh
```

If MongoDB isn't running:
- Windows: Start MongoDB from Services or command line: `mongod`
- Or install from: https://www.mongodb.com/try/download/community

### Port 5000 already in use?

```powershell
# Find and kill the process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

### API errors?

Check `.env` file:
- Is `GEMINI_API_KEY` set? ✓
- Is MongoDB running? ✓
- Is internet connection working? ✓

---

## 📞 Support Information

### Before asking for help, verify:

1. **MongoDB is running**
   ```
   mongosh
   ```

2. **All requirements installed**
   ```
   pip list | findstr Flask pymongo
   ```

3. **.env file exists and is readable**
   ```
   Test-Path .env
   ```

4. **Port 5000 is available**
   ```
   netstat -ano | findstr :5000
   ```

---

## 🎯 Next Steps

1. **Create test accounts** - Try the signup/login flow
2. **Upload test cards** - Test the image processing
3. **Configure email** - Set up SMTP for notifications
4. **Deploy to production** - Follow SETUP_AND_RUN.md for production tips

---

## ⚡ Performance Notes

- **Development Server:** Good for testing, not production
- **For Production:** Use Gunicorn: `gunicorn -w 4 -b 0.0.0.0:5000 back:app`
- **Database:** MongoDB should be on SSD for best performance
- **Image Processing:** Requires internet (Gemini API)

---

## 📋 Checklist

- [x] Virtual environment created
- [x] Dependencies installed
- [x] .env configured
- [x] Flask server running
- [x] Ready to use!

---

**Status:** 🟢 **READY FOR TESTING**

**Application Running On:**
- Local: http://localhost:5000
- Network: http://192.168.10.158:5000

**Last Updated:** November 24, 2025

