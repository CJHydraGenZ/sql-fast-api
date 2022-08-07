from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# Here is the click function:

print(pyautogui.displayMousePosition())


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
