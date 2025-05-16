import pyautogui
import time
from datetime import datetime

numMin = 1
pyautogui.FAILSAFE = False

while True:
    pyautogui.moveTo(10, 10, 2)
    pyautogui.moveTo(20, 20, 2)
    pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
    time.sleep(numMin * 60)
