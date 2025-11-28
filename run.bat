@echo off
REM Visiting Card Reader - Quick Start Script
REM This script sets up and runs the application

echo.
echo ============================================
echo  Visiting Card Reader - Setup & Run
echo ============================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo [!] Virtual environment not found!
    echo [*] Creating virtual environment...
    python -m venv venv
)

echo [*] Activating virtual environment...
call venv\Scripts\activate.bat

echo [*] Installing dependencies...
pip install -r requirements.txt -q

echo.
echo ============================================
echo  Configuration Check
echo ============================================
echo.

REM Check for .env file
if not exist ".env" (
    echo [!] ERROR: .env file not found!
    echo [*] Please create .env file with your configuration.
    pause
    exit /b 1
)

echo [✓] .env file found
echo.
echo [!] IMPORTANT - Before running, verify these in .env:
echo    - GEMINI_API_KEY is set
echo    - SMTP credentials configured (if using email)
echo    - MongoDB is running on localhost:27017
echo.
echo [?] Press ENTER to continue or CTRL+C to exit...
pause

echo.
echo ============================================
echo  Starting Application
echo ============================================
echo.
echo [*] Running Flask development server...
echo [*] Application will be available at: http://localhost:5000
echo [*] Press CTRL+C to stop the server
echo.

python back.py

pause
