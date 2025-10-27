import os
import cv2
import keyboard
from datetime import datetime, timedelta
import pyautogui
import time
import numpy as np
import fish_main as fish
import fuben_main as fuben
import kuaijie_main as kuaijie
from fish.modules.locate import InitSysLang, GetSysLang

STOP_HOUR = 8
STOP_MINUTE = 0
pyautogui.FAILSAFE = True


def should_stop():
    """检查当前时间是否达到停止时间"""
    now = datetime.datetime.now()
    if now.hour >= STOP_HOUR and now.minute >= STOP_MINUTE:
        return True
    return False

def select():
    InitSysLang()
    print("Welcome to Star Resonance Smart Fishing Script")
    print("Only Fishing is available.")
    print("Starting Fishing script...\n")
    fish.fish_main()
if __name__ == "__main__":
    select()