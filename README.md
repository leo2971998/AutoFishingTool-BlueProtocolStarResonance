# Star Resonance Smart Fishing Bot
## Blue Protocol Auto Fishing Script

An intelligent Python automation script for fishing in Star Resonance (Blue Protocol) with **real-time fish rarity detection**.

---

## ✨ Features

- 🎮 **Automatic Game Window Detection** - Finds and monitors 16:9 game windows
- 🎣 **Auto Fishing** - Automatically casts rod, detects bites, and reels in fish
- 🛒 **Auto Purchase** - Automatically buys fishing rods and bait when depleted
- 🐟 **Fish Rarity Detection** - Detects and tracks fish by rarity (Mythical/Rare/Common)
- 📊 **Live Statistics** - Real-time tracking of caught fish by type
- 🌍 **English Only** - Fully localized for English language gameplay
- 🔍 **Debug Mode** - Saves screenshots for detection troubleshooting

---

## 📋 Requirements

### System Requirements
- **Python**: 3.12.7 or higher
- **Game**: Star Resonance (Blue Protocol) - English version
- **Resolution**: 1920×1080 (16:9 aspect ratio, supports up to 2K)
- **Admin Rights**: Must run as Administrator

### Python Dependencies
```
opencv-python==4.12.0.88
numpy==2.2.6
PyAutoGUI==0.9.54
PyGetWindow==0.0.9
keyboard==0.13.5
Pillow==12.0.0
mouseinfo==0.1.3
```

---

## 🚀 Installation

### Method 1: Quick Install (Windows)
1. **Run the installer**:
   ```bash
   install.bat
   ```
   This will automatically install all dependencies.

### Method 2: Manual Install
1. **Clone or download this repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎯 Usage

### Starting the Script

1. **Launch the game** and enter the fishing interface
2. **Run the script** (as Administrator):
   ```bash
   run.bat
   ```
   Or manually:
   ```bash
   python src/main.py
   ```

3. **Select bait type**:
   ```
   Choose bait type to automatically replenish (default: Special bait):
   0. Regular bait
   1. Special bait
   ```

4. **Press [F5]** to start fishing!

### Controls

| Key | Action |
|-----|--------|
| **F5** | Start the fishing script |
| **F6** | Pause the script (hold key) |
| **ESC** | Exit the script |
| **Ctrl+C** | Emergency stop (in console) |

### Safety Feature
If the script clicks infinitely, move your mouse to the **upper-left corner** of the screen to trigger failsafe, then press **F6** to stop.

---

## 🐟 Fish Rarity Detection

The script automatically detects fish rarity by analyzing the **bottom-left corner** of the game window after each catch.

### Detected Rarities
- ⭐ **Mythical** (Yellow/Gold) - RGB: (255, 215, 0)
- 💜 **Rare** (Purple) - RGB: (147, 51, 234)
- 💚 **Common** (Green) - RGB: (34, 197, 94)

### Real-Time Output
After catching each fish, you'll see:
```
⭐ Detected: MYTHICAL fish!
🎣 The fish has been reeled in, ready for the next round of fishing

🐠 Currently caught 16 fish~
📊 Fish Statistics:
   ⭐ Mythical: 3
   💜 Rare: 8
   💚 Common: 5
```

### Final Summary
When you stop the script:
```
✅ Script stopped
📊 Final Statistics:
   Total fish caught: 16
   ⭐ Mythical: 3
   💜 Rare: 8
   💚 Common: 5
```

---

## 🔧 Configuration & Fine-Tuning

### Adjusting Fish Detection

If fish rarity detection is inaccurate, you can fine-tune these settings in `src/fish/modules/fishing_logic.py`:

#### 1. **RGB Color Values** (lines 27-31)
```python
FISH_RARITY_COLORS = {
    'mythical': (255, 215, 0),   # Yellow/Gold
    'rare': (147, 51, 234),       # Purple
    'common': (34, 197, 94)       # Green
}
```
**How to adjust**: Take a screenshot, use a color picker to get exact RGB values.

#### 2. **Color Tolerance** (line 376)
```python
tolerance=40  # Higher = more lenient matching
```
**Recommended range**: 30-60

#### 3. **Match Threshold** (line 377)
```python
match_threshold=0.05  # Lower = more sensitive
```
**Recommended range**: 0.01-0.10

#### 4. **Detection Delay** (in `src/fish_main.py` line 299)
```python
time.sleep(1.5)  # Wait for fish display animation
```
**Adjust if**: Fish display animation is faster/slower

#### 5. **Detection Region** (lines 474-479)
```python
fish_rarity_region = (
    int(gamewindow[0] + 0.02 * gamewindow[2]),   # Left offset: 2%
    int(gamewindow[1] + 0.85 * gamewindow[3]),   # Top offset: 85%
    int(0.15 * gamewindow[2]),                   # Width: 15%
    int(0.10 * gamewindow[3])                    # Height: 10%
)
```
**Adjust if**: Capture area doesn't align with fish display

---

## 🐛 Troubleshooting

### Debug Screenshots
The script saves debug screenshots to help troubleshoot detection issues:
- **Location**: `src/fish/modules/pic/en/`
- **Files**:
  - `debug_screenshot.png` - Main detection areas
  - `debug_fish_rarity.png` - Fish rarity capture region
  - `yugan_screenshot.png` - Fishing rod status
  - `yuer_screenshot.png` - Bait status

### Common Issues

#### Fish Rarity Not Detected
1. Check `debug_fish_rarity.png` to see what's being captured
2. Use a color picker to verify RGB values match the fish display
3. Adjust `tolerance` and `match_threshold` values
4. Ensure game is running in English

#### Script Won't Start
- ✅ Run as **Administrator**
- ✅ Ensure game window title is "Blue Protocol"
- ✅ Game must be in fishing interface
- ✅ Check resolution is 16:9 (1920×1080 or similar)

#### Infinite Clicking
1. Move mouse to upper-left corner (failsafe trigger)
2. Press **F6** to pause
3. Restart with **F5**

#### Can't Find Game Window
- Game window must have "Blue Protocol" in the title
- Resolution must be 16:9 aspect ratio
- Try switching to windowed mode

---

## 📁 Project Structure

```
Leo-AutoFishinBlueProtocol/
├── src/
│   ├── main.py                    # Entry point
│   ├── fish_main.py               # Main fishing logic
│   ├── fuben_main.py              # Dungeon script (Chinese only)
│   ├── kuaijie_main.py            # Quick switch (Chinese only)
│   └── fish/
│       └── modules/
│           ├── fishing_logic.py   # Core fishing & detection
│           ├── locate.py          # Language & localization
│           ├── utils.py           # Image processing utilities
│           ├── player_control.py  # Input automation
│           ├── camera_control.py  # Camera handling
│           ├── logger.py          # Logging system
│           └── pic/
│               └── en/            # English UI templates
├── requirements.txt
├── install.bat                    # Quick installer
├── run.bat                        # Quick launcher
└── README.md
```

---

## ⚙️ How It Works

### Detection Flow
1. **Game Window Detection** - Locates the game by finding ESC button
2. **Fishing Rod Check** - Verifies rod and bait are equipped
3. **Cast Rod** - Left-click to cast
4. **Wait for Bite** - Monitors for yellow hook indicator
5. **Reel In** - Presses A/D keys to keep fish centered
6. **Handle Tension** - Rapid clicks during tension phase
7. **Capture Rarity** - Screenshots bottom-left corner after 1.5s delay
8. **Color Analysis** - Compares pixels against known rarity colors
9. **Update Statistics** - Increments counters and displays results
10. **Continue** - Clicks "Continue Fishing" button

### Auto-Purchase
- Automatically opens inventory (M/N keys)
- Checks for "Use" button on items
- Opens shop (B key) if items depleted
- Purchases 200 rods or bait
- Returns to fishing

---

## 🎮 Tips for Best Results

1. **Use Special Bait** - Better fish = more accurate color detection
2. **Stable Internet** - Prevents lag during detection window
3. **Clean UI** - Minimize overlays that might obstruct fish display
4. **Windowed Mode** - More reliable window detection
5. **16:9 Resolution** - Required for accurate region calculations
6. **Administrator Mode** - Required for input automation

---

## 📝 Logging

All fishing activities are logged to help track progress and debug issues.

**Log Location**: `src/fish/modules/pic/en/log.txt`

**Logged Events**:
- Fish caught with rarity
- Rod/bait purchases
- Detection errors
- Statistics updates

---

## ⚠️ Important Notes

- ⚠️ **Must run as Administrator** for keyboard/mouse automation
- ⚠️ **English game version only** - UI template matching requires English
- ⚠️ **16:9 resolution required** - Other aspect ratios won't work properly
- ⚠️ **Fishing interface only** - Script must be started while fishing
- ⚠️ **Use responsibly** - Automation may violate game terms of service

---

## 🔄 Updates & Improvements

### Recent Changes
- ✅ Removed all Chinese language support
- ✅ Added fish rarity detection system
- ✅ Real-time statistics display
- ✅ Debug screenshot functionality
- ✅ Improved English localization
- ✅ Better error handling

### Future Enhancements
- [ ] Multi-resolution support
- [ ] Machine learning for better fish detection
- [ ] Web dashboard for statistics
- [ ] Discord notifications
- [ ] Support for other fishing locations

---

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows existing style
- Comments are in English
- Test with English game client
- Update README for new features

---

## 📄 License

This project is for educational purposes only. Use at your own risk.

---

## 🙏 Credits

Original concept and base fishing automation by the Star Resonance community.

Fish rarity detection and English localization improvements by contributors.

---

## 📞 Support

If you encounter issues:
1. Check the **Troubleshooting** section
2. Review `debug_fish_rarity.png` screenshots
3. Check log files in `src/fish/modules/pic/en/`
4. Verify all requirements are met

---

**Happy Fishing! 🎣**
