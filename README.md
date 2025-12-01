# 🔮 Chaos Oracle Cult - 6 Deadly Personas

A real-time AI chat application featuring 7 chaotic AI personas powered by CrewAI, with a modern Next.js frontend and FastAPI WebSocket backend.

## 🎭 The Personas

1. **💀 Doomer** - Eternal pessimist with eerily accurate doom predictions
2. **🔥 Hype Bro** - Pure motivational energy and alpha mindset
3. **😈 Roast Master** - Brutal roasts and uncomfortable truths
4. **📊 Fact-Checker** - Cursed statistics and questionable correlations
5. **👹 The Gremlin** - Chaotic glitch in the matrix
6. **🔮 Prophet** - Mystical orchestrator of the final verdict

## 🚀 Quick Start

### Prerequisites

- Python 3.10-3.13
- Node.js 18+ and npm
- API Keys (OpenRouter, Tavily)

### 1. Backend Setup

```bash
# Install Python dependencies
pip install -r backend_requirements.txt

# Install CrewAI dependencies
pip install uv
crewai install

# Set up environment variables
# Create .env file with:
# OPENROUTER_API_KEY=your_key_here
# TAVILY_API_KEY=your_key_here
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 3. Start the WebSocket Server

```bash
# From project root
python backend_server.py
```

The server will start on `http://localhost:8000`

### 4. Access the Application

Open your browser to `http://localhost:3000`

## 📁 Project Structure

```
chaos_oracle___7_deadly_personas_v2_crewai-project/
├── src/chaos_oracle___7_deadly_personas/
│   ├── config/
│   │   ├── agents.yaml          # Agent configurations
│   │   └── tasks.yaml           # Task definitions
│   ├── crew.py                  # CrewAI crew setup
│   ├── app.py                   # Streamlit app (legacy)
│   └── main.py                  # CLI entry point
├── frontend/
│   ├── app/
│   │   ├── page.tsx            # Main chat interface
│   │   ├── layout.tsx          # Root layout
│   │   └── globals.css         # Global styles
│   ├── components/
│   │   ├── MessageBubble.tsx   # Message display
│   │   ├── TypingIndicator.tsx # Typing animation
│   │   └── Sidebar.tsx         # Persona sidebar
│   └── lib/
│       ├── websocket.ts        # WebSocket client
│       ├── personas.ts         # Persona configs
│       └── types.ts            # TypeScript types
├── backend_server.py           # FastAPI WebSocket server
└── backend_requirements.txt    # Backend dependencies
```

## 🎨 Features

- ✨ **Real-time WebSocket Communication** - Instant message streaming
- 🎭 **6 Unique AI Personas** - Each with distinct personality and styling
- 📱 **Responsive Design** - Works on desktop and mobile
- 🎨 **Custom Styling** - Persona-specific colors and emojis
- ⚡ **Fast & Modern** - Built with Next.js 15 and React 19
- 🔄 **Auto-reconnect** - Handles connection drops gracefully
- 💬 **WhatsApp-style Chat** - Familiar and intuitive interface

## 🛠️ Technology Stack

### Frontend
- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **WebSocket API** - Real-time communication

### Backend
- **CrewAI** - Multi-agent orchestration
- **FastAPI** - High-performance Python web framework
- **Uvicorn** - ASGI server
- **OpenRouter** - LLM API access (Grok 4.1)
- **Tavily** - Web search for Fact-Checker

## 🔧 Configuration

### Agent Configuration

Edit `src/chaos_oracle___7_deadly_personas/config/agents.yaml` to modify agent personalities, goals, and backstories.

### Task Configuration

Edit `src/chaos_oracle___7_deadly_personas/config/tasks.yaml` to modify agent tasks and expected outputs.

### Frontend Styling

Edit `frontend/lib/personas.ts` to customize colors, emojis, and confidence ranges.

## 🚢 Deployment

### Frontend (Vercel)

```bash
cd frontend
vercel deploy
```

### Backend (Railway/Render)

1. Create a new service
2. Connect your repository
3. Set build command: `pip install -r backend_requirements.txt && crewai install`
4. Set start command: `python backend_server.py`
5. Add environment variables

## 📝 API Endpoints

### WebSocket
- `ws://localhost:8000/ws` - Main WebSocket endpoint

### HTTP
- `GET /` - Server status
- `GET /health` - Health check with connection count

## 🎯 Usage

1. Open the application in your browser
2. Type your question in the input field
3. Watch as each persona responds in sequence
4. The Prophet delivers the final verdict
5. Clear chat or ask another question

## 🐛 Troubleshooting

### WebSocket Connection Failed
- Ensure backend server is running on port 8000
- Check firewall settings
- Verify CORS settings in `backend_server.py`

### Frontend Not Loading
- Run `npm install` in frontend directory
- Clear `.next` cache: `rm -rf .next`
- Check Node.js version (18+)

### Agents Not Responding
- Verify API keys in `.env` file
- Check OpenRouter API quota
- Review backend server logs

## 📄 License

MIT License - Feel free to use for your projects!

## 🙏 Credits

Built with:
- [CrewAI](https://crewai.com) - Multi-agent framework
- [Next.js](https://nextjs.org) - React framework
- [FastAPI](https://fastapi.tiangolo.com) - Python web framework
- [OpenRouter](https://openrouter.ai) - LLM API access

---

**Deadline**: December 2, 2025 1:29 AM GMT+5:30 ⏰

Made with 🔮 and chaos
