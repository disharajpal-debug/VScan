# Visiting Card Reader - Quick Start Script (PowerShell)
# This script sets up and runs the application

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Visiting Card Reader - Setup & Run" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if venv exists
if (-not (Test-Path "venv")) {
    Write-Host "[!] Virtual environment not found!" -ForegroundColor Yellow
    Write-Host "[*] Creating virtual environment..." -ForegroundColor Green
    python -m venv venv
}

Write-Host "[*] Activating virtual environment..." -ForegroundColor Green
& "venv\Scripts\Activate.ps1"

Write-Host "[*] Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt -q

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Configuration Check" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check for .env file
if (-not (Test-Path ".env")) {
    Write-Host "[X] ERROR: .env file not found!" -ForegroundColor Red
    Write-Host "[*] Please create .env file with your configuration." -ForegroundColor Yellow
    Write-Host "[*] See SETUP_AND_RUN.md for instructions." -ForegroundColor Yellow
    exit 1
}

Write-Host "[✓] .env file found" -ForegroundColor Green
Write-Host ""
Write-Host "[!] IMPORTANT - Verify these in .env:" -ForegroundColor Yellow
Write-Host "    ✓ GEMINI_API_KEY is set" -ForegroundColor Gray
Write-Host "    ✓ SMTP credentials configured (if using email)" -ForegroundColor Gray
Write-Host "    ✓ MongoDB is running on localhost:27017" -ForegroundColor Gray
Write-Host ""
Write-Host "[?] Press ENTER to continue or CTRL+C to exit..." -ForegroundColor Cyan
Read-Host

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Starting Application" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Running Flask development server..." -ForegroundColor Green
Write-Host "[*] Application will be available at: http://localhost:5000" -ForegroundColor Cyan
Write-Host "[*] Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python back.py

Write-Host ""
Write-Host "Application stopped." -ForegroundColor Yellow
