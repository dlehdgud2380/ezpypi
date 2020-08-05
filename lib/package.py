# package management library for install, uninstall, updatecheck

import os
import platform
import re

user_os = platform.system()


class Pip:
    def __init__(self):
        self.pip_path = ''
        self.project_folder = ''

    # Get pip path from .venv/ or main system
    def get_path(self):
        while(True):
            venv_path = input('Input your python project folder path!\n(If you blank, it will use existing pip) \n Path: ')
            if user_os == 'Windows':
                if venv_path == '':
                    self.pip_path = os.popen('where pip').read().strip()
                else:
                    self.pip_path = os.popen('where /r ' + venv_path + ' pip').read().strip()
                    if self.pip_path == '':
                        print('Please input correct path!\n')
                        continue
            elif user_os != 'Windows':
                if venv_path == '':
                    self.pip_path = os.popen('which pip3').read().strip()
                else:
                    self.pip_path = os.popen('which ' + venv_path + '/' +'.venv' + '/' + 'bin' + '/' + 'pip').read().strip()
                    if self.pip_path == '':
                        print('Please input correct path!\n')
                        continue
            break

        # PIP PATH CHECK and custom pip path
        while(True):
            pip_check = input('\nYour pip path is %s \nRight? (Y/N) --> ' % self.pip_path)
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

    # print your pip path

    def print_path(self):
        return self.pip_path

    # Administor
    def sudo(self):
        if user_os != 'Windows':
            return 'sudo'
        else:
            return ''

    # install
    def install(self, word):
        os.system('%s %s install %s' % (self.sudo(), self.pip_path, word))

    # uninstall
    def uninstall(self, word):
        os.system('%s %s uninstall %s' % (self.sudo(), self.pip_path, word))

    # installed
    def list_installed(self, mode):
        if int(mode) == 1:
            os.system('%s list' % self.pip_path)
        elif int(mode) == 2:
            p = re.compile('[a-zA-Z0-9 -]+')
            freeze = os.popen('%s %s freeze' % (self.sudo(), self.pip_path))
            package_list = []
            for i in freeze:
                package_list.append(str.strip(p.findall(i)[0]))
            return package_list

    # install using requirements.txt
    def multi_install(self, path):
        os.system('%s %s install -r %s' % (self.sudo(), self.pip_path, path))

    # requirements Export
    def export_requirement(self):
        os.system('%s %s freeze > requirements.txt' % (self.sudo(), self.pip_path))
'''
    #Upgrade Package
    def upgrade(self):
        os.system('%s list' %self.pip_path)
        target = input('\nType package name for upgrade: ')
        os.system('%s %s install --upgrade %s' %(self.sudo(), self.pip_path, word))
'''