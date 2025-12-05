# 🔑 How to Get a New Gemini API Key

## Problem

Your current API key has exhausted its daily quota (1,500 requests/day for free tier).

**Solutions:**

1. **Option A: Create a NEW free API key** (fastest - 5 minutes)
2. **Option B: Upgrade to Paid Plan** (recommended - 15 minutes)
3. **Option C: Use a Different AI Service** (alternative - 20 minutes)

---

## ✅ Option A: Create a NEW Free API Key (Fastest)

### Step 1: Go to Google AI Studio

```
https://makersuite.google.com/app/apikey
```

### Step 2: Sign In

- Use your Google account
- If you don't have one, create a free account

### Step 3: Create New Key

1. Click **"Create API Key"** button (usually on the left side)
2. Select **"Create API key in new project"**
3. A new key will be generated
4. Copy the key to clipboard

### Step 4: Add Key to .env File

**File:** `C:\Users\admin\Visiting_card_reader\.env`

**Replace this line:**

```bash
GEMINI_API_KEY=AIzaSyCRqqHVz4V4OCS6TrYMhKgzkmyXzUTYF-4
```

**With your new key:**

```bash
GEMINI_API_KEY=your_new_key_here_paste_without_quotes
```

### Step 5: Save and Restart

1. Save the `.env` file
2. In PowerShell, press **CTRL+C** to stop Flask
3. Run Flask again:
   ```powershell
   python back.py
   ```

### Step 6: Test

- Go to http://localhost:5000
- Try uploading a card

**Pros:**

- ✅ Free
- ✅ Quick (5 minutes)
- ✅ Works immediately

**Cons:**

- ❌ Same 1,500/day limit
- ❌ Will hit limit again in a few days if heavy usage

---

## 💳 Option B: Upgrade to Paid Plan (RECOMMENDED)

### Why Upgrade?

- **30x higher quota** (60 → 1,500 requests/minute)
- **Cheaper than you think** (~$0.001 per card)
- **$300 free credits** first month
- **Better for production**

### Step 1: Go to Google Cloud Console

```
https://console.cloud.google.com/
```

### Step 2: Create/Select Project

1. If first time, create a new project
   - Click **Select a project** → **New Project**
   - Name it: `visiting-card-reader`
   - Click **Create**
2. If you already have a project, select it

### Step 3: Enable Billing

1. Go to **Billing** (left menu)
2. Click **Link Billing Account**
3. If you don't have a billing account:
   - Click **Create Billing Account**
   - Add your payment method (credit/debit card)
   - You won't be charged for free credits ($300)
4. Select your billing account
5. Link it to your project

### Step 4: Enable Generative Language API

1. Go to **API & Services** → **Library**
2. Search: `generative language`
3. Click **Generative Language API**
4. Click **Enable**

### Step 5: Create API Key

1. Go to **API & Services** → **Credentials**
2. Click **Create Credentials** → **API Key**
3. Copy your new API key

### Step 6: Update .env File

Replace the old key in `.env`:

```bash
GEMINI_API_KEY=your_new_paid_tier_key_here
```

### Step 7: Restart Application

```powershell
# Stop Flask (press CTRL+C)
# Then restart
python back.py
```

### Step 8: Test

- Upload card images
- Should work without rate limit errors

**Benefits:**

- ✅ 30x higher quota
- ✅ $300 free credits
- ✅ ~$0.001 per card
- ✅ Much faster

**Timeline:**

- 10-15 minutes to set up
- New quotas apply immediately

---

## 🤔 Option C: Use Different AI Service

### If You Want to Switch to Claude (Anthropic)

1. Go to https://console.anthropic.com/
2. Create account
3. Get API key
4. Install Claude library: `pip install anthropic`
5. Update `back.py` to use Claude instead

**Pricing:**

- Free tier: ~200K free tokens/month
- Paid: $0.003/input, $0.015/output

---

## 📊 Quota Comparison

| Service       | Free Quota               | Cost              | Speed     |
| ------------- | ------------------------ | ----------------- | --------- |
| Gemini (Free) | 60 req/min, 1,500/day    | $0                | Good      |
| Gemini (Paid) | 1,500 req/min, unlimited | $0.001/card       | Excellent |
| Claude (Free) | 200K tokens/month        | $0                | Good      |
| OpenAI GPT-4V | 500 req/day              | $0.01 per request | Excellent |

---

## ⚠️ Before Switching Keys

### Save Your Current Key (Optional)

Keep the old key somewhere safe in case you want to revert:

```bash
Old Key: AIzaSyCRqqHVz4V4OCS6TrYMhKgzkmyXzUTYF-4
```

### Check Current Usage

1. Go to Google Cloud Console
2. **API & Services** → **Quotas**
3. Search for **Generative Language**
4. Check **Requests per minute** and **Requests per day** usage

---

## 🚀 Quick Start (Just Get a New Key)

### 1 minute version:

```bash
# Step 1: Go to https://makersuite.google.com/app/apikey
# Step 2: Click "Create API Key"
# Step 3: Copy new key
# Step 4: Edit .env file, replace GEMINI_API_KEY value
# Step 5: Save file
# Step 6: Restart Flask (Ctrl+C, then python back.py)
# Step 7: Try uploading a card
```

---

## 🔧 If You're Getting Errors

### Error: "Invalid API Key"

- Check that key is copied correctly (no extra spaces)
- Wait 30 seconds for key to activate
- Restart Flask

### Error: "Still getting 429"

- Key might be from same project with same quota
- Try upgrading to paid plan (Option B)
- Or create key on different Google account

### Error: "API key not found"

- Make sure `.env` file has: `GEMINI_API_KEY=your_key`
- No quotes needed
- Save the file
- Restart Flask

---

## 📝 Step-by-Step for Paid Upgrade (Detailed)

### 1. Go to Google Cloud Console

```
https://console.cloud.google.com/
```

### 2. Create New Project

- Click **Select a Project** dropdown
- Click **New Project**
- Name: `visiting-card-reader`
- Click **Create**
- Wait 30 seconds

### 3. Enable Billing

- Left menu → **Billing**
- Click **Link Billing Account**
- **Create Billing Account** (if new)
- Add credit card
- Accept terms
- Click **Link to Project**

### 4. Enable API

- Left menu → **API & Services** → **Library**
- Search: `generative language`
- Click the result
- Click **Enable**

### 5. Create API Key

- Left menu → **API & Services** → **Credentials**
- Click **Create Credentials** → **API Key**
- Copy key (icon next to key)

### 6. Update Application

- Open: `C:\Users\admin\Visiting_card_reader\.env`
- Find: `GEMINI_API_KEY=`
- Replace with your new key:
  ```
  GEMINI_API_KEY=AIza...your...new...key...here
  ```
- Save file (Ctrl+S)

### 7. Restart Flask

```powershell
# In PowerShell, press CTRL+C (stops current Flask)
python back.py
```

### 8. Test Upload

- Go to http://localhost:5000
- Login
- Upload a card
- Should work! ✅

---

## ✅ Verification

### How to Know It's Working:

1. Check console output (where Flask is running):

   ```
   Extracting card... (should NOT show 429 error)
   ```

2. Check response:

   ```
   Card details extracted and saved! ✅
   ```

3. Card appears in "All Cards" list

---

## 💡 My Recommendation

**Use Option B (Paid Upgrade):**

- ✅ Only takes 15 minutes
- ✅ $300 free credits
- ✅ Will cost ~$0.001 per card
- ✅ No more rate limit issues
- ✅ Great for production use
- ✅ Can disable billing later if needed

**Next Best Option:** Option A (New Free Key)

- Quick temporary fix
- Will hit limit again
- Good for testing

---

## 📞 Need Help?

### If Key Still Doesn't Work:

1. **Verify key format:**

   - Should start with: `AIza...`
   - Should be 39+ characters long
   - No quotes in `.env`

2. **Check .env file:**

   ```bash
   # Correct format:
   GEMINI_API_KEY=AIzaSyCR...your...key...here

   # Wrong formats:
   GEMINI_API_KEY="AIzaSyCR..."  # ❌ Has quotes
   GEMINI_API_KEY = AIzaSyCR...  # ❌ Has spaces
   ```

3. **Restart Flask:**

   - Press **CTRL+C**
   - Run: `python back.py`

4. **Wait 30 seconds:**
   - New keys sometimes take time to activate

---

**Status:** 🟡 Action Required - Need to get new API key

**Next Step:** Choose Option A (Quick) or Option B (Recommended) and follow the steps above.
