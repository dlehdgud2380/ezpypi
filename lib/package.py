#package management library for install, uninstall, updatecheck

import os
import sys
import platform

user_os = platform.system()
get_path = os.path.dirname(sys.executable)

class Pip:
    def __init__(self):
        self.pip_path = ''

    #Get pip path
    def get_path(self):
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
            print('Can`t find pip! Please install pip!')
            sys.exit()

        print('Your pip path is %s' %self.pip_path)


    #install
    def install(self, word):
        os.system('sudo %s install %s' %(self.pip_path, word))

    #uninstall
    def uninstall(self):
        os.system('%s list' %self.pip_path)
        target = input('\nType package name for uninstall: ')
        os.system('sudo %s uninstall %s' %(self.pip_path, target))

    #installed
    def list_installed(self):
        os.system('%s list' %self.pip_path)

    #install using requirements.txt
    def multi_install(self, path):
        os.system('sudo %s install -r %s' %(self.pip_path, path))

    #Upgrade Package
    def upgrade(self):
        os.system('%s list' %self.pip_path)
        target = input('\nType package name for upgrade: ')
        os.system('sudo %s uninstall %s' %(self.pip_path, target))