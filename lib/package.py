#package management library for install, uninstall, updatecheck

import os
import sys
import platform
import re
import lib.tui as tui
import time

user_os = platform.system()
get_path = os.path.dirname(sys.executable)

class Pip:
    def __init__(self):
        self.pip_path = ''
        self.package_list = []

    #Get pip path
    def get_path(self):
        print('[Found PIP path your computer]\n')
        if user_os == 'Windows':
            self.pip_path = get_path + '\\' + 'Scripts' +  '\\' + 'pip.exe'
        elif user_os != 'Windows':
            list_temp = []
            temp = os.popen('ls ' + get_path +'/pip*')
            for i, val in enumerate(temp):
                list_temp.append(val)
                print('%d. %s' %(i, val))
            while(True):
                select = input('Select pip: ')
                try:
                    if int(select) > len(list_temp)-1 or int(select) < 0 :
                        print('You type wrong number!\n')
                    else:
                        self.pip_path = list_temp[int(select)].strip()
                        break
                except:
                    print('You type wrong value!\n')
        else:
            print('Can`t find pip! Please install pip or change python path!')
            print('[Program exit]')
            sys.exit()

        #PIP PATH CHECK and custom pip path
        while(True):
            pip_check = input('\nYour pip path is %s \nRight? (Y/N) --> ' %self.pip_path)
            if pip_check == 'y':
                break
            elif pip_check == 'n':
                temp = input('\nPlease input your custom pip path!\n(If blank + ENTER, will use selected path)\n Path: ')
                if temp == '':
                    continue
                else:
                    self.pip_path = temp
                    continue
            else:
                print('You type wrong value!')
        
    #print your pip path
    def print_path(self):
        return self.pip_path

    #Administor
    def sudo(self):
        if user_os != 'Windows':
            return 'sudo'
        else:
            return ''

    #check essential module for this program
    def check_essential_module(self):
        tui.window_lid('Check essential module')
        print('Essential Moudle Checking... ',end='')
        p = re.compile('[a-zA-Z0-9 -]+')
        ESSENTAIL_MODULE = ['requests', 'bs4', 'pywebview']
        modulecheck = ['N', 'N', 'N']
        freeze = os.popen('%s %s freeze' %(self.sudo(), self.pip_path))
        for i in freeze:
            self.package_list.append(str.strip(p.findall(i)[0]))
        if ESSENTAIL_MODULE[0] in self.package_list:
            modulecheck[0] = 'Y'
        if ESSENTAIL_MODULE[1] in self.package_list:
            modulecheck[1] = 'Y'
        if ESSENTAIL_MODULE[2] in self.package_list:
            modulecheck[2] = 'Y'
        if modulecheck[0] == 'N' or modulecheck[1] == 'N' or modulecheck[2] == 'N':
            print('\n[Essential Module Status]\n')
            for i in range(0, len(ESSENTAIL_MODULE)):
                print('%s : %s' %(ESSENTAIL_MODULE[i], modulecheck[i]))
            #install essential modules
            while(True):
                if modulecheck[0] == 'N':
                    print('\nInstall requests module\n')
                    self.install('essential/requests-2.24.0-py2.py3-none-any.whl')
                    modulecheck[0] = 'Y'
                elif modulecheck[1] == 'N':
                    print('\nInstall beautifulsoup4 module\n')
                    self.install('essential/bs4-0.0.1.tar.gz')
                    modulecheck[1] = 'Y'
                elif modulecheck[2] == 'N':
                    print('\nInstall pywebview module\n')
                    self.install('essential/pywebview-3.3.2-py3-none-any.whl')
                    modulecheck[2] = 'Y'
                else:
                    print('\nEssential Modules are ready!')
                    break
            time.sleep(1)
        else:
            print('OK')
            pass

    #install
    def install(self, word):
        os.system('%s %s install %s' %(self.sudo(), self.pip_path, word))

    #uninstall
    def uninstall(self, word):
        os.system('%s %s uninstall %s' %(self.sudo(), self.pip_path, word))

    #installed
    def list_installed(self, mode):
        if int(mode) == 1:
            os.system('%s list' %self.pip_path)
        elif int(mode) == 2:
            return self.package_list

    #install using requirements.txt
    def multi_install(self, path):
        os.system('%s %s install -r %s' %(self.sudo(), self.pip_path, path))

    #requirements Export
    def export_requirement(self):
        os.system('%s %s freeze > requirements.txt' %(self.sudo(), self.pip_path))
'''
    #Upgrade Package
    def upgrade(self):
        os.system('%s list' %self.pip_path)
        target = input('\nType package name for upgrade: ')
        os.system('%s %s install --upgrade %s' %(self.sudo(), self.pip_path, word))
'''