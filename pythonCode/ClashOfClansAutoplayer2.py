import pyautogui, sys, time
import UserInterFace
import CoinCollect
import ExlixirCollect
import GameClass
import PlayerClass

#Initiate UserInterface Class
class UIInit(UserInterFace.UI):
    pass

#Initiate Coin Collect
class CoinCollectInit(CoinCollect.CoinCollectClass):
    pass

#Initiate Elixir Collect
class ExlixirCoolectInit(ExlixirCollect.ExlixirCollectClass):
    pass

#Initiate Game Class
class GameClassInit(GameClass.GamePlayClass):
    pass

#Initiate Player Class
class PlayerClassInit(PlayerClass.PlayerInitiateClass):
    pass


while True:
       #Start up initiation
       if UIInit.returnOpt1 == 'OK':
            
           PlayerClassInit().WindowsClick()
           PlayerClassInit().NoxSearch()
           PlayerClassInit().GameButton()
           GameClassInit().enlargeScreen()
            
       else:
           break
            
       while True:
            #main loop to continously execute functions
        
            if UIInit.returnOpt2 == 'Collect Coin':
                CoinCollectInit().collectCoin()
                
            elif UIInit.returnOpt2 == 'Collect Elixir':
                ExlixirCoolectInit().collectElixir()
                
            elif UIInit.returnOpt2 == 'Collect All Resources':
                CoinCollectInit().collectCoin()
                ExlixirCoolectInit().collectElixir()
                
            else:
                BuildingUpgradeInit().TownHall()
                BuildingUpgradeInit().GoldStorageUpgrade()





