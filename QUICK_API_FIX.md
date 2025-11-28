# 🚨 Quick Fix: Getting a New API Key (5 Minutes)

## The Problem
Your Gemini API key has hit its daily limit (1,500 requests).

## The Solution
Get a new API key from Google.

---

## 🏃 FASTEST WAY (5 min - Free but temporary)

### Step 1: Get New Key
Go to: **https://makersuite.google.com/app/apikey**
- Sign in with Google
- Click "Create API Key"
- Click "Create API key in new project"
- Copy the new key

### Step 2: Update .env
Open: `C:\Users\admin\Visiting_card_reader\.env`

Find this line:
```
GEMINI_API_KEY=AIzaSyCRqqHVz4V4OCS6TrYMhKgzkmyXzUTYF-4
```

Replace with your new key (just paste, no quotes):
```
GEMINI_API_KEY=AIza...your_new_key_here...
```

Save file (Ctrl+S)

### Step 3: Restart Flask
In PowerShell:
```powershell
# Press CTRL+C first (to stop current Flask)
python back.py
```

### Step 4: Test
- Go to http://localhost:5000
- Upload a card
- Should work! ✅

---

## 💳 BETTER WAY (15 min - Unlimited, cheap)

### Step 1: Enable Billing
Go to: **https://console.cloud.google.com/**
1. Click "Select a project"
2. Click "New Project" 
3. Name it: `visiting-card-reader`
4. Click "Create"
5. Wait 30 seconds

### Step 2: Add Payment Method
1. Left menu → "Billing"
2. Click "Link Billing Account"
3. Click "Create Billing Account"
4. Add your credit card
5. Accept terms
6. Done! (You won't be charged, you get $300 free)

### Step 3: Enable API
1. Left menu → "API & Services" → "Library"
2. Search: `generative language`
3. Click the result
4. Click "Enable"

### Step 4: Get New Key
1. Left menu → "API & Services" → "Credentials"
2. Click "Create Credentials" → "API Key"
3. Copy the key

### Step 5: Update .env
Same as above - replace old key with new one

### Step 6: Restart & Test
```powershell
python back.py
```

---

## 📊 What's the Difference?

| | Free Key | Paid Key |
|---|----------|----------|
| Cost | $0 | $0 (first $300) |
| Daily Limit | 1,500 requests | Unlimited* |
| Per Minute | 60 requests | 1,500 requests |
| Per Card | Included | ~$0.001 |
| How Long | Few days | Months with free credits |

*Paid key needs credit card linked for billing

---

## ❓ Common Questions

**Q: Will I be charged?**
A: No! You get $300 free credits first month.

**Q: How do I stop being charged later?**
A: Disable billing in Google Cloud Console.

**Q: Which option should I use?**
A: Option 2 (Paid) - it's only 15 min and solves the problem permanently.

**Q: Do I need a new key?**
A: Yes, new keys get fresh quota.

---

## 🔍 Troubleshooting

**Error: "API key invalid"**
- Make sure you copied key correctly
- No spaces or quotes
- Wait 30 seconds for key to activate
- Restart Flask

**Error: "Still getting 429"**
- Make sure you restarted Flask
- Make sure .env file is saved
- Try a paid key instead

---

## ✅ Checklist

- [ ] Go to Google AI Studio and create new key
- [ ] Copy the new key
- [ ] Open `.env` file in VS Code
- [ ] Find `GEMINI_API_KEY=` line
- [ ] Replace with new key
- [ ] Save file (Ctrl+S)
- [ ] Stop Flask (Ctrl+C)
- [ ] Start Flask (`python back.py`)
- [ ] Test upload at http://localhost:5000

---

**Estimated Time:** 5-15 minutes
**Difficulty:** ⭐ Easy
**Status:** 🔴 ACTION REQUIRED

