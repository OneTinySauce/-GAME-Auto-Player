import pyautogui, sys, time

def WindowsClick():
    buttonLoc = pyautogui.locateOnScreen('windowsButton.png')
    buttonPoint = pyautogui.center(buttonLoc)
    buttonX, buttonY = buttonPoint
    pyautogui.click(buttonX, buttonY)

def vrBoxSearch():
    pyautogui.write('Virtual Box', interval=0.08)
    pyautogui.press('enter')
def andButton():
    buttonLoc = pyautogui.locateOnScreen('sButton.png')
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        andButton()
def openGame():
        buttonLoc = pyautogui.locateOnScreen('clashApp.png')
        if buttonLoc != None:
            buttonPoint = pyautogui.center(buttonLoc)
            buttonX, buttonY = buttonPoint
            pyautogui.moveTo(buttonX, buttonY)
            pyautogui.click(clicks=3, interval=0.25)
        else:
            openGame()

WindowsClick()
vrBoxSearch()
andButton()
openGame()
