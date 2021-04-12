import pyautogui, sys, time

#Class for collecting 
class ExlixirCollectClass:
    
    #Function for collecting elixir
    def collectElixir(self):
        buttonLoc = pyautogui.locateOnScreen('Elixir.png', confidence = 0.7)
        if buttonLoc != None:
            buttonPoint = pyautogui.center(buttonLoc)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX, buttonY)
        else:
            self.collectElixir()
