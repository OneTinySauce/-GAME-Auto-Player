import pyautogui, sys, time
import UserInterFace
import CoinCollect
import ExlixirCollect
import GameClass
import PlayerClass

from pymsgbox import alert, confirm
class UIInit(UserInterFace.UI):
    def __init__(self, class_a):
        self.returnOpt1 = class_a.returnOpt1
        self.returnOpt2 = class_a.returnOpt2

dev_1 = UserInterFace.UI()


while True:
       if dev_1.returnOpt1() == 'OK':
           dev_1.WindowsClick()
           dev_1.NoxSearch()
           dev_1.GameButton()
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





