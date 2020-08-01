#package management library for install, uninstall, updatecheck

import os
import sys
import platform
import re

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
                select = int(input('Select pip: '))
                if select > len(list_temp)-1 or select < 0 :
                    print('You type wrong number!')
                else:
                    self.pip_path = list_temp[select].strip()
                    break
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
        p = re.compile('[a-zA-Z0-9 -]+')
        ESSENTAIL_MODULE = ['requests', 'beautifulsoup4', 'pywebview']
        modulecheck = ['N', 'N', 'N']
        freeze = os.popen('%s %s freeze' %(self.sudo(), self.pip_path))
        for i in freeze:
            temp = p.findall(i)[0]
            self.package_list.append(temp)
            if temp == ESSENTAIL_MODULE[0]:
                modulecheck[0] = 'Y'
            elif temp == ESSENTAIL_MODULE[1]:
                modulecheck[1] = 'Y'
            elif temp == ESSENTAIL_MODULE[2]:
                modulecheck[2] = 'Y'
            else:
                continue
        print('[Essential Module Status]\n')
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
                self.install('essential/beautifulsoup4-4.9.1-py3-none-any.whl')
                modulecheck[1] = 'Y'
            elif modulecheck[2] == 'N':
                print('\nInstall pywebview module\n')
                self.install('essential/pywebview-3.3.2-py3-none-any.whl')
                modulecheck[2] = 'Y'
            else:
                print('\nEssential Modules are ready!')
                break

    #install
    def install(self, word):
        os.system('%s %s install %s' %(self.sudo(), self.pip_path, word))

    #uninstall
    def uninstall(self, word):
        os.system('%s %s uninstall %s' %(self.sudo(), self.pip_path, word))

    #installed
    def list_installed(self, mode):
        if mode == '1':
            os.system('%s list' %self.pip_path)
        elif mode == '2':
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
        os.system('sudo %s uninstall %s' %(self.pip_path, target))
'''