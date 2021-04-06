import pyautogui, sys, time

class GamePlayClass:
    def enlargeScreen(self):
       time.sleep(6)
       temp = 0
       while temp < 5:
         pyautogui.keyDown('ctrl')
         pyautogui.press('0')
         pyautogui.scroll(-15)
         temp = temp + 1
    pyautogui.keyUp('ctrl')