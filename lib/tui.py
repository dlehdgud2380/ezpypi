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

def intro_display(version):
    term_clear()
    text = '''
[Easy to use on Any OS]
            ______  __   __ ______   _____
            | ___ \ \ \ / / | ___ \ |_   _|
  ___  ____ | |_/ /  \ V /  | |_/ /   | |
 / _ \|_  / |  __/    \ /   |  __/    | |
|  __/ / /  | |       | |   | |      _| |_
 \___|/___| \_|       \_/   \_|      \___/ %s                              
''' %version
    print(text)
    time.sleep(2)

def window_lid(process):
    term_clear()
    text_lid = '''
----------------------------------------------------------
 %s
----------------------------------------------------------
    ''' %process
    print(text_lid)

def main_menu():
    print('\n1. Package Search\n2. Direct installation\n3. Install using requirements.txt\n4. Package Remove\n5. Installed Package List\n6. Exit\n')