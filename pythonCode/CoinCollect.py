import pyautogui, sys, time

#Class for collecting accumulated coins
class CoinCollectClass:
    
    #Function for collecting coins
    def collectCoin(self):
        buttonLoc = pyautogui.locateOnScreen('coin.png', confidence = 0.7)
        if buttonLoc != None:
            buttonPoint = pyautogui.center(buttonLoc)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX, buttonY)
        else:
            self.collectCoin()
