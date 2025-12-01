@echo off
echo ========================================
echo   Chaos Oracle - Full Stack Launcher
echo ========================================
echo.
echo This will start both backend and frontend servers
echo.

echo Starting Backend Server in new window...
start "Chaos Oracle - Backend" cmd /k start_backend.bat

timeout /t 3 /nobreak > nul

echo Starting Frontend Server in new window...
start "Chaos Oracle - Frontend" cmd /k start_frontend.bat

echo.
echo ========================================
echo   Servers Starting!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to close this window...
pause > nul
