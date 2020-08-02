#pypi.org package manager program by sc0nep

import lib.tui as tui
import lib.package as package
import time
import urllib.request
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Program Starting
tui.intro_display()

#get pippath
tui.window_lid('Get pip path')
pip = package.Pip()
pip.get_path()

#check essential module
pip.check_essential_module()

try:
    urllib.request.urlopen('https://pypi.org/', timeout=3)
    import lib.pypi as pypi
    mode = 'Online'
except Exception:
    mode = 'Offline'

#MainMenu
while(True):
    tui.window_lid('MAIN MENU')
    #pip_path, PYPI Server status
    print('\nPIP_path: %s' %pip.print_path())
    if mode == 'Offline':
        print('PYPI Server Status: %s - You can`t use PYPI Search\n' %mode)
    else:
        pypi_status = pypi.server_response('https://pypi.org/').status_code
        if pypi_status == 200:
            print('PYPI Server Status:  %s / %s\n' %(mode, pypi_status))
        else:
            print('PYPI Server Status: %s / %s - You can`t use PYPI Search%s\n' %(mode, pypi_status))
    tui.main_menu()
    select = input('\nType Number: ')
    if select == '1':
        tui.window_lid('PYPI Search')
        if mode == 'Offline' or pypi_status != 200:
            print('You can`t use PYPI Search! It can only use on online and server response 200!')
            print('Please check PYPI Server Status!!')
            tui.autoback()
            continue
        else:
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
                            select_work = input('[1] Watch Description, [2] Release history, [3] Install, [Blank + ENTER] Back to Search result\nnum: ')
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
                            else:
                                break
                    elif item_select == '':
                        os.remove('lib/description.html')
                        break
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
        pip.list_installed(1)
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