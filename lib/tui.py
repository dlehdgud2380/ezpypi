#Printing result more visual in Terminal

import os
import platform
import time

def term_clear():
    user_os = platform.system()
    if user_os == 'Windows' :
        os.system('cls')
    else:
        os.system('clear')

def waiting():
    print('\n[Will back in 3 sec.]')
    time.sleep(3)

def intro_display():
    text = '''
[Easy to use on Any OS]
            ______  __   __ ______   _____
            | ___ \ \ \ / / | ___ \ |_   _|
  ___  ____ | |_/ /  \ V /  | |_/ /   | |
 / _ \|_  / |  __/    \ /   |  __/    | |
|  __/ / /  | |       | |   | |      _| |_
 \___|/___| \_|       \_/   \_|      \___/
                             Ver 0.1 Alpha                              
'''
    print(text)
    time.sleep(2)

def window_lid(process):
    text_lid = '''
----------------------------------------------------------
 %s
----------------------------------------------------------
    ''' %process
    print(text_lid)

def window_floor():
    text_floor = '''
|________________________________________________________|
    '''
    print(text_floor)


#Debug
if __name__ == "__main__":
    term_clear()
    window_lid('ezPypi - ver 0.1')
    intro_display()
    window_floor()