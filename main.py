#pypi.org package manager program by sc0nep

import lib.pypi as pypi
import lib.package as package
import lib.tui as tui
import time
import sys

#Program Starting
tui.intro_display('0.1 Alpha')

#Server Check
tui.window_lid('pypi_server check')
print('Server Checking...')
http_code = pypi.response_status('https://pypi.org')
if http_code == 200:
    print('\nServer working... Wellcome to ezPyPi!')
    time.sleep(1)
else:
    print('ErrorCode: %s' %http_code)
    print('[Program exit]')
    sys.exit()

#get pippath
tui.window_lid('Get pip path')
pip = package.Pip()
pip.get_path()

#MainMenu
while(True):
    tui.window_lid('MAIN MENU')
    print('PIP_path: %s' %pip.print_path())
    tui.main_menu()
    select = input('Type Number: ')
    if select == '1':
        tui.window_lid('Package Search')
        word = input('Type word: ')
        listpage = pypi.Pypi_listpage(word)
        search_result = listpage.print_searchresult()
        while(True):
            tui.window_lid('Package Selection')
            for i in search_result:
                print(i)
            item_select = input('\n[number + Enter] package info, [Enter] Back to Main menu \nInput: ')
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
                    info = '''name: %s
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
            else:
                break
    elif select == '2':
        print('test')
    elif select == '3':
        print('test')
    elif select == '4':
        print('test')
    elif select == '5':
        print('test')
    elif select == '6':
        break
    else:
        print('Please type correct number!')
        time.sleep(0.5)
    break