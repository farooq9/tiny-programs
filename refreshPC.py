#program to refresh pc 10 times
import pyautogui
from time import *
#delet the 10 and # in below line to take the input
num = 10 #int(input('How many time you want to refresh?: '))
sleep(4)
pyautogui.hotkey('win', 'd')
for i in range(num):
    pyautogui.rightClick(920, 256)
    pyautogui.press('down')
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
