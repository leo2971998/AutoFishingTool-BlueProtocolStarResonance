@echo off
setlocal enabledelayedexpansion

color 0A
title Star Echo - Fishing Bot - Installation

echo.
echo ================================================
echo   Star Echo Fishing Bot - Setup Installation
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.9+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

REM Check if venv directory exists
if exist "venv" (
    echo [2/4] Virtual environment already exists
    echo        Activating existing venv...
) else (
    echo [2/4] Creating Python virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        color 0C
        echo.
        echo ERROR: Failed to create virtual environment!
        echo.
        pause
        exit /b 1
    )
)

echo.
echo [3/4] Activating virtual environment and installing packages...
call venv\Scripts\activate.bat

REM Install requirements
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ERROR: Failed to install required packages!
    echo.
    pause
    exit /b 1
)

echo.
echo [4/4] Verifying installation...
python -c "import cv2; import pyautogui; import keyboard; import numpy; print('All packages installed successfully!')"

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ERROR: Package verification failed!
    echo.
    pause
    exit /b 1
)

color 0B
echo.
echo ================================================
echo   Installation completed successfully!
echo ================================================
echo.
echo Your system is ready to run the Star Echo Fishing Bot
echo.
echo Next steps:
echo 1. Run "run_fishing.bat" to start fishing automation
echo 2. Or run "run_menu.bat" to see all available options
echo.
pause