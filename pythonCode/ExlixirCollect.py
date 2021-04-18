import pyautogui, sys, time

#Class for collecting 
class ExlixirCollectClass:
    def collectElixir(self):
        state = 'Failed'
        buttonLoc = pyautogui.locateOnScreen('Elixir.png', confidence = 0.7)
        while state == 'Failed':
            if buttonLoc != None:
                buttonPoint = pyautogui.center(buttonLoc)
                buttonX, buttonY = buttonPoint
                pyautogui.click(buttonX, buttonY)
            else:
                self.collectElixir()
            state = 'Passed'
        return state
