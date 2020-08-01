#pypi.org package manager program by sc0nep

import lib.package as package
import lib.tui as tui
import time
import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Program Starting
<<<<<<< HEAD
tui.intro_display('0.1 Beta 1')
=======
tui.intro_display()

#get pippath
tui.window_lid('Get pip path')
pip = package.Pip()
pip.get_path()

#check essential module
tui.window_lid('Check essential module')
pip.check_essential_module()
time.sleep(1)

import lib.pypi as pypi
>>>>>>> f52e2f315da69e7222f28a17f2e6f6569fd72100

#Server Check
tui.window_lid('pypi_server check')
print('Server Checking...')
http_code = pypi.response_status('https://pypi.org')
if http_code == 200:
    print('Server working... Wellcome to ezPyPi!')
    time.sleep(1)
else:
    print('ErrorCode: %s' %http_code)
    print('[Program exit]')
    sys.exit()

#MainMenu
while(True):
    tui.window_lid('MAIN MENU')
    print('\nPIP_path: %s\n' %pip.print_path())
    tui.main_menu()
    select = input('\nType Number: ')
    if select == '1':
        tui.window_lid('Package Search')
        word = input('[Type word or Type ENTER key back to main menu]\n Search: ')
        if word == '':
            continue
        else:
            listpage = pypi.Pypi_listpage(word)
            search_result = listpage.print_searchresult()
            while(True):
                tui.window_lid('Package Selection')
                for i in search_result:
                    print(i)
                item_select = input('\n[number + Enter] package info, [Enter] Back to Main menu \n Input: ')
                if item_select != '':
                    while(True):
                        #package info
                        singleitem = listpage.singleitem(int(item_select))
                        package_name = singleitem[0]
                        package_version = singleitem[1]
                        package_released = singleitem[2]
                        package_subtitle = singleitem[3]
                        package_homepage = ''
                        itempage = pypi.Pypi_itempage(package_name)
                        package_homepage = itempage.homepage_link()
                        itempage.get_markdown()
                        tui.window_lid('Package Info')
                        info = '''
name: %s
version: %s
released: %s
subtitle: %s
project_homepage: %s
''' %(package_name, package_version, package_released, package_subtitle, package_homepage)
                        print(info)
                        select_work = input('[1] Watch Description, [2] Release history, [3] Install [4] Back to Search result\nnum: ')
                        if select_work == '1':
                            itempage.webview_description()
                        elif select_work == '2':
                            tui.window_lid('%s - Version History' %package_name)
                            for i in itempage.release_history():
                                print(i)
                            back = input('\n[Type ENTER key for back to package info]')
                        elif select_work == '3':
                            tui.window_lid('Install ''%s'' package' %package_name)
                            pip.install(package_name)
                            back = input('\n[Type ENTER key for back to package info]')
                        elif select_work == '4':
                            break
                elif item_select == '':
                    break;
                else:
                    print('Please type correct number!')
                    time.sleep(0.5)
    elif select == '2':
        tui.window_lid('Direct Installation')
        word = input('[Type Package Name or Type ENTER key for back to main menu]\n Package Name: ')
        if word == '':
            continue
        else:
            pip.install(word)
            back = input('\n[Type ENTER key for back to main menu]')
    elif select == '3':
        tui.window_lid('Install using requirements.txt')
        word = input('[Type requirements.txt Path or Type ENTER key for back to main menu]\n Path: ')
        if word == '':
            continue
        else:
            pip.multi_install(word)
            back = input('\n[Type ENTER key for back to main menu]')
    elif select == '4':
        tui.window_lid('Package Remove')
        pip.list_installed()
        word = input('\n[Type package name for remove or Type ENTER key for back to main menu]\n Package Name: ')
        if word == '':
            continue
        else:
            pip.uninstall(word)
            tui.autoback()
    elif select == '5':
        tui.window_lid('Installed Package List')
        select = input('1. Print list with Version \n2. Print list only name\n\n[number + Enter] print package list, [Enter] Back to Main menu\n input: ')
        if select == '1':
            tui.window_lid('Installed Package List - With version')
            pip.list_installed(select)
        elif select == '2':
            tui.window_lid('Installed Package List - Only Name')
            for i in pip.list_installed(select):
                print(i)
        else:
            continue
        back = input('\n[Type ENTER key for back to main menu]')
    elif select == '6':
        tui.window_lid('export requirements.txt')
        print('exporting...\n')
        pip.export_requirement()
        time.sleep(0.3)
        print('\nSaved ezpypi/requirements.txt')
        back = input('\n[Type ENTER key for back to main menu]')
    elif select == '0':
        break
    elif select == '7':
        tui.window_lid('ezPYPI Info')
        tui.programinfo()
        back = input('\n[Type ENTER key for back to main menu]')
    else:
        print('Please type correct number!')
        time.sleep(0.5)