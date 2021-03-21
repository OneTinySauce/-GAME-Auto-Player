import pyautogui, sys, time
from pymsgbox import alert, confirm

def WindowsClick():
    buttonLoc = pyautogui.locateOnScreen('windowsButton.png')
    buttonPoint = pyautogui.center(buttonLoc)
    buttonX, buttonY = buttonPoint
    pyautogui.click(buttonX, buttonY)

def NoxSearch():
    pyautogui.write('Nox', interval=0.08)
    pyautogui.press('enter')
def GameButton():
    buttonLoc = pyautogui.locateOnScreen('ClashOfClansApp.png')
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        GameButton()
def enlargeScreen():
    time.sleep(6)
    temp = 0
    while temp < 5:
        pyautogui.keyDown('ctrl')
        pyautogui.press('0')
        pyautogui.scroll(-15)
        temp = temp + 1
pyautogui.keyUp('ctrl')
def collectElixir():
    buttonLoc = pyautogui.locateOnScreen('Elixir.png', confidence = 0.7)
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        collectElixir()
def collectCoin():
    buttonLoc = pyautogui.locateOnScreen('coin.png', confidence = 0.7)
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        collectCoin()

returnOpt1 = confirm(text='Thank you for using Clash of Clans Auto Player! \n'
                 'You are about to ace this game! \n'
                 'Click OK to continue \n'
                 'Click Cancel to exit', title='ClashOfClans', buttons=['OK', 'Cancel'])
returnOpt2 = confirm(text='Click on one of the Options', title='Action', buttons=['Collect Coin', 'Collect Elixir', 'CollectAllResources'])
while True:
       if returnOpt1 == 'OK':
           WindowsClick()
           NoxSearch()
           GameButton()
           enlargeScreen()
       else:
           break
       while True:
            if returnOpt2 == 'Collect Coin':
                collectCoin()
            elif returnOpt2 == 'Collect Elixir':
                collectElixir()
            else:
                collectCoin()
                collectElixir()
