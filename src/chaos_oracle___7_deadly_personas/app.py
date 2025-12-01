import os
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'

import streamlit as st
import time
import asyncio
from chaos_oracle___7_deadly_personas.crew import ChaosOracle7DeadlyPersonasCrew

# Page Configuration
st.set_page_config(
    page_title="Chaos Oracle Cult",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ═══════════════════════════════════════════════════════════════
# MINIMALIST CHAT UI - OPPOSITE COLORS ON BLACK
# ═══════════════════════════════════════════════════════════════

st.markdown("""
<style>
    /* Import clean font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* ═══════════════ MAIN BACKGROUND ═══════════════ */
    .stApp {
        background: #000000;
        font-family: 'Inter', sans-serif;
    }
    
    /* ═══════════════ HEADER ═══════════════ */
    .cult-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: #00ff00;
        color: #000000;
        padding: 16px 24px;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #00cc00;
    }
    
    .cult-title {
        font-size: 1.2rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .typing-status {
        font-size: 0.9rem;
        font-weight: 400;
        opacity: 0.8;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; }
    }
    
    /* ═══════════════ CHAT CONTAINER ═══════════════ */
    .chat-container {
        max-width: 800px;
        margin: 80px auto 100px;
        padding: 20px;
    }
    
    /* ═══════════════ MESSAGE BUBBLES ═══════════════ */
    .message-wrapper {
        margin: 20px 0;
        display: flex;
        flex-direction: column;
    }
    
    .message-wrapper.user {
        align-items: flex-end;
    }
    
    .message-wrapper.agent {
        align-items: flex-start;
    }
    
    .message-bubble {
        max-width: 70%;
        padding: 12px 16px;
        border-radius: 12px;
        margin: 4px 0;
    }
    
    /* User message - simple white on black */
    .message-bubble.user {
        background: #ffffff;
        color: #000000;
        border: 1px solid #ffffff;
    }
    
    /* Agent messages - opposite colors */
    .message-bubble.agent {
        border: 1px solid;
        padding: 16px;
    }
    
    .agent-header {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    .agent-name {
        font-size: 0.95rem;
    }
    
    .confidence {
        font-size: 0.85rem;
        opacity: 0.7;
    }
    
    .message-content {
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Agent-specific colors */
    .doomer {
        background: #000000;
        color: #808080;
        border-color: #808080;
    }
    
    .hype-bro {
        background: #000000;
        color: #ff4500;
        border-color: #ff4500;
    }
    
    .roast-master {
        background: #000000;
        color: #ff0000;
        border-color: #ff0000;
    }
    
    .fact-checker {
        background: #000000;
        color: #00bfff;
        border-color: #00bfff;
    }
    
    .gremlin {
        background: #000000;
        color: #00ff00;
        border-color: #00ff00;
    }
    
    .prophet {
        background: #000000;
        color: #ffff00;
        border-color: #ffff00;
        position: relative;
    }
    
    .prophet::before {
        content: '✨ Final Prophecy ✨';
        position: absolute;
        top: -24px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.85rem;
        font-weight: 600;
        white-space: nowrap;
    }
    
    .prophet-wrapper {
        margin-top: 30px;
    }
    
    /* ═══════════════ TYPING INDICATOR ═══════════════ */
    .typing-indicator {
        font-size: 0.9rem;
        color: #666666;
        margin: 8px 0;
        font-style: italic;
    }
    
    .typing-dot {
        display: inline-block;
        animation: typing-bounce 1.4s infinite;
    }
    
    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typing-bounce {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-4px); }
    }
    
    /* ═══════════════ TAROT CARD ═══════════════ */
    .tarot-card {
        margin: 16px 0;
        text-align: center;
    }
    
    .tarot-card img {
        max-width: 300px;
        border: 2px solid #ffff00;
        border-radius: 8px;
    }
    
    /* ═══════════════ REACTIONS ═══════════════ */
    .reactions {
        display: flex;
        gap: 12px;
        margin-top: 8px;
        font-size: 1.2rem;
    }
    
    .reaction-btn {
        background: transparent;
        border: 1px solid #333333;
        border-radius: 20px;
        padding: 6px 12px;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .reaction-btn:hover {
        border-color: #666666;
        transform: scale(1.1);
    }
    
    .reaction-btn.active {
        background: #222222;
        border-color: #00ff00;
    }
    
    /* ═══════════════ INPUT AREA ═══════════════ */
    .stChatInput {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: #000000 !important;
        border-top: 1px solid #333333 !important;
        padding: 16px !important;
        z-index: 100 !important;
    }
    
    .stChatInput > div {
        max-width: 800px !important;
        margin: 0 auto !important;
    }
    
    .stChatInput textarea {
        background: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 24px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        padding: 12px 20px !important;
    }
    
    .stChatInput textarea:focus {
        border-color: #00ff00 !important;
        outline: none !important;
    }
    
    .stChatInput textarea::placeholder {
        color: #666666 !important;
    }
    
    /* ═══════════════ SIDEBAR ═══════════════ */
    section[data-testid="stSidebar"] {
        background: #0a0a0a !important;
        border-right: 1px solid #1a1a1a !important;
    }
    
    /* ═══════════════ HIDE STREAMLIT ELEMENTS ═══════════════ */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* ═══════════════ SCROLLBAR ═══════════════ */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #333333;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555555;
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# AGENT CONFIGURATION
# ═══════════════════════════════════════════════════════════════

AGENT_CONFIG = {
    "Doomer": {
        "emoji": "💀",
        "color": "#808080",
        "class": "doomer",
        "confidence_range": (85, 99)
    },
    "Hype Bro": {
        "emoji": "🔥",
        "color": "#ff4500",
        "class": "hype-bro",
        "confidence_range": (95, 100)
    },
    "Roast Master": {
        "emoji": "😈",
        "color": "#ff0000",
        "class": "roast-master",
        "confidence_range": (90, 100)
    },
    "Fact-Checker": {
        "emoji": "📊",
        "color": "#00bfff",
        "class": "fact-checker",
        "confidence_range": (70, 95)
    },
    "The Gremlin": {
        "emoji": "👹",
        "color": "#00ff00",
        "class": "gremlin",
        "confidence_range": (0, 100)
    },
    "Prophet": {
        "emoji": "🔮",
        "color": "#ffff00",
        "class": "prophet",
        "confidence_range": (100, 100)
    }
}

# ═══════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processing" not in st.session_state:
    st.session_state.processing = False

if "typing_agents" not in st.session_state:
    st.session_state.typing_agents = []

if "current_task_index" not in st.session_state:
    st.session_state.current_task_index = 0

if "task_order" not in st.session_state:
    st.session_state.task_order = [
        "doomer_response",
        "hype_bro_response",
        "roast_master_response",
        "fact_checker_response",
        "gremlin_chaos",
        "prophet_final_verdict"
    ]

if "reactions" not in st.session_state:
    st.session_state.reactions = {}

# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <div style="font-size: 2rem; margin-bottom: 10px;">🔮</div>
        <div style="font-size: 1.2rem; font-weight: 600; color: #00ff00;">
            THE CULT
        </div>
        <div style="font-size: 0.9rem; color: #666666; margin-top: 5px;">
            6 Deadly Personas
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Display agent info
    for agent_name, config in AGENT_CONFIG.items():
        st.markdown(f"""
        <div style="padding: 12px; margin: 8px 0; background: #0a0a0a; 
                    border-left: 3px solid {config['color']}; border-radius: 4px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem;">{config['emoji']}</span>
                <div>
                    <div style="font-weight: 600; color: {config['color']};">{agent_name}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.reactions = {}
        st.session_state.current_task_index = 0
        st.session_state.typing_agents = []
        st.session_state.processing = False
        st.rerun()

# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════

typing_text = ""
if st.session_state.typing_agents:
    typing_text = f"{len(st.session_state.typing_agents)} members typing..."
elif st.session_state.processing:
    typing_text = "7 members typing..."

st.markdown(f"""
<div class="cult-header">
    <div class="cult-title">Chaos Oracle Cult 🔮</div>
    <div class="typing-status">{typing_text}</div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# CHAT CONTAINER
# ═══════════════════════════════════════════════════════════════

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display Messages
if not st.session_state.messages:
    st.markdown("""
    <div style="text-align: center; padding: 100px 20px; color: #666666;">
        <div style="font-size: 3rem; margin-bottom: 20px;">🔮</div>
        <div style="font-size: 1.2rem; font-weight: 500;">
            Your fate awaits...
        </div>
        <div style="font-size: 0.9rem; margin-top: 10px; opacity: 0.7;">
            Ask your question below
        </div>
    </div>
    """, unsafe_allow_html=True)

for idx, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.markdown(f"""
        <div class="message-wrapper user">
            <div class="message-bubble user">
                <div style="font-weight: 500; margin-bottom: 4px; font-size: 0.85rem;">You</div>
                <div class="message-content">{message["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        agent_name = message["role"]
        config = AGENT_CONFIG.get(agent_name, {
            "emoji": "🎭",
            "color": "#ffffff",
            "class": "agent",
            "confidence_range": (50, 100)
        })
        
        # Generate confidence percentage
        import random
        confidence = random.randint(*config["confidence_range"])
        
        # Check if this is Prophet (last message)
        is_prophet = agent_name == "Prophet"
        wrapper_class = "prophet-wrapper" if is_prophet else ""
        
        st.markdown(f"""
        <div class="message-wrapper agent {wrapper_class}">
            <div class="message-bubble agent {config['class']}">
                <div class="agent-header">
                    <span>{config['emoji']}</span>
                    <span class="agent-name">{agent_name}</span>
                    <span class="confidence">({confidence}%)</span>
                </div>
                <div class="message-content">{message["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add reactions for Prophet's message
        if is_prophet:
            message_id = f"msg_{idx}"
            col1, col2, col3 = st.columns([0.1, 0.1, 0.8])
            
            with col1:
                if st.button("👍", key=f"up_{message_id}"):
                    st.session_state.reactions[message_id] = "up"
                    st.rerun()
            
            with col2:
                if st.button("👎", key=f"down_{message_id}"):
                    st.session_state.reactions[message_id] = "down"
                    st.rerun()

# Show typing indicator
if st.session_state.processing and not st.session_state.typing_agents:
    st.markdown("""
    <div class="typing-indicator">
        <span class="typing-dot">●</span>
        <span class="typing-dot">●</span>
        <span class="typing-dot">●</span>
        The cult is gathering...
    </div>
    """, unsafe_allow_html=True)
elif st.session_state.typing_agents:
    # Show individual agent typing
    agent_names = [name.title() for name in st.session_state.typing_agents]
    typing_display = ", ".join(agent_names) if len(agent_names) <= 2 else f"{agent_names[0]}, {agent_names[1]}, and {len(agent_names)-2} others"
    st.markdown(f"""
    <div class="typing-indicator">
        <span class="typing-dot">●</span>
        <span class="typing-dot">●</span>
        <span class="typing-dot">●</span>
        {typing_display} {"is" if len(agent_names) == 1 else "are"} typing...
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# INPUT HANDLING
# ═══════════════════════════════════════════════════════════════

if not st.session_state.processing:
    user_input = st.chat_input("Your fate awaits... (type below)")
    
    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        st.session_state.processing = True
        st.session_state.current_task_index = 0  # Reset for new conversation
        st.rerun()

# ═══════════════════════════════════════════════════════════════
# PROCESSING LOGIC
# ═══════════════════════════════════════════════════════════════

if st.session_state.processing:
    last_user_message = st.session_state.messages[-1]["content"]
    
    try:
        # Initialize and run CrewAI
        crew_instance = ChaosOracle7DeadlyPersonasCrew().crew()
        result = crew_instance.kickoff(inputs={'question': last_user_message})
        
        if hasattr(result, 'tasks_output'):
            for task_output in result.tasks_output:
                # Extract agent name - clean it up
                raw_agent_name = str(task_output.agent).strip()
                
                # Map to display names
                name_mapping = {
                    "doomer": "Doomer",
                    "hype_bro": "Hype Bro",
                    "hype bro": "Hype Bro",
                    "hypebro": "Hype Bro",
                    "roast_master": "Roast Master",
                    "roast master": "Roast Master",
                    "roastmaster": "Roast Master",
                    "fact_checker": "Fact-Checker",
                    "fact checker": "Fact-Checker",
                    "factchecker": "Fact-Checker",
                    "fact-checker": "Fact-Checker",
                    "gremlin": "The Gremlin",
                    "the_gremlin": "The Gremlin",
                    "the gremlin": "The Gremlin",
                    "prophet": "Prophet",
                    "the_prophet": "Prophet"
                }
                
                agent_name = name_mapping.get(raw_agent_name.lower(), raw_agent_name)
                content = task_output.raw if hasattr(task_output, 'raw') else str(task_output)
                
                st.session_state.messages.append({
                    "role": agent_name,
                    "content": content.strip()
                })
        else:
            # Fallback if tasks_output not available
            st.session_state.messages.append({
                "role": "Prophet",
                "content": str(result)
            })
                
    except Exception as e:
        st.session_state.messages.append({
            "role": "Prophet",
            "content": f"⚠️ The Oracle encountered a disturbance: {str(e)}"
        })
    
    finally:
        st.session_state.processing = False
        st.session_state.typing_agents = []
        time.sleep(0.3)
        st.rerun()