#Printing result more visual in Terminal
#Only for ezPYPI

import os
import platform
import time

INTROTEXT = '''            ______  __   __ ______   _____
            | ___ \ \ \ / / | ___ \ |_   _|
  ___  ____ | |_/ /  \ V /  | |_/ /   | |
 / _ \|_  / |  __/    \ /   |  __/    | |
|  __/ / /  | |       | |   | |      _| |_
 \___|/___| \_|       \_/   \_|      \___/
<-- Easy to use on Any OS -->
'''
APP_VERSION = '0.1 Beta 2'

def term_clear():
    user_os = platform.system()
    if user_os == 'Windows' :
        os.system('cls')
    else:
        os.system('clear')

def autoback():
    print('\n[Will back in 3 sec.]')
    time.sleep(3)

def version():
    return APP_VERSION

def intro_display():
    term_clear()
    print('%s-------------------------------------------- \n%s' %(INTROTEXT, version()))
    time.sleep(2)

def window_lid(process):
    term_clear()
    text_lid = '''
-------------------------------------------------------------------
 %s
-------------------------------------------------------------------''' %(process)
    print(text_lid)

def programinfo():
    info = '''%s
Version: %s
------------------------------------------------------------------
[Developer Info]

Name: LeeDongHyeong
mail: sc0_nep@yahoo.co.jp
Github: https://github.com/dlehdgud2380

BUG REPORT PLEASE!! ''' %(INTROTEXT, version())
    print(info)

def main_menu():
    menu = ['1. PYPI Search', '2. Direct installation', '3. Install using requirements.txt', '4. Package Remove', '5. Installed Package List', '6. export reqirements.txt', '7. ezPYPI Info', '0. Exit']
    for i in menu:
        print(i)