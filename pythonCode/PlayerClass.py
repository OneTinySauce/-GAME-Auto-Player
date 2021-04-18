import pyautogui, sys, time
class PlayerInitiateClass:

    def WindowsClick(self):
        buttonLoc = pyautogui.locateOnScreen('windowsButton.png')
        if (buttonLoc != None):
            buttonPoint = pyautogui.center(buttonLoc)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX, buttonY)
            return 'Passed'
        else:
            return 'Failed'

    def NoxSearch(self):
        (pyautogui.write('Nox', interval=0.25))
        (pyautogui.press('enter'))

    def GameButton(self):
        state = 'Failed'
        buttonLoc = pyautogui.locateOnScreen('ClashOfClansApp.png', confidence=0.7)
        while state == 'Failed':
            if buttonLoc != None:
                buttonPoint = pyautogui.center(buttonLoc)
                buttonX, buttonY = buttonPoint
                pyautogui.click(buttonX, buttonY)
            else:
                self.GameButton()
            state = 'Passed'
        return state
