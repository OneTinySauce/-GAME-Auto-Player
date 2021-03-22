import pyautogui, sys, time
from pymsgbox import alert, confirm

# Find windows icon and click on.
def WindowsClick():
    buttonLoc = pyautogui.locateOnScreen('windowsButton.png')
    buttonPoint = pyautogui.center(buttonLoc)
    buttonX, buttonY = buttonPoint
    pyautogui.click(buttonX, buttonY)

# Simple search for Noxx Emulator, the clikcs to launch.
def NoxSearch():
    pyautogui.write('Nox', interval=0.08)
    pyautogui.press('enter')
    
# Find and click on clash of clans icon to launch game.
# Uses recursion in case of system delay to retry until success.
def GameButton():
    buttonLoc = pyautogui.locateOnScreen('ClashOfClansApp.png')
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        GameButton()
        
# Scrolls out to fit screen to max size.
# Once again, extra scrolling for redundancy and possible system lag.
def enlargeScreen():
    time.sleep(6)
    temp = 0
    while temp < 5:
        pyautogui.keyDown('ctrl')
        pyautogui.press('0')
        pyautogui.scroll(-15)
        temp = temp + 1
pyautogui.keyUp('ctrl')

# Recursive Function to find and click on elixir icons to collect
# Uses confidence - may have to be revisisted if game colors/resolutions
# differ between users.
def collectElixir():
    buttonLoc = pyautogui.locateOnScreen('Elixir.png', confidence = 0.7)
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        collectElixir()
        
# Recursive Function to find and click on coin icons to collect
# Uses confidence - may have to be revisisted if game colors/resolutions
# differ between users.
def collectCoin():
    buttonLoc = pyautogui.locateOnScreen('coin.png', confidence = 0.7)
    if buttonLoc != None:
        buttonPoint = pyautogui.center(buttonLoc)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
    else:
        collectCoin()

# Code for the structure of the entry UI window
returnOpt1 = confirm(text='Thank you for using Clash of Clans Auto Player! \n'
                 'You are about to ace this game! \n'
                 'Click OK to continue \n'
                 'Click Cancel to exit', title='ClashOfClans', buttons=['OK', 'Cancel'])

# Code for the structure of the collection settings - allows enablment of certain resources to collect
returnOpt2 = confirm(text='Click on one of the Options', title='Action', buttons=['Collect Coin', 'Collect Elixir', 'CollectAllResources'])

# Main start up function and loop to run resource collection automatically
while True:
       if returnOpt1 == 'OK':
           WindowsClick()
           NoxSearch()
           GameButton()
           enlargeScreen()
       else:
           break
            
       # Resource collection loop
       while True:
            if returnOpt2 == 'Collect Coin':
                collectCoin()
            elif returnOpt2 == 'Collect Elixir':
                collectElixir()
            else:
                collectCoin()
                collectElixir()
