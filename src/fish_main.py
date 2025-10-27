import os
import cv2
import keyboard
from datetime import datetime, timedelta
import pyautogui
import time
import numpy as np
from fish.modules.utils import (find_game_window, SwitchToGame, InitUnitLang,
                                 debug_screenshot_data,full_imagePath)
from fish.modules.fishing_logic import (
    init_clicker,get_clicker, youganma, jinlema, shanggoulema, fishing_choose,
    diaoyuchong, diaodaole,diaodaolema, PlayerCtl, SolveDaySwitch ,fish_area_cac,
    InitFishLogicLang, detect_fish_rarity, log_fish_catch, get_fish_statistics
)
from fish.modules.logger import GetLogger ,log_init
from fish.modules.locate import GetSysLang,InitSysLang

STOP_HOUR = 8
STOP_MINUTE = 0
pyautogui.FAILSAFE = True
FishMainLangFlag = True # True is Chinese, False is English
logger = None
clicker = None
class FishMainStatus:
    """游戏窗口类"""
    def __init__(self):
        self.startTime = datetime.now()
        self.timeOutTimes = 0
        self.resetFlag = True
        self.gamewindow = None
        self.FishStopFlag = False
        self.yuer = None
        self.yugan = None
        self.shanggoufind = None
        self.zuofind = None
        self.youfind = None
        self.jixufind = None
        self.zhanglifind = None
        self.fish_rarity_region = None
        self.status = 0
        self.fishCounter = 0
    
    def addFishCounter(self):
        self.fishCounter += 1
    
    def addTimeOutTimes(self):
        self.timeOutTimes += 1
    
    def resetTimeOutTimes(self):
        self.timeOutTimes = 0

    def setStartTime(self):
        self.startTime = datetime.now()
    def getTimeLag (self):
        return datetime.now() - self.startTime
    def setstatus(self,data):
        self.status = data
    def stop(self):
        self.FishStopFlag = True
    def reload(self):
        # Reload window to ensure switched to Star Echo window before taking screenshot
        SwitchToGame()
        print("Try to get the fishing status window")
        pyautogui.sleep(2)
        gamewindow = None
        counter = 0
        while gamewindow is None:
            screenshot = pyautogui.screenshot()
            screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            gamewindow = find_game_window(screenshot_cv,"fish")
            counter += 1
            if counter > 10:
                print("Failed to get the fishing status window, please make sure the game has entered the fishing interface")
                return False
        # Calculate each detection area
        self.gamewindow = gamewindow
        self.yuer,self.yugan,self.shanggoufind,self.zuofind,self.youfind,self.jixufind,self.zhanglifind,self.fish_rarity_region = fish_area_cac(gamewindow)
        debug_screenshot_data(screenshot_cv,gamewindow,self.yuer,self.yugan,self.shanggoufind,self.zuofind,self.youfind,self.jixufind,self.zhanglifind)
        return True

g_FishMain = FishMainStatus()

def fish_InitLogger():
    global logger  
    logger = GetLogger()
def fish_InitClicker():
    global clicker
    clicker = get_clicker()

def should_stop():
    """Check if the current time has reached the stop time"""
    now = datetime.datetime.now()
    if now.hour >= STOP_HOUR and now.minute >= STOP_MINUTE:
        return True
    return False
def InitFishMainLang(mylang):
    global FishMainLangFlag
    if mylang == "zh":
        FishMainLangFlag = True
    else:
        FishMainLangFlag = False
def InitAllLang():
    InitSysLang()
    mylang = GetSysLang()
    InitFishMainLang(mylang)
    InitUnitLang(mylang)
    InitFishLogicLang(mylang)
    log_init()
def GuideInfomation():
    print("\n\nWelcome to the Star Echo Fishing Script")
    print("This script recognizes 16:9 game windows\n")
    print("⚠️  IMPORTANT: Run this program as ADMINISTRATOR!")
    print("⚠️  IMPORTANT: Run this program as ADMINISTRATOR!")
    print("⚠️  IMPORTANT: Run this program as ADMINISTRATOR!\n")
    print("Tip 1: Make sure the game has entered the fishing interface!")
    print("Tip 2: The script will automatically replenish Special fish bait after using all rods and bait")
    print("Tip 3: If infinite clicking occurs, move mouse to upper-left corner, then press [F6] to pause")
    print("Tip 4: You can use [PageUp] and [PageDown] to adjust detection time (default: 0.06s)")
    print("Tip 5: Press [F5] to start, [F6] to pause, [ESC] to exit\n")
    
    print("Choose bait type to automatically replenish (default: Special bait):")
    print("0. Regular bait")
    print("1. Special bait")
    choice = input("Enter your choice: ")
    fishing_choose(choice)
    print("\nPress [F5] to start the script!")
    print("Remember: [Hold F6] to pause, [ESC] to exit\n")

def fish_init():
    InitAllLang()
    GuideInfomation()
    # print(f"{g_current_dir}")
    while True:
        if keyboard.is_pressed('F5'):
            if FishMainLangFlag:
                print("脚本开始运行")
            else:
                print("The script is running")
            break
        time.sleep(0.05)
    init_clicker()
    SwitchToGame()
    fish_InitLogger()
    fish_InitClicker()

def fish_KeyboardStopScript():
    clicker = get_clicker()
    if keyboard.is_pressed('F6'):
        g_FishMain.stop()
        clicker.stop_clicking()
        pyautogui.keyUp('A')
        pyautogui.keyUp('D')
        pyautogui.mouseUp(button='left')
        if FishMainLangFlag:
            print("✅ Detected F6 key, stop script")
        else:
            print("✅ Detected F6 key, stop script")

def fish_reset():
    SwitchToGame()
    # Try to click on the daily reset problem
    if(g_FishMain.zhanglifind is not None):
        reset_counter = 0
        while(reset_counter < 3):
            if SolveDaySwitch(g_FishMain.jixufind,g_FishMain.zhanglifind):
                break
            reset_counter += 1
        if reset_counter < 3:
            pass
        else:
            stopScreenshot = pyautogui.screenshot()
            stopScreenshot_cv = cv2.cvtColor(np.array(stopScreenshot), cv2.COLOR_RGB2BGR)
            image_save_path = full_imagePath("debug_screenshot_stop.png")
            cv2.imwrite(image_save_path, stopScreenshot_cv)
            if FishMainLangFlag:
                print("Unable to reset to normal MiniGame interface, force stop script\n")
                logger.critical("Unable to reset to normal MiniGame interface, force stop script\n")
                print(f"Debug screenshot has been saved to {image_save_path}\n")
                logger.critical(f"Debug screenshot has been saved to {image_save_path}\n")
            else:
                print("Unable to reset to normal MiniGame interface, force stop script\n")
                logger.critical("Unable to reset to normal MiniGame interface, force stop script\n")
                print(f"Debug screenshot has been saved to {image_save_path}\n")
                logger.critical(f"Debug screenshot has been saved to {image_save_path}\n")
            return False
    return g_FishMain.reload()

def fish_HardOutDate():
    if FishMainLangFlag:
        print("⚠️ More than 90 seconds have passed without moving, most likely the Monthly Pass has arrived or there is a major problem, forcing restart mode")
        logger.critical("⚠️ More than 90 seconds have passed without moving, most likely the Monthly Pass has arrived or there is a major problem, forcing restart mode")
    else:
        print("⚠️ More than 90 seconds have passed without moving, most likely the Monthly Pass has come or there is a big problem, force restart mode")
        logger.critical("⚠️ More than 90 seconds have passed without moving, most likely the Monthly Pass has come or there is a big problem, force restart mode")
    if fish_reset():
        g_FishMain.setstatus(0)
    else:
        g_FishMain.stop()
        if FishMainLangFlag:
            print("⚠️ Can't restore to fishing interface, stop script")
        else:
            print("⚠️ Cant restore to fishing interface, stop script")
    
def fish_SoftOutDate():
    if FishMainLangFlag:
        print("⏰ ⚠️ More than 30 seconds have passed without ending the fishing process, forcing status check...")
        logger.debug("⏰ ⚠️ More than 30 seconds have passed without ending the fishing process, forcing status check...")
    else:
        print("⏰ ⚠️ More than 30 seconds have passed without ending the fishing process, force check status...")
        logger.debug("⏰ ⚠️ More than 30 seconds have passed without ending the fishing process, force check status...")
        
    if jinlema(g_FishMain.yugan):
        if FishMainLangFlag:
            print("🐟 Still fishing, continue waiting")
            logger.debug("🐟 Still fishing, continue waiting")
        else:
            print("🐟 Still fishing, continue waiting")
            logger.debug("🐟 Still fishing, continue waiting")
        # Check if still in fishing interface, if so don't worry
        return False
    else:
        # Not in fishing interface, check if fish has been hooked
        if(diaodaolema(g_FishMain.jixufind)): 
            if FishMainLangFlag:
                print("🐟 Detected that the fish has been hooked, but timed out without handling, re-checking")
                logger.debug("🐟 Detected that the fish has been hooked, but timed out without handling, re-checking")
            else:
                print("🐟 Detected that the fish has been hooked, but it timed out and was not processed, re-checking")
                logger.debug("🐟 Detected that the fish has been hooked, but it timed out and was not processed, re-checking")
            diaodaole()
        else:
            if FishMainLangFlag:
                print("❌ Timeout and not in fishing interface, no fish hooked, restart process")
                logger.error("❌ Timeout and not in fishing interface, no fish hooked, restart process")
            else:
                print("❌ Timeout and not in the fishing interface, no fish is hooked, restart the process")
                logger.error("❌ Timeout and not in the fishing interface, no fish is hooked, restart the process")
        g_FishMain.setstatus(0)
        return True
    
def fish_StopData():
    stats = get_fish_statistics()
    print(f"\n✅ Script stopped")
    print(f"📊 Final Statistics:")
    print(f"   Total fish caught: {g_FishMain.fishCounter}")
    print(f"   🔵 Common: {stats['common']}")
    print(f"   💜 Rare: {stats['rare']}")
    print(f"   ⭐ Mythical: {stats['mythical']}")

def fish_ProgressDefault():
    clicker.stop_clicking()
    if youganma(g_FishMain.yugan, g_FishMain.yuer):   
        PlayerCtl.leftmouse(1)
        if FishMainLangFlag:
            print("🎯 Casting rod...")
        else:
            print("🎯 Throwing a rod...")
        g_FishMain.setstatus(1)
    else:
        if FishMainLangFlag:
            logger.debug("❌ No rod or bait, try to buy")
        else:
            logger.debug("❌ No rod or bait, try to buy")

        
def fish_ProgressCheckMiniGameStart():
    clicker.stop_clicking()
    if jinlema(g_FishMain.yugan):
        "Entered fishing only counts as start of loop, avoid infinite casting"
        g_FishMain.setStartTime()
        if FishMainLangFlag:
            print("✅ Successfully cast rod into fishing interface.")
        else:
            print("✅ Successfully threw a rod into the fishing interface.")
        g_FishMain.setstatus(2)
    else:
        if FishMainLangFlag:
            print("❌ Failed to cast rod, trying again")
        else:
            print("❌ Failed to throw a rod, try again")
        g_FishMain.setstatus(0)

def fish_ProgressCheckHook():
    clicker.stop_clicking()
    if shanggoulema(g_FishMain.shanggoufind, g_FishMain.gamewindow):
        if FishMainLangFlag:
            print("🎣 Detected that the fish has been hooked! Ready to fish!")
        else:
            print("🎣 Detected that the fish has been hooked! Ready to fish!")
        g_FishMain.setstatus(3)

def fish_ProgressFishing():
    if diaoyuchong(g_FishMain.zuofind,
                    g_FishMain.youfind,
                    g_FishMain.jixufind,
                    g_FishMain.zhanglifind):
        print("🎣 The fish has been reeled in, ready for the next round of fishing\n\n")
        logger.info(f"🐟 Fish reeled in")
        g_FishMain.setstatus(4)

def fish_ProgressFinishied():
    clicker.stop_clicking()
    
    # Wait for the fish result screen to fully appear
    time.sleep(1.0)
    
    # Detect fish rarity BEFORE clicking "Continue fishing"
    rarity = detect_fish_rarity(g_FishMain.fish_rarity_region)
    log_fish_catch(rarity)
    
    # Now click "Continue fishing"
    if diaodaole():
        lag = g_FishMain.getTimeLag()
        
        g_FishMain.addFishCounter()
        
        # Get current statistics
        stats = get_fish_statistics()
        
        # Print results
        print(f"✅ The fish has been reeled in, this round took {lag.total_seconds():.1f}s\n")
        print(f"🐠 Currently caught {g_FishMain.fishCounter} fish~")
        print(f"📊 Fish Statistics:")
        print(f"   🔵 Common: {stats['common']}")
        print(f"   💜 Rare: {stats['rare']}")
        print(f"   ⭐ Mythical: {stats['mythical']}\n")
        
        logger.info(f"🐠 Currently caught {g_FishMain.fishCounter} fish~")
        
        g_FishMain.setstatus(0)
        g_FishMain.setStartTime()
        g_FishMain.resetTimeOutTimes()

g_FishFunctionDic = {
    0:fish_ProgressDefault,
    1:fish_ProgressCheckMiniGameStart,
    2:fish_ProgressCheckHook,
    3:fish_ProgressFishing,
    4:fish_ProgressFinishied
}

def fish_porgress():
    if FishMainLangFlag:
        print("Fishing in progress...")
        logger.info("Fishing in progress...")
    else:
        print("Fishing in progress...")
        logger.info("Fishing in progress...")
    
    if g_FishMain.reload() is not True:
            return
    # Main loop
    timeout = timedelta(minutes=0, seconds=30)
    g_FishMain.setStartTime()
    g_FishMain.resetTimeOutTimes()
    while True:
        fish_KeyboardStopScript()
        # If more than 30 seconds have passed, reset the timer
        if g_FishMain.getTimeLag() > timeout:
            g_FishMain.setStartTime()
            SwitchToGame()
            if fish_SoftOutDate():
                g_FishMain.resetTimeOutTimes()
            if g_FishMain.timeOutTimes >= 3:
                fish_HardOutDate()
                g_FishMain.resetTimeOutTimes()
            g_FishMain.addTimeOutTimes()

        if g_FishMain.FishStopFlag:
            fish_StopData()
            return
        
        g_FishFunctionDic[g_FishMain.status]()

        time.sleep(0.05)

def fish_main():
    try:
        fish_init()
        fish_porgress()
    except KeyboardInterrupt:
        if FishMainLangFlag:
            print("\nUser interrupted the script")
        else:
            print("\nUser interrupted the script")
    except Exception as e:
        if FishMainLangFlag:
            print(f"An error occurred: {e}")
        else:
            print(f"An error occurred: {e}")
    finally:
        pass

if __name__ == "__main__":
    fish_main()
