@echo off
echo ========================================
echo   Chaos Oracle - Backend Server
echo ========================================
echo.

echo Installing backend dependencies...
pip install -r backend_requirements.txt

echo.
echo Starting FastAPI WebSocket Server...
echo Server will be available at: http://localhost:8000
echo WebSocket endpoint: ws://localhost:8000/ws
echo.

python backend_server.py
