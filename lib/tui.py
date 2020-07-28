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

def autoback():
    print('\n[Will back in 3 sec.]')
    time.sleep(3)

def intro_display(version):
    term_clear()
    text = '''
            ______  __   __ ______   _____
            | ___ \ \ \ / / | ___ \ |_   _|
  ___  ____ | |_/ /  \ V /  | |_/ /   | |
 / _ \|_  / |  __/    \ /   |  __/    | |
|  __/ / /  | |       | |   | |      _| |_
 \___|/___| \_|       \_/   \_|      \___/ %s
<--Easy to use on Any OS-->
''' %version
    print(text)
    time.sleep(2)

def window_lid(process):
    term_clear()
    text_lid = '''
                                           ezPYPI 0.1 Alpha
-----------------------------------------------------------
 %s
-----------------------------------------------------------''' %process
    print(text_lid)

def programinfo():
    info = '''
            ______  __   __ ______   _____
            | ___ \ \ \ / / | ___ \ |_   _|
  ___  ____ | |_/ /  \ V /  | |_/ /   | |
 / _ \|_  / |  __/    \ /   |  __/    | |
|  __/ / /  | |       | |   | |      _| |_
 \___|/___| \_|       \_/   \_|      \___/ 0.1 Alpha
 <--Easy to use on Any OS-->

----------------------------------------------------------
[Developer Info]

Name: LeeDongHyeong
mail: sc0_nep@yahoo.co.jp
Github: https://github.com/dlehdgud2380

BUG REPORT PLEASE!! '''
    print(info)

def main_menu():
    menu = ['1. Package Search', '2. Direct installation', '3. Install using requirements.txt', '4. Package Remove', '5. Installed Package List', '6. export reqirements.txt', '7. ezPYPI Info', '0. Exit']
    for i in menu:
        print(i)