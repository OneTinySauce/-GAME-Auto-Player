import pyautogui, sys, time
from pymsgbox import alert, confirm

class UI:
        returnOpt1 = confirm(text='Thank you for using Clash of Clans Auto Player! \n'
                         'You are about to ace this game! \n'
                        'Click OK to continue \n'
                       'Click Cancel to exit', title='ClashOfClans', buttons=['OK', 'Cancel'])

        #Intentional Failure to break the execution
        if returnOpt1 == 'OK':
            returnOpt2 = confirm(text='Click on one of the Options', title='Action',
                                 buttons=['Collect Coin', 'Collect Elixir', 'Collect All Resources',
                                          'Upgrade Buildings'])
