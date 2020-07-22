#package management library for install, uninstall, updatecheck

import os
import sys
import platform

user_os = platform.system()
get_path = os.path.dirname(sys.executable)

#find pip location

class Pip:
    def __init__(self):
        self.pip_path = ''

    def get_path(self):
        if user_os == 'Windows':
            self.pip_path = get_path + '\\' + 'Scripts' +  '\\' + 'pip.exe'
        else:
            list_temp = []
            temp = os.popen('ls ' + get_path +'/pip*')
            for i, val in enumerate(temp):
                list_temp.append(val)
                print('%d. %s' %(i, val))
            select = int(input('Select pip: '))
            self.pip_path = list_temp[select].strip()
            print('Your pip path is %s' %self.pip_path)

    #install
    def install(self, word):
        os.system('sudo %s install %s' %(self.pip_path, word))

    #uninstall
    def uninstall(self):
        os.system('%s list' %self.pip_path)
        target = input('Type package name for uninstall: ')
        os.system('sudo %s uninstall %s' %(self.pip_path, target))

    #installed
    def list_installed(self):
        os.system('%s list' %self.pip_path)

    #install using requirements.txt
    def multi_install(self, path):
        os.system('sudo %s install -r %s' %(self.pip_path, path))

#Debug
if __name__ == "__main__":
    a = Pip()
    a.get_path()
    while(True):
        menu = int(input('[Select Menu]\n\n1. Install\n2. uninstall\n3. Installed packages\n4. Install Package using requirement.txt\n\nnumber: '))
        if menu == 1:
            word = input('Type package name for install: ')
            a.install(word)
        elif menu == 2:
            a.uninstall()
        elif menu == 3:
            a.list_installed()
        elif menu == 4:
            word = input('Type requirement.txt path: ')
            a.multi_install()
        else:
            break