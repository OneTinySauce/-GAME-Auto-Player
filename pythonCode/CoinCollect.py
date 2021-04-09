import pyautogui, sys, time

class CoinCollectClass:
    def collectCoin(self):
        buttonLoc = pyautogui.locateOnScreen('coin.png', confidence = 0.7)
        if buttonLoc != None:
            buttonPoint = pyautogui.center(buttonLoc)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX, buttonY)
        else:
            self.collectCoin()