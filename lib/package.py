#package management library for install, uninstall, updatecheck

import os
import sys
import platform

user_os = platform.system()
get_path = os.path.dirname(sys.executable)
pip_path = ''

#find pip location
if user_os == 'Windows':
    pip_path = get_path + '\\' + 'Scripts' +  '\\' + 'pip.exe'
else:
    list_temp = []
    temp = os.popen('ls ' + get_path +'/pip*')
    count_temp = 0
    for i in temp:
        list_temp.append(temp.readline())
        print('%d. + %s' %i %s)
    select = input(int('Select pip: '))
    pip_path = list_temp[select]

print(pip_path)

'''
class pip:

    #install

    #uninstall

    #installed

    #install using requirements.txt

    #Change Python root path
'''