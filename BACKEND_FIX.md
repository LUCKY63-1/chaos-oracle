# 🔧 BACKEND NOT RUNNING - API KEY ISSUE

## ❌ Problem Identified

Your backend server crashed with this error:
```
❌ Error processing crew: No API key environment variable.
```

The backend needs **API keys** to communicate with the AI services.

---

## ✅ SOLUTION: Add Your API Keys

### Step 1: Check Your `.env` File

You need to add your API keys to the `.env` file in the project root.

**Required API Keys:**
1. **OPENROUTER_API_KEY** - For the AI models (Grok 4.1)
2. **TAVILY_API_KEY** - For the Fact-Checker's web search

### Step 2: Get Your API Keys

#### OpenRouter API Key
1. Go to: https://openrouter.ai/keys
2. Sign up or log in
3. Create a new API key
4. Copy the key

#### Tavily API Key
1. Go to: https://tavily.com
2. Sign up or log in
3. Get your API key
4. Copy the key

### Step 3: Update Your `.env` File

Open the `.env` file and make sure it looks like this:

```env
# OpenRouter API Key (required)
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxx

# Tavily API Key (required for Fact-Checker)
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxx

# Server Configuration (optional)
PORT=8000
HOST=0.0.0.0
```

**Replace the `xxxxx` with your actual API keys!**

---

## 🚀 After Adding Keys

### Restart the Backend Server

```bash
# Stop the current server (Ctrl+C in the terminal)
# Then restart:
python backend_server.py
```

Or use the batch script:
```bash
start_backend.bat
```

### Verify It's Working

1. **Check the terminal output** - Should see:
   ```
   🔮 Starting Chaos Oracle WebSocket Server...
   📡 WebSocket endpoint: ws://localhost:8000/ws
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```

2. **Test the health endpoint**:
   - Open: http://localhost:8000/health
   - Should see: `{"status": "healthy", ...}`

3. **Check the frontend**:
   - Open: http://localhost:3000
   - Connection status should show green "Connected"

---

## 🧪 Test Without API Keys (Optional)

If you want to test the UI without setting up API keys yet, you can:

1. **Mock the backend responses** (for UI testing only)
2. **Use the Streamlit version** (has different requirements)
3. **Get free API keys** from OpenRouter (they offer free tier)

---

## 💡 Free API Key Options

### OpenRouter (Free Tier)
- Model: `grok-4.1-fast:free` (already configured)
- No credit card required
- Limited requests per day
- Perfect for testing

### Tavily (Free Tier)
- 1000 searches/month free
- No credit card required
- Enough for testing

---

## 🔍 Troubleshooting

### Backend still not starting?

1. **Check if API keys are valid**
   ```bash
   # In PowerShell
   $env:OPENROUTER_API_KEY
   ```

2. **Check for typos in .env file**
   - No spaces around `=`
   - No quotes around values
   - Keys should start with `sk-or-v1-` (OpenRouter)

3. **Check the terminal for specific errors**
   - Look for error messages
   - Check if it's an API key issue or something else

### Frontend shows "Disconnected"?

This means the backend is not running. Follow the steps above to:
1. Add API keys
2. Restart backend
3. Verify it's running on port 8000

---

## 📝 Quick Checklist

- [ ] Got OpenRouter API key
- [ ] Got Tavily API key
- [ ] Updated `.env` file with both keys
- [ ] Restarted backend server
- [ ] Backend shows "Uvicorn running on http://0.0.0.0:8000"
- [ ] Health endpoint works: http://localhost:8000/health
- [ ] Frontend shows green "Connected" status
- [ ] Ready to test!

---

## 🎯 Next Steps

Once your API keys are added and the backend is running:

1. ✅ Open http://localhost:3000
2. ✅ Type a test message: "Will I be successful?"
3. ✅ Watch all 6 personas respond
4. ✅ Verify the Prophet's final verdict

---

**Need help getting API keys? Let me know!** 🔑
