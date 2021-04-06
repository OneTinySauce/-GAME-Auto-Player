import pyautogui, sys, time
from pymsgbox import alert, confirm

class UI:
    def __init__(self):
        self.returnOpt1 = confirm(text='Thank you for using Clash of Clans Auto Player! \n'
                         'You are about to ace this game! \n'
                        'Click OK to continue \n'
                       'Click Cancel to exit', title='ClashOfClans', buttons=['OK', 'Cancel'])
        self.returnOpt2 = confirm(text='Click on one of the Options', title='Action', buttons=['Collect Coin', 'Collect Elixir', 'CollectAllResources'])

    def returnOpt1(self):
        return self.returnOpt1

    def returnOpt2(self):
        return self.returnOpt2