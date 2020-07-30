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
            print('[Found PIP path your computer]\n')
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
            print('[Program exit]')
            sys.exit()

        print('Your pip path is %s' %self.pip_path)
        
    #print your pip path
    def print_path(self):
        return self.pip_path

    #Administor
    def sudo(self):
        if user_os != 'Windows':
            return 'sudo'
        else:
            return ''

    #install
    def install(self, word):
        os.system('%s %s install %s' %(self.sudo(), self.pip_path, word))

    #uninstall
    def uninstall(self, word):
        os.system('%s %s uninstall %s' %(self.sudo(), self.pip_path, word))

    #installed
    def list_installed(self):
        os.system('%s list' %self.pip_path)

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