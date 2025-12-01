# 🔮 Chaos Oracle: 6 Deadly Personas

> **A real-time multi-agent divination system that synthesizes diverse AI perspectives into mystical prophecies**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)

---

## 🌟 Overview

Chaos Oracle is an innovative AI-powered divination system that combines **6 distinct AI personas** to provide multi-faceted guidance on life's questions. Unlike traditional AI assistants that deliver uniform responses, Chaos Oracle creates a dynamic conversation between specialized agents—each with unique personalities, tools, and perspectives.

### ✨ Key Features

- 🎭 **6 Unique AI Personas** - From pessimistic Doomer to mystical Prophet
- ⚡ **Real-time Streaming** - Watch agents respond live via WebSocket
- 🎨 **Beautiful UI** - Modern, responsive chat interface with dark/light themes
- 🔧 **Specialized Tools** - Web search, fact-checking, and more
- 🚀 **Production Ready** - Deployed with comprehensive observability
- 📱 **Mobile Friendly** - Fully responsive design

---

## 🎭 Meet the Personas

| Persona | Role | Specialty |
|---------|------|-----------|
| 🌑 **Doomer** | Pessimistic Realist | Worst-case scenarios with high accuracy |
| 🔥 **Hype Bro** | Motivational Coach | Manifestation mindset and positive energy |
| 💀 **Roast Master** | Brutal Critic | Constructive criticism without mercy |
| 📊 **Fact-Checker** | Data Analyst | Evidence-based insights with web search |
| 👹 **The Gremlin** | Chaos Agent | Random disruptions and unexpected wisdom |
| 🔮 **Prophet** | Mystical Synthesizer | Final verdict combining all perspectives |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **npm or yarn**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LUCKY63-1/Chaos-Oracle.git
   cd Chaos-Oracle
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys:
   # - OPENROUTER_API_KEY (get from https://openrouter.ai/keys)
   # - TAVILY_API_KEY (get from https://tavily.com)
   ```

3. **Install backend dependencies**
   ```bash
   pip install -r backend_requirements.txt
   ```

4. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### Running Locally

#### Option 1: Use Batch Scripts (Windows)
```bash
# Start both backend and frontend
start_all.bat

# Or start separately:
start_backend.bat  # Terminal 1
start_frontend.bat # Terminal 2
```

#### Option 2: Manual Start
```bash
# Terminal 1 - Backend
python backend_server.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Health Check**: http://localhost:8000/health

---

## 🏗️ Architecture

### Tech Stack

**Backend:**
- **FastAPI** - High-performance Python web framework
- **CrewAI** - Multi-agent orchestration framework
- **WebSocket** - Real-time bidirectional communication
- **OpenRouter** - LLM API gateway (Grok-4.1 models)
- **Tavily** - Web search API for fact-checking

**Frontend:**
- **Next.js 16** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first styling
- **Lucide React** - Modern icon library
- **WebSocket Client** - Real-time updates

### System Flow

```
User Question → WebSocket → Backend Orchestrator
                                    ↓
                          Sequential Agent Processing
                                    ↓
        Doomer → Hype Bro → Roast Master → Fact-Checker → Gremlin → Prophet
                                    ↓
                    Real-time Streaming to Frontend
                                    ↓
                          Chat Interface Display
```

---

## 📖 Usage

1. **Start the application** (see Quick Start above)
2. **Navigate to** http://localhost:3000
3. **Click "Begin Prophecy"** to start a new session
4. **Enter your question** (e.g., "Should I quit my job?")
5. **Watch the magic happen** - Each persona responds in real-time
6. **Receive the prophecy** - Prophet synthesizes all perspectives

### Example Questions

- "Will I be successful in my new business venture?"
- "Should I move to a new city?"
- "Is now the right time to invest in crypto?"
- "Will I find love this year?"

---

## 🎨 Features in Detail

### Real-time Streaming
- Live agent responses via WebSocket
- Typing indicators for each persona
- Smooth animations and transitions

### Intelligent Personas
- Each agent has unique personality traits
- Specialized tools (web search for Fact-Checker)
- Sequential processing builds on previous responses

### User Experience
- Dark/light theme with smooth transitions
- Mobile-responsive design
- Connection status indicators
- Clear chat functionality
- Vintage typewriter animations

### Observability
- Comprehensive logging system
- Performance metrics tracking
- Health check endpoints
- Error handling and recovery

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
OPENROUTER_API_KEY=your_openrouter_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

# Optional
PORT=8000
FRONTEND_URL=http://localhost:3000
LOG_LEVEL=INFO
```

### Agent Configuration

Agents are configured in `src/chaos_oracle___7_deadly_personas/config/agents.yaml`. You can customize:
- Agent personalities
- Response styles
- Tool assignments
- Processing order

---

## 📦 Deployment

### Railway (Recommended)

1. **Connect your GitHub repository** to Railway
2. **Set environment variables** in Railway dashboard
3. **Deploy** - Railway auto-detects configuration from `railway.json`

### Render

1. **Create new Web Service** from GitHub repo
2. **Configure build command**: `pip install -r backend_requirements.txt`
3. **Configure start command**: `python backend_server.py`
4. **Set environment variables**

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

---

## 🧪 Testing

### Health Check
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "active_connections": 0,
  "uptime_seconds": 123.45
}
```

### WebSocket Test
Open browser console at http://localhost:3000 and check for:
- ✅ WebSocket connection established
- ✅ No connection errors
- ✅ Messages flowing bidirectionally

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **CrewAI** - For the excellent multi-agent framework
- **OpenRouter** - For LLM API access
- **Tavily** - For web search capabilities
- **FastAPI** - For the amazing Python web framework
- **Next.js** - For the powerful React framework

---

## 📧 Contact

**Project Link**: [https://github.com/LUCKY63-1/Chaos-Oracle](https://github.com/LUCKY63-1/Chaos-Oracle)

---

## 🔮 Future Enhancements

- [ ] Long-term memory for conversation context
- [ ] Agent evaluation framework
- [ ] Multi-language support
- [ ] Voice integration (speech-to-text/text-to-speech)
- [ ] Plugin architecture for custom agents
- [ ] Advanced analytics dashboard
- [ ] Federated deployment across cloud providers
- [ ] Ethical AI framework with content moderation

---

<div align="center">

**Made with 🔮 and ❤️**

*Ask the Oracle. Embrace the Chaos.*

</div>
