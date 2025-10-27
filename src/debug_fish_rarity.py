"""
Debug script to test formula-based fish rarity region calculation
"""

import cv2
import pyautogui
import numpy as np
import keyboard
import time

def debug_fish_rarity_capture():
    """
    Test formula-based rarity region calculation
    """
    print("=" * 70)
    print("Fish Rarity Debug Script (FORMULA-BASED TEST)")
    print("=" * 70)
    print("\n📌 Instructions:")
    print("   1. Go to the game and trigger the fish finish screen")
    print("   2. Press F5 when you see the rarity box appear")
    print("   3. The script will capture using formula-based coordinates")
    print("\n⏳ Waiting for F5 key press...")
    
    # Wait for F5 key press
    while True:
        if keyboard.is_pressed('F5'):
            time.sleep(0.2)
            break
        time.sleep(0.05)
    
    print("✅ F5 pressed! Starting capture...")
    
    # Assume standard 1920x1080 gamewindow (full screen)
    gamewindow = (0, 0, 1920, 1080)
    
    # Calculate fish_rarity_region using formula
    fish_rarity_region = (
        int(gamewindow[0] + 0.56 * gamewindow[2]),   # Start at 56% from left
        int(gamewindow[1] + 0.72 * gamewindow[3]),   # Start at 72% from top
        int(0.10 * gamewindow[2]),                    # Width 10% of window width
        int(0.08 * gamewindow[3])                     # Height 8% of window height
    )
    
    print("\n" + "=" * 70)
    print("📊 CALCULATION DEBUG INFO")
    print("=" * 70)
    print(f"\n🎮 Game Window:")
    print(f"   Tuple: {gamewindow}")
    print(f"   Left: {gamewindow[0]}, Top: {gamewindow[1]}")
    print(f"   Width: {gamewindow[2]}, Height: {gamewindow[3]}")
    
    print(f"\n🎯 Fish Rarity Region (FORMULA-BASED):")
    print(f"   Tuple: {fish_rarity_region}")
    print(f"\n   Left calculation:   gamewindow[0] + 0.56 * gamewindow[2]")
    print(f"                     = {gamewindow[0]} + 0.56 * {gamewindow[2]}")
    print(f"                     = {gamewindow[0]} + {0.56 * gamewindow[2]}")
    print(f"                     = {fish_rarity_region[0]}")
    
    print(f"\n   Top calculation:    gamewindow[1] + 0.72 * gamewindow[3]")
    print(f"                     = {gamewindow[1]} + 0.72 * {gamewindow[3]}")
    print(f"                     = {gamewindow[1]} + {0.72 * gamewindow[3]}")
    print(f"                     = {fish_rarity_region[1]}")
    
    print(f"\n   Width calculation:  0.10 * gamewindow[2]")
    print(f"                     = 0.10 * {gamewindow[2]}")
    print(f"                     = {fish_rarity_region[2]}")
    
    print(f"\n   Height calculation: 0.08 * gamewindow[3]")
    print(f"                     = 0.08 * {gamewindow[3]}")
    print(f"                     = {fish_rarity_region[3]}")
    
    print(f"\n   Right edge: {fish_rarity_region[0]} + {fish_rarity_region[2]} = {fish_rarity_region[0] + fish_rarity_region[2]}")
    print(f"   Bottom edge: {fish_rarity_region[1]} + {fish_rarity_region[3]} = {fish_rarity_region[1] + fish_rarity_region[3]}")
    
    # Take full screenshot
    print("\n1️⃣ Taking full screenshot...")
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    full_screenshot_path = "debug_full_screen_capture.png"
    cv2.imwrite(full_screenshot_path, screenshot_cv)
    print(f"   ✅ Saved to: {full_screenshot_path}")
    
    # Capture the rarity region
    print("\n2️⃣ Capturing rarity region...")
    rarity_screenshot = pyautogui.screenshot(region=fish_rarity_region)
    rarity_img_array = np.array(rarity_screenshot)
    rarity_img_cv = cv2.cvtColor(rarity_img_array, cv2.COLOR_RGB2BGR)
    
    rarity_path = "debug_fish_rarity.png"
    cv2.imwrite(rarity_path, rarity_img_cv)
    print(f"   ✅ Saved to: {rarity_path}")
    print(f"   Image size: {rarity_img_cv.shape[1]}x{rarity_img_cv.shape[0]}")
    
    # Check brightness
    gray = cv2.cvtColor(rarity_img_cv, cv2.COLOR_BGR2GRAY)
    mean_brightness = np.mean(gray)
    print(f"   Average brightness: {mean_brightness:.2f} (0=black, 255=white)")
    
    if mean_brightness > 50:
        print(f"   ✅ Image looks good (not black)")
    else:
        print(f"   ⚠️ Image is very dark")
    
    # Draw rectangle on full screenshot
    print("\n3️⃣ Creating debug screenshot with highlighted region...")
    debug_full = screenshot_cv.copy()
    
    top_left = (fish_rarity_region[0], fish_rarity_region[1])
    bottom_right = (
        fish_rarity_region[0] + fish_rarity_region[2],
        fish_rarity_region[1] + fish_rarity_region[3]
    )
    
    # Draw yellow rectangle
    cv2.rectangle(debug_full, top_left, bottom_right, (0, 255, 255), 3)
    
    # Add label
    label = f"Fish Rarity ({fish_rarity_region[2]}x{fish_rarity_region[3]})"
    cv2.putText(debug_full, label, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    debug_full_path = "debug_full_screenshot_with_rarity_region.png"
    cv2.imwrite(debug_full_path, debug_full)
    print(f"   ✅ Saved to: {debug_full_path}")
    
    print("\n" + "=" * 70)
    print("✅ Debug capture complete!")
    print("=" * 70)
    print(f"\n📁 Generated files in src/fish/modules/pic/en/:")
    print(f"   - {rarity_path}")
    print(f"   - {full_screenshot_path}")
    print(f"   - {debug_full_path}")

if __name__ == "__main__":
    try:
        debug_fish_rarity_capture()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
