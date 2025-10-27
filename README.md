# 🎣 Star Echo Fishing Bot

An advanced automatic fishing tool for **Blue Protocol** with real-time fish rarity detection and statistics tracking.

## ✨ Features

- 🎣 **Automatic Fishing** - Automatic fishing with rod casting and reeling
- 🐠 **Fish Rarity Detection** - Automatically detects common, rare, and mythical fish
- 📊 **Statistics Tracking** - Tracks fish caught and categories in real-time
- 🔍 **Debug Capture** - Exports screenshots for troubleshooting
- 📱 **Multi-Resolution Support** - Works on any screen resolution
- 🛒 **Auto-Purchase** - Automatically buys fishing rods and bait when depleted

## 🚀 Quick Start (For Beginners)

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. **⚠️ IMPORTANT:** During installation, check the box that says **"Add Python to PATH"**
3. Click "Install Now"

### Step 2: Setup the Bot
1. Download or extract this project
2. **Double-click** `install.bat` in the project folder
3. Wait for installation to complete (it will show "Installation completed successfully!")

### Step 3: Run the Bot
**Double-click** `run.bat` to start fishing automation

That's it! No command line needed! 🎉

---

## 📋 File Guide

### Batch Files (Double-click to run)

| File | Purpose |
|------|---------|
| `install.bat` | First time setup - creates virtual environment and installs packages |
| `run.bat` | Start fishing automation |

### Python Files
- `src/fish_main.py` - Main fishing automation script
- `src/main.py` - Legacy menu system

---

## 🎮 How to Use Fishing Automation

1. **Double-click** `run.bat`
2. Make sure the game is running and visible
3. Go to the fishing area in-game
4. Press **F5** to start the script
5. Press **F6** to pause
6. Press **ESC** to exit

**What it does:**
- Automatically casts your fishing rod
- Waits for fish to bite
- Reels in the fish
- Detects fish rarity (common, rare, mythical)
- Tracks your catch statistics
- Automatically buys more rods and bait when depleted
- Repeats until you stop it

---

## ⚠️ Important Requirements

### Before Running the Script:

1. ✅ **Run as Administrator** (Right-click → Run as administrator)
2. ✅ **Python 3.9+** installed with "Add Python to PATH" checked
3. ✅ **Blue Protocol** game is running
4. ✅ **Game window** is visible on screen
5. ✅ **Don't cover** the game window with other apps
6. ✅ **Mouse is free** to move (no other software controlling it)

### First Time Only:
1. Open `install.bat` 
2. Let it complete (takes 2-5 minutes)
3. After success, you're ready to go!

---

## 🐛 Troubleshooting

### "Python is not installed or not in PATH"
- Solution: Install Python from https://www.python.org/ and CHECK "Add Python to PATH"
- Then run `install.bat` again

### "Virtual environment not found"
- Solution: Run `install.bat` first

### Script runs but doesn't fish
- Make sure game window is visible
- Try pressing F5 to start
- Check if game is in fishing interface
- Run as Administrator

### Fish rarity not detecting
- Check `src/fish/modules/pic/en/debug_fish_rarity.png`
- This shows what the script is seeing
- If it's black, the rarity box position is wrong

### Script stops immediately
- Check Windows Task Manager - make sure no other Python scripts are running
- Close any overlays (Discord, streaming software, etc.)
- Try running as Administrator

---

## 📊 Debug Screenshots

The bot saves debug images to help troubleshoot:

**Location:** `src/fish/modules/pic/en/` (or `/zh/` for Chinese)

- `debug_fish_rarity.png` - What the rarity detection sees
- `debug_full_screenshot_with_rarity_region.png` - Full screen with highlighted capture area
- `debug_screenshot_stop.png` - Last screenshot before stopping
- `yugan_screenshot.png` - Fishing rod status
- `yuer_screenshot.png` - Bait status

---

## 🎯 Keyboard Controls

- **F5** = Start fishing
- **F6** = Pause fishing
- **ESC** = Exit script

---

## 📝 Configuration

Edit these files to customize:

- `requirements.txt` - Python packages to install
- `src/fish/modules/fishing_logic.py` - Fishing behavior and detection settings
- `src/fish_main.py` - Fishing automation settings

---

## 🔧 System Requirements

- **OS:** Windows 7, 8, 10, 11
- **Python:** 3.9 or higher
- **RAM:** 2GB minimum (4GB recommended)
- **Disk Space:** 500MB for venv and packages
- **Game:** Blue Protocol

---

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Look at debug screenshots in `src/fish/modules/pic/en/`
3. Review console output for error messages
4. Make sure all requirements are met

---

## 📖 For Experienced Users

If you prefer command line:

```bash
# Setup
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Run fishing
cd src
python fish_main.py
```

---

## 📄 License

This project is provided as-is for educational purposes.

---

## ⭐ Tips for Best Results

1. ✅ Run as Administrator
2. ✅ Use a dedicated fishing spot
3. ✅ Ensure stable internet connection
4. ✅ Don't move the mouse while script is running
5. ✅ Check debug images if something goes wrong
6. ✅ Keep the game window in focus/visible

**Happy fishing!** 🎣✨

---

**Last Updated:** 2025-01-27  
**Version:** 2.1 (Fishing Focus)
