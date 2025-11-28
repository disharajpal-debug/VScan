# 429 Error - API Rate Limiting Guide

## What Happened?

You received a **429 Too Many Requests** error. This means the Gemini API has rate-limited your requests because you've exceeded the free tier quota.

---

## ✅ What I Fixed

Your application now has **automatic retry logic with exponential backoff**:

1. **Automatic Retries**: If rate-limited, the app waits and retries automatically
   - First retry: waits 2 seconds
   - Second retry: waits 4 seconds
   - Third retry: waits 8 seconds

2. **Better Error Messages**: Users see helpful messages like:
   - ⏳ "API rate limit reached. Please wait a few minutes and try again."
   - ❌ "The extraction service is temporarily unavailable"

3. **Proper Status Codes**: Errors return correct HTTP status codes (429, 503)

---

## 📊 Gemini API Rate Limits

**Free Tier Limits:**
- **Requests per minute**: 60 RPM
- **Requests per day**: 1,500 RPD
- **Tokens per minute**: 1,000,000 TPM

**If you exceed these, you'll get 429 errors**

---

## 💡 How to Avoid Rate Limiting

### Option 1: **Wait (Free & Easiest)**
- Wait 1-2 minutes between card uploads
- The app now retries automatically
- No configuration needed

### Option 2: **Upgrade to Paid Plan**
- Go to Google AI Studio: https://makersuite.google.com/app/apikey
- Enable billing on your Google Cloud account
- Higher limits:
  - **1,500 RPM** (up from 60)
  - **10,000,000 TPM** (up from 1,000,000)

### Option 3: **Use a Different AI Service**
- Claude (Anthropic)
- OpenAI (GPT-4 Vision)
- Azure Computer Vision

---

## 🔧 Configuration Options

### Current Setup (in `.env`):
```bash
GEMINI_MODEL=gemini-2.0-flash
GEMINI_API_KEY=your_key_here
```

### To Use a Different Free API:

#### **Option A: Use Claude API (Anthropic)**

1. Get API key: https://console.anthropic.com/
2. Install: `pip install anthropic`
3. Update your code to use Claude

#### **Option B: Use OpenAI Vision**

1. Get API key: https://platform.openai.com/api-keys
2. Install: `pip install openai`
3. Update your code to use GPT-4 Vision

---

## 📝 Recommended Actions

### Immediate (Do Now):
1. ✅ Your app already has automatic retries - **no action needed**
2. Wait 2-3 minutes and try uploading again
3. The automatic retry will work if API is temporarily limited

### Short Term (Next 30 minutes):
- Upgrade to Gemini API paid tier if uploading many cards
- Or space out uploads over time

### Long Term (This week):
- Monitor usage in Google Cloud Console: https://console.cloud.google.com/
- Set up billing alerts to know when approaching limits
- Consider batching uploads or using a queuing system

---

## 📈 Monitor Your Usage

### Check Your Quota:

1. Go to: https://console.cloud.google.com/
2. Select your project
3. Go to **API & Services** → **Quotas**
4. Search for "Generative Language"
5. View **Requests per minute** and **Requests per day**

---

## 🚀 To Try Again

### After Waiting 2-3 Minutes:

1. Go to: http://localhost:5000
2. Upload another card image
3. The app will:
   - Try the extraction
   - If rate-limited (429), automatically retry
   - Show a message about waiting

### If Still Rate-Limited:

**Option 1: Upgrade API Plan**
- Go to Google Cloud Console
- Enable billing
- Wait 10-15 minutes for limits to increase
- Try again

**Option 2: Use Different Service**
- Switch to Claude or OpenAI (requires code changes)
- Each has their own free quota

**Option 3: Wait Until Tomorrow**
- Daily limit (1,500 RPD) resets at midnight UTC
- You'll have 1,500 new requests then

---

## 🔄 How Automatic Retry Works

**When you upload a card now:**

```
1. Send request to Gemini API
   ↓
2. Get 429 error (rate limited)
   ↓
3. Wait 2 seconds
   ↓
4. Retry request
   ↓
5. Get 429 error again
   ↓
6. Wait 4 seconds
   ↓
7. Retry request
   ↓
8. Get 429 error again
   ↓
9. Wait 8 seconds
   ↓
10. Final retry
    ↓
11. If still failing: Show error "Please try again later"
    If succeeds: Extract card details!
```

---

## 📞 Support

### Error Messages You Might See:

| Message | Meaning | Solution |
|---------|---------|----------|
| ⏳ "Rate limit reached" | Too many requests | Wait 2-3 min, retry |
| ❌ "Service unavailable" | API down temporarily | Try again in 5 min |
| 🔄 "Failed after 3 retries" | Persistent issue | Upgrade plan or wait |
| ❌ "Network error" | Connection issue | Check internet |

---

## 💰 Pricing Information

**Gemini API - Free Tier:**
- 60 requests per minute
- 1,500 requests per day
- Cost: **$0/month**

**Gemini API - Paid Plan:**
- $0.075 per 1000 input tokens
- $0.30 per 1000 output tokens
- Cost: ~$0.001 per card (estimate)
- Start with **$300/month free credit**

**Compare to:**
- Claude: $0.003 input / $0.015 output (per 1K tokens)
- OpenAI GPT-4V: $0.01 input / $0.03 output (per 1K tokens)

---

## ✅ Verification

To confirm the retry logic is working:

1. Check the terminal where Flask is running
2. You should see messages like:
   ```
   Rate limited (429). Retrying in 2 seconds... (Attempt 1/3)
   Rate limited (429). Retrying in 4 seconds... (Attempt 2/3)
   ```
3. This means automatic retry is active

---

**Last Updated:** November 24, 2025
**Status:** ✅ Retry Logic Implemented

