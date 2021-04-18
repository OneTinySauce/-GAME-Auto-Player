import pyautogui, sys, time

#Class for collecting accumulated coins
class CoinCollectClass:
    def collectCoin(self):
        state = 'Failed'
        buttonLoc = pyautogui.locateOnScreen('coin.png', confidence = 0.7)
        while state == 'Failed':
            if buttonLoc != None:
                buttonPoint = pyautogui.center(buttonLoc)
                buttonX, buttonY = buttonPoint
                pyautogui.click(buttonX, buttonY)
            else:
                self.collectCoin()
            state = 'Passed'
        return state
