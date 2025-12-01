@echo off
echo ========================================
echo   Chaos Oracle - Frontend
echo ========================================
echo.

cd frontend

echo Installing frontend dependencies...
call npm install

echo.
echo Starting Next.js Development Server...
echo Frontend will be available at: http://localhost:3000
echo.

call npm run dev
