"""
FastAPI WebSocket Server for Chaos Oracle
TRUE Real-Time Streaming with Observability (Logging, Tracing, Metrics)
"""
import asyncio
import json
import time
import logging
import sys
import io
from typing import Dict, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
import threading

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.chaos_oracle___7_deadly_personas.crew import ChaosOracle7DeadlyPersonasCrew

# ═══════════════════════════════════════════════════════════════
# OBSERVABILITY: Logging Configuration
# ═══════════════════════════════════════════════════════════════

def _setup_logging():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    try:
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    fh = logging.FileHandler('chaos_oracle.log', encoding='utf-8')
    fh.setFormatter(formatter)
    try:
        ch = logging.StreamHandler(sys.stdout)
    except Exception:
        try:
            ch = logging.StreamHandler(io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace'))
        except Exception:
            ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root.addHandler(fh)
    root.addHandler(ch)

_setup_logging()

logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════════════
# OBSERVABILITY: Metrics Tracking
# ═══════════════════════════════════════════════════════════════

class MetricsCollector:
    """Collect and track agent performance metrics"""
    
    def __init__(self):
        self.lock = threading.Lock()
        self.agent_metrics = {}
        self.total_requests = 0
        self.total_responses = 0
        
    def start_agent(self, agent_name: str):
        """Record agent start time"""
        with self.lock:
            if agent_name not in self.agent_metrics:
                self.agent_metrics[agent_name] = {
                    'count': 0,
                    'total_time': 0,
                    'avg_time': 0,
                    'last_execution': None
                }
            
            self.agent_metrics[agent_name]['start_time'] = time.time()
        logger.info(f"📊 METRIC: Agent '{agent_name}' started")
        
    def end_agent(self, agent_name: str):
        """Record agent completion and calculate metrics"""
        with self.lock:
            if agent_name in self.agent_metrics:
                start_time = self.agent_metrics[agent_name].get('start_time')
                if start_time:
                    duration = time.time() - start_time
                    self.agent_metrics[agent_name]['count'] += 1
                    self.agent_metrics[agent_name]['total_time'] += duration
                    self.agent_metrics[agent_name]['avg_time'] = (
                        self.agent_metrics[agent_name]['total_time'] / 
                        self.agent_metrics[agent_name]['count']
                    )
                    self.agent_metrics[agent_name]['last_execution'] = duration
                
                logger.info(f"📊 METRIC: Agent '{agent_name}' completed in {duration:.2f}s")
                logger.info(f"📊 METRIC: Average time for '{agent_name}': {self.agent_metrics[agent_name]['avg_time']:.2f}s")
                
    def get_metrics(self):
        """Get all collected metrics"""
        with self.lock:
            return {
                'total_requests': self.total_requests,
                'total_responses': self.total_responses,
                'agent_metrics': self.agent_metrics.copy()
            }

metrics = MetricsCollector()

# ═══════════════════════════════════════════════════════════════
# FastAPI App Setup
# ═══════════════════════════════════════════════════════════════

app = FastAPI(title="Chaos Oracle WebSocket Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENT_ORDER = [
    "Doomer",
    "Hype Bro", 
    "Roast Master",
    "Fact-Checker",
    "The Gremlin",
    "Prophet"
]

NAME_MAPPING = {
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

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self._lock = threading.Lock()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        with self._lock:
            self.active_connections.append(websocket)
            logger.info(f"✅ Client connected. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        with self._lock:
            if websocket in self.active_connections:
                self.active_connections.remove(websocket)
            logger.info(f"❌ Client disconnected. Total: {len(self.active_connections)}")

    async def send_message(self, message: dict, websocket: WebSocket):
        try:
            await websocket.send_text(json.dumps(message))
            logger.debug(f"📤 Sent message type: {message.get('type')}")
        except Exception as e:
            logger.error(f"Error sending message: {e}")

manager = ConnectionManager()

# ═══════════════════════════════════════════════════════════════
# REAL-TIME STREAMING: Monitor Crew Execution
# ═══════════════════════════════════════════════════════════════

def run_crew_with_monitoring(question: str, response_queue: asyncio.Queue, main_loop):
    """
    Run CrewAI and monitor task completion in REAL-TIME
    Stream each agent's response immediately as it completes
    """
    logger.info(f"🔮 TRACE: Starting crew execution for question: {question[:50]}...")
    with metrics.lock:
        metrics.total_requests += 1
    
    # Use the main event loop passed from the WebSocket endpoint
    loop = main_loop
    
    try:
        crew_instance = ChaosOracle7DeadlyPersonasCrew().crew()

        # Track which tasks have been sent
        sent_tasks = set()

        # Create event for task notification
        task_available_event = threading.Event()

        # Start crew in background thread
        crew_result = [None]  # Use list to allow modification in thread

        def run_crew():
            try:
                logger.info("🔮 TRACE: Crew kickoff started")
                crew_result[0] = crew_instance.kickoff(inputs={'question': question})
                logger.info("🔮 TRACE: Crew kickoff completed")
                # Set event on final completion
                task_available_event.set()
            except Exception as e:
                logger.error(f"❌ ERROR: Crew execution failed: {e}")
                loop.call_soon_threadsafe(response_queue.put_nowait, ('error', None, str(e)))
                # Set event on error completion
                task_available_event.set()

        crew_thread = threading.Thread(target=run_crew, daemon=True)
        crew_thread.start()

        # Monitor crew progress in real-time
        logger.info("👁️ TRACE: Starting real-time monitoring loop")

        while crew_thread.is_alive():
            # Check if crew has task outputs available
            if hasattr(crew_instance, '_tasks') and hasattr(crew_instance, 'tasks'):
                for idx, task in enumerate(crew_instance.tasks):
                    # Check if this task has output and hasn't been sent yet
                    if hasattr(task, 'output') and task.output and idx not in sent_tasks:
                        agent_name = NAME_MAPPING.get(str(task.agent).strip().lower(), str(task.agent))

                        logger.info(f"✅ TRACE: Agent '{agent_name}' completed (task {idx})")
                        metrics.end_agent(agent_name)
                        with metrics.lock:
                            metrics.total_responses += 1

                        # Create task output object
                        class TaskOutput:
                            def __init__(self, agent, raw):
                                self.agent = agent
                                self.raw = raw

                        task_output = TaskOutput(task.agent, task.output.raw if hasattr(task.output, 'raw') else str(task.output))

                        # Send immediately!
                        loop.call_soon_threadsafe(response_queue.put_nowait, ('task', idx, task_output))
                        sent_tasks.add(idx)

                        logger.info(f"📡 TRACE: Streamed response from '{agent_name}' to frontend")

                        # Set event to notify task availability
                        task_available_event.set()

            # Use event-driven waiting instead of busy polling
            task_available_event.wait(timeout=0.2)  # Wait for event or timeout
            task_available_event.clear()  # Clear event after processing
        
        # Wait for thread to complete
        crew_thread.join(timeout=1)

        # Final scan/flush of remaining outputs after loop completion
        # Check for any late-set crew_result or remaining tasks
        if crew_result[0] and hasattr(crew_result[0], 'tasks_output'):
            for idx, task_output in enumerate(crew_result[0].tasks_output):
                if idx not in sent_tasks:
                    agent_name = NAME_MAPPING.get(str(task_output.agent).strip().lower(), str(task_output.agent))
                    logger.info(f"📡 TRACE: Sending remaining response from '{agent_name}'")
                    loop.call_soon_threadsafe(response_queue.put_nowait, ('task', idx, task_output))
                    sent_tasks.add(idx)

        # Also check crew_instance for any remaining outputs that might not be in crew_result
        if hasattr(crew_instance, '_tasks') and hasattr(crew_instance, 'tasks'):
            for idx, task in enumerate(crew_instance.tasks):
                if hasattr(task, 'output') and task.output and idx not in sent_tasks:
                    agent_name = NAME_MAPPING.get(str(task.agent).strip().lower(), str(task.agent))
                    logger.info(f"📡 TRACE: Final flush - sending remaining response from '{agent_name}'")

                    # Create task output object
                    class TaskOutput:
                        def __init__(self, agent, raw):
                            self.agent = agent
                            self.raw = raw

                    task_output = TaskOutput(task.agent, task.output.raw if hasattr(task.output, 'raw') else str(task.output))
                    loop.call_soon_threadsafe(response_queue.put_nowait, ('task', idx, task_output))
                    sent_tasks.add(idx)
        
        loop.call_soon_threadsafe(response_queue.put_nowait, ('done', None, None))
        logger.info("✅ TRACE: All agents completed successfully")
        
    except Exception as e:
        logger.error(f"❌ ERROR: Crew execution error: {e}", exc_info=True)
        loop.call_soon_threadsafe(response_queue.put_nowait, ('error', None, str(e)))

# ═══════════════════════════════════════════════════════════════
# API Endpoints
# ═══════════════════════════════════════════════════════════════

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Chaos Oracle WebSocket Server",
        "version": "3.0.0 - Real-Time Streaming + Observability",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    with manager._lock:
        active_connections_count = len(manager.active_connections)
    return {
        "status": "healthy",
        "active_connections": active_connections_count,
        "agents": AGENT_ORDER
    }

@app.get("/metrics")
async def get_metrics():
    """Observability: Expose metrics endpoint"""
    return metrics.get_metrics()

# ═══════════════════════════════════════════════════════════════
# WebSocket Endpoint
# ═══════════════════════════════════════════════════════════════

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            logger.info(f"📨 Received message type: {message_data.get('type')}")
            
            if message_data.get("type") == "user_message":
                user_question = message_data.get("content", "")
                logger.info(f"💬 User question: {user_question[:100]}")
                
                await manager.send_message({
                    "type": "processing_started",
                    "timestamp": datetime.now().isoformat()
                }, websocket)
                
                await manager.send_message({
                    "type": "typing",
                    "agents": AGENT_ORDER,
                    "message": "The cult is gathering..."
                }, websocket)
                
                # Create queue for real-time streaming
                response_queue = asyncio.Queue()
                
                # Get the current event loop to pass to the monitoring thread
                current_loop = asyncio.get_running_loop()
                
                # Start monitoring in background
                monitor_thread = threading.Thread(
                    target=run_crew_with_monitoring,
                    args=(user_question, response_queue, current_loop),
                    daemon=True
                )
                monitor_thread.start()
                
                # Stream responses as they arrive
                agent_index = 0
                processing = True
                
                while processing:
                    try:
                        msg_type, idx, data = await response_queue.get()
                        
                        if msg_type == 'task':
                            raw_agent_name = str(data.agent).strip()
                            agent_name = NAME_MAPPING.get(raw_agent_name.lower(), raw_agent_name)
                            content = data.raw if hasattr(data, 'raw') else str(data)
                            
                            logger.info(f"✅ Streaming response from {agent_name}")
                            
                            # Send typing indicator
                            await manager.send_message({
                                "type": "agent_typing",
                                "agent": agent_name,
                                "timestamp": datetime.now().isoformat()
                            }, websocket)
                            
                            await asyncio.sleep(0.3)
                            
                            # Send response
                            await manager.send_message({
                                "type": "agent_response",
                                "agent": agent_name,
                                "content": content.strip(),
                                "timestamp": datetime.now().isoformat(),
                                "index": agent_index
                            }, websocket)
                            
                            agent_index += 1
                            await asyncio.sleep(0.2)
                            
                        elif msg_type == 'done':
                            await manager.send_message({
                                "type": "processing_complete",
                                "timestamp": datetime.now().isoformat()
                            }, websocket)
                            processing = False
                            logger.info("✅ Processing complete")
                            
                        elif msg_type == 'error':
                            logger.error(f"❌ Error: {data}")
                            await manager.send_message({
                                "type": "error",
                                "message": f"The Oracle encountered a disturbance: {data}",
                                "timestamp": datetime.now().isoformat()
                            }, websocket)
                            processing = False
                            
                    except asyncio.TimeoutError:
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        logger.error(f"❌ Error in streaming loop: {e}")
                        processing = False
            
            elif message_data.get("type") == "ping":
                await manager.send_message({
                    "type": "pong",
                    "timestamp": datetime.now().isoformat()
                }, websocket)
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"❌ WebSocket error: {str(e)}")
        manager.disconnect(websocket)

if __name__ == "__main__":
    logger.info("🔮 Starting Chaos Oracle WebSocket Server with Observability...")
    logger.info("📡 WebSocket endpoint: ws://localhost:8000/ws")
    logger.info("🌐 Health check: http://localhost:8000/health")
    logger.info("📊 Metrics endpoint: http://localhost:8000/metrics")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
