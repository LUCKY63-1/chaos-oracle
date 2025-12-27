# 🚢 DEPLOYMENT GUIDE - Chaos Oracle

## 🎯 Deploy Before: Dec 2, 2025 1:29 AM GMT+5:30

---

## Option 1: Vercel (Frontend) + Railway (Backend) - RECOMMENDED

### Frontend on Vercel (5 minutes)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Chaos Oracle - Complete"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy to Vercel**
   - Go to https://vercel.com
   - Click "New Project"
   - Import your GitHub repo
   - Set root directory: `frontend`
   - Click "Deploy"
   - Done! ✅

### Backend on Railway (10 minutes)

1. **Create `railway.json`** (already in project root)

2. **Deploy to Railway**
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repo
   - Add environment variables:
     - `GROQ_API_KEY`
     - `TAVILY_API_KEY`
   - Railway will auto-detect and deploy
   - Get your backend URL (e.g., `https://your-app.railway.app`)

3. **Update Frontend WebSocket URL**
   - In `frontend/lib/websocket.ts`, change:
   ```typescript
   constructor(url: string = 'wss://your-app.railway.app/ws')
   ```
   - Redeploy frontend on Vercel

---

## Option 2: Render (Full Stack) - FREE TIER

### Backend on Render

1. **Create `render.yaml`** (already in project root)

2. **Deploy**
   - Go to https://render.com
   - Click "New +"
   - Select "Web Service"
   - Connect GitHub repo
   - Settings:
     - Build Command: `pip install -r backend_requirements.txt && pip install crewai[litellm,tools] tavily-python`
     - Start Command: `python backend_server.py`
   - Add environment variables
   - Deploy

### Frontend on Render

1. **Deploy**
   - Click "New +"
   - Select "Static Site"
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Publish Directory: `frontend/.next`
   - Update WebSocket URL to your backend URL

---

## Option 3: Docker (Self-Hosted)

### Create Dockerfile for Backend

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend_requirements.txt .
RUN pip install -r backend_requirements.txt
RUN pip install crewai[litellm,tools] tavily-python

COPY . .

CMD ["python", "backend_server.py"]
```

### Create Dockerfile for Frontend

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

CMD ["npm", "start"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8000:8000"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - TAVILY_API_KEY=${TAVILY_API_KEY}

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

---

## 🔐 Environment Variables

### Required for Backend
```env
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

### Optional
```env
PORT=8000
HOST=0.0.0.0
```

---

## 📝 Pre-Deployment Checklist

### Code
- [ ] All files committed to Git
- [ ] `.env` in `.gitignore`
- [ ] No hardcoded API keys
- [ ] WebSocket URL configurable
- [ ] Error handling in place

### Testing
- [ ] Backend starts without errors
- [ ] Frontend builds successfully (`npm run build`)
- [ ] WebSocket connects
- [ ] All personas respond
- [ ] Mobile responsive

### Documentation
- [ ] README.md complete
- [ ] QUICKSTART.md clear
- [ ] Environment variables documented
- [ ] API endpoints documented

---

## 🎬 Post-Deployment

### Test Production
1. Visit your deployed frontend URL
2. Check WebSocket connection (green dot)
3. Send a test message
4. Verify all personas respond
5. Test on mobile device

### Monitor
- Check backend logs for errors
- Monitor API usage (OpenRouter/Tavily)
- Watch for WebSocket disconnections

### Share
- [ ] Demo video recorded
- [ ] Screenshots taken
- [ ] GitHub repo public
- [ ] README has live demo link

---

## 🚨 Common Deployment Issues

### WebSocket Connection Failed
**Problem**: Frontend can't connect to backend
**Solution**: 
- Use `wss://` (not `ws://`) for HTTPS
- Check CORS settings in `backend_server.py`
- Verify backend URL is correct

### Build Fails
**Problem**: `npm run build` fails
**Solution**:
- Run `npm install` first
- Check Node.js version (18+)
- Clear `.next` cache

### API Rate Limits
**Problem**: Too many requests to OpenRouter
**Solution**:
- Add rate limiting in backend
- Cache responses
- Use different API key

---

## 🎉 You're Live!

**Share your deployment**:
- Frontend URL: `https://your-app.vercel.app`
- Backend URL: `https://your-app.railway.app`
- GitHub Repo: `https://github.com/your-username/chaos-oracle`

**Demo Script**:
1. "This is Chaos Oracle - 7 AI personas predict your fate"
2. Ask: "Will I be successful?"
3. Show each persona responding in real-time
4. Highlight the beautiful UI and animations
5. Show mobile responsiveness

**Good luck with your deadline! 🔮**
