@echo off
setlocal enabledelayedexpansion

color 0B
title Star Echo - Fishing Bot

cls
echo.
echo ================================================
echo   Star Echo Fishing Bot - Automation
echo ================================================
echo.

REM Check if venv exists
if not exist "venv" (
    color 0C
    echo ERROR: Virtual environment not found!
    echo Please run "install.bat" first
    echo.
    pause
    exit /b 1
)

REM Check if src folder exists
if not exist "src" (
    color 0C
    echo ERROR: src folder not found!
    echo.
    pause
    exit /b 1
)

echo   IMPORTANT REQUIREMENTS:
echo.
echo   1. Blue Protocol game must be running
echo   2. Game window must be visible
echo   3. Close all other overlays
echo.
echo CONTROLS:
echo   - Press F5 to START the script
echo   - Press F6 to PAUSE (then F5=restart or ESC=exit)
echo.
echo Starting Fishing Automation in 5 seconds...
echo (Press Ctrl+C now to cancel)
echo.
timeout /t 5 /nobreak

cd src
call ..\venv\Scripts\activate.bat
python fish_main.py
cd ..

echo.
echo ================================================
echo   Fishing Automation Ended
echo ================================================
echo.
pause