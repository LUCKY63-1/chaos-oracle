# 🚀 QUICK START GUIDE - Chaos Oracle

## ⏰ You have until Dec 2, 2025 1:29 AM GMT+5:30

## 🎯 3-Step Launch (5 minutes)

### Step 1: Install Backend Dependencies (1 min)
```bash
pip install fastapi uvicorn[standard] websockets python-multipart
```

### Step 2: Start Backend Server (30 seconds)
```bash
python backend_server.py
```
✅ Server runs on: `http://localhost:8000`

### Step 3: Start Frontend (2 minutes)
```bash
cd frontend
npm install
npm run dev
```
✅ Frontend runs on: `http://localhost:3000`

---

## 🎬 EVEN FASTER - Use Batch Scripts (Windows)

### Option A: Start Everything at Once
```bash
start_all.bat
```

### Option B: Start Separately
```bash
# Terminal 1
start_backend.bat

# Terminal 2
start_frontend.bat
```

---

## ✅ Verify Everything Works

1. **Backend Health Check**
   - Open: `http://localhost:8000/health`
   - Should see: `{"status": "healthy", "active_connections": 0, ...}`

2. **Frontend**
   - Open: `http://localhost:3000`
   - Should see: Chaos Oracle chat interface

3. **Test a Message**
   - Type: "Will I be rich?"
   - Watch all 6 personas respond!

---

## 🔑 Environment Variables

Create `.env` file in project root:
```env
OPENROUTER_API_KEY=your_openrouter_key_here
TAVILY_API_KEY=your_tavily_key_here
```

Get keys from:
- OpenRouter: https://openrouter.ai/keys
- Tavily: https://tavily.com

---

## 🐛 Quick Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Kill process if needed
taskkill /PID <process_id> /F
```

### Frontend won't start
```bash
# Clear cache and reinstall
cd frontend
rm -rf .next node_modules
npm install
npm run dev
```

### WebSocket won't connect
- Make sure backend is running first
- Check browser console for errors
- Verify URL is `ws://localhost:8000/ws`

---

## 📊 What You Built

✅ **FastAPI WebSocket Server** - Real-time backend
✅ **Next.js Frontend** - Modern React UI
✅ **6 AI Personas** - CrewAI agents
✅ **Real-time Chat** - WhatsApp-style interface
✅ **Auto-reconnect** - Handles disconnections
✅ **Responsive Design** - Works on all devices

---

## 🚢 Ready to Ship?

### Test Checklist
- [ ] Backend starts without errors
- [ ] Frontend loads at localhost:3000
- [ ] WebSocket connects (green dot in header)
- [ ] Can send a message
- [ ] All 6 personas respond
- [ ] Prophet gives final verdict
- [ ] Clear chat works
- [ ] Mobile responsive (test in DevTools)

### Deploy Checklist
- [ ] Environment variables set
- [ ] API keys valid
- [ ] README updated
- [ ] Screenshots taken
- [ ] Demo video recorded
- [ ] GitHub repo created

---

## 🎉 You're Ready!

**Time to deadline**: Check your clock!

**What to demo**:
1. Show the beautiful UI
2. Ask a question
3. Watch personas respond in real-time
4. Show the typing indicators
5. Highlight the Prophet's final verdict

**Good luck! 🔮**
