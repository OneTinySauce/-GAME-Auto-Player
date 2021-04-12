import pyautogui, sys, time

#Class for a building upgrade queue
class UpgradeBuildings:
    
    #Function for upgrading a town hall
    def TownHall(self):
        buttonLocW1 = pyautogui.locateOnScreen('2_2_worker.png', confidence = 0.7)
        if buttonLocW1 != None:
            buttonLoc2 = pyautogui.locateOnScreen('TownHall.png', confidence = 0.7)
            if buttonLoc2 != None:
                buttonPoint = pyautogui.center(buttonLoc2)
                buttonX, buttonY = buttonPoint
                pyautogui.click(buttonX, buttonY)
            else:
                self.TownHall()
            time.sleep(4)
            buttonLoc3 = pyautogui.locateOnScreen('upgrade.png', confidence = 0.7)
            if buttonLoc3 != None:
                buttonPoint2 = pyautogui.center(buttonLoc3)
                buttonX1, buttonY2 = buttonPoint2
                pyautogui.click(buttonX1, buttonY2)
            else:
                self.TownHall()
            time.sleep(3)
            buttonLoc4 = pyautogui.locateOnScreen('twoK.png', confidence = 0.7)
            if buttonLoc4 != None:
                pyautogui.click()
            else:
                self.TownHall()
        else:
            pass
        
    #Function for upgrading a gold storage
    def GoldStorageUpgrade(self):
        buttonLoc2 = pyautogui.locateOnScreen('goldStorage.png', confidence = 0.6)
        if buttonLoc2 != None:
            buttonPoint = pyautogui.center(buttonLoc2)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX, buttonY)
        else:
            self.GoldStorageUpgrade()
        time.sleep(4)
        buttonLoc3 = pyautogui.locateOnScreen('upgrade.png', confidence = 0.7)
        if buttonLoc3 != None:
            buttonPoint2 = pyautogui.center(buttonLoc3)
            buttonX1, buttonY2 = buttonPoint2
            pyautogui.click(buttonX1, buttonY2)
        else:
            self.GoldStorageUpgrade()
        time.sleep(3)
        buttonLoc4 = pyautogui.locateOnScreen('sevenFifty.png', confidence = 0.7)
        if buttonLoc4 != None:
            pyautogui.click()
        else:
            self.GoldStorageUpgrade()
