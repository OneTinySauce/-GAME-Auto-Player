import pyautogui, sys, time


class PlayerInitiateClass:

    def WindowsClick(self):
        buttonLoc = pyautogui.locateOnScreen('windowsButton.png')
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)

    def NoxSearch(self):
        pyautogui.write('Nox', interval=0.25)
        pyautogui.press('enter')

    def GameButton(self):
        buttonLoc = pyautogui.locateOnScreen('ClashOfClansApp.png')
        if buttonLoc != None:
           buttonPoint = pyautogui.center(buttonLoc)
           buttonX, buttonY = buttonPoint
           pyautogui.click(buttonX, buttonY)
        else:
           self.GameButton()