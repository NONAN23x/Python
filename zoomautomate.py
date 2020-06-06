import time, datetime
import pyautogui
import subprocess

#Point(x=604, y=50)//Search Bar
#Point(x=686, y=382)//zoombuttom

pyautogui.hotkey('winleft')
time.sleep(4)
pyautogui.typewrite("zoom", 0.5)
pyautogui.hotkey("enter")
time.sleep(8)
pyautogui.moveTo(686, 382, 0.4)
pyautogui.click()
time.sleep(7)  # Time delay for entering pass
entry = ""  # put your Zoom id here
pyautogui.typewrite(entry, 0.4)  # Point(x=528, y=507)//Video Turn off(essential)
pyautogui.moveTo(528, 507, 1)
pyautogui.click()
pyautogui.moveTo(726, 542)  # Point(x=726, y=547)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite("", 0.2)  # and pass here
time.sleep(0.2)
pyautogui.hotkey('enter')
time.sleep(6)
pyautogui.click(x=925, y=230)
time.sleep(0.5)
pyautogui.click(x=884, y=309)

def take_scrn():
    i = 1
    while i < 60:
        time.sleep(1)
        pyautogui.hotkey('winleft', 'Fn', 'Prntscrn')
        time.sleep(2*60)
        i += 1
take_scrn()


