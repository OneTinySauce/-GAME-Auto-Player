import pyautogui, sys, time
import UserInterFace
import CoinCollect
import ExlixirCollect
import GameClass
import PlayerClass

class UIInit(UserInterFace.UI):
    pass


class CoinCollectInit(CoinCollect.CoinCollectClass):
    pass

class ExlixirCoolectInit(ExlixirCollect.ExlixirCollectClass):
    pass

class GameClassInit(GameClass.GamePlayClass):
    pass
class PlayerClassInit(PlayerClass.PlayerInitiateClass):
    pass


while True:
       if UIInit.returnOpt1 == 'OK':
           PlayerClassInit().WindowsClick()
           PlayerClassInit().NoxSearch()
           PlayerClassInit().GameButton()
           GameClassInit().enlargeScreen()
       else:
           break
       while True:
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





