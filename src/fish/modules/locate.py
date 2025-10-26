import os
import locale

g_myLang = None
def PrintText():
    print("\n======================================")
    if GetSysLang() == "zh":
        print("中文模式")
    else:
        print("You selected English")
    print("======================================\n")
def GetSysLang():
    global g_myLang
    return g_myLang

def InitSysLang():
    global g_myLang
    if g_myLang is not None:
        return
    
    # Force English only - no language selection
    g_myLang = "en"
    print("\n======================================")
    print("English Mode")
    print("======================================\n")
    return

# 调用函数并打印结果
if __name__ == "__main__":
    InitSysLang()
    system_lang = GetSysLang()
    print(f"检测到的系统语言环境是：{system_lang}")