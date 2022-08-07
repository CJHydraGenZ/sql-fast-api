from pydoc import cli
import pyautogui
from time import sleep
import random
import keyboard


def picPos():
    print(pyautogui.position())
    # print(pyautogui.displayMousePosition())


# # print(pyautogui.displayMousePosition())
# print(pyautogui.size())


# def mouseMove():
#     randomX = random.randint(100, 800)
#     randomY = random.randint(100, 800)word
#     pyautogui.moveTo(randomX, randomY)
#     # pyautogui.moveTo(0, 767)
#     print(pyautogui.position())


# def mouseClick():
#     pyautogui.click()


def mouseMove(x, y):
    pyautogui.moveTo(x, y)
    # pyautogui.moveTo(0, 767)
    print(pyautogui.position())


def click():
    pyautogui.click()


def typeWrite(text):
    pyautogui.typewrite(text)


def enterKeyboard():
    pyautogui.press('enter')


mouseMove(200, 750)
# 676 404
click()
typeWrite('word')
enterKeyboard()
sleep(2)
enterKeyboard()
typeWrite('INI ADALAHA BOT')
mouseMove(1349, 0)
click()
mouseMove(676, 404)
click()
# click()
# enterKeyboard()
# while keyboard.is_pressed('q') == False:
#     picPos()

# mouseMove()
# mouseClick()
# sleep(0.5)
# 1349
