import pyautogui

import threading

def click():
    threading.Timer(1200.0, click).start()
    pyautogui.moveTo(362, 733)
    pyautogui.click()

click()


