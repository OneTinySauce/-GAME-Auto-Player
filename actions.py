import pyautogui as ag
import cv2

##Settings
#Determin confidence level
accurate = 0.9

##find on screen, move to and left click once
def findAndClick(file, confidenceLevel):
    location = ag.locateOnScreen(file, confidenceLevel)
    if location == None:
        return False
    ag.click(ag.moveTo(location))
    return True

##Collect gold and elixir
def collectResources():
    elixir = findAndClick('screenshots/ResourceElixir.png', accurate)
    gold = findAndClick('screenshots/ResourceGold.png', accurate)
    return elixir, gold