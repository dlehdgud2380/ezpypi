from bs4 import BeautifulSoup
import requests
from lib.tui import version
import platform
import wget
import zipfile
import os

user_os = platform.system()
URL = 'https://github.com'
REALEASE = '/dlehdgud2380/ezpypi/releases'
present_version = version()

class Update_checker:
    def __init__(self):
        #Get html source
        self.response = requests.get(URL+REALEASE)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        #get version from github
        self.get_version = self.soup.find('div', class_='f1 flex-auto min-width-0 text-normal').text[8:-1]
        print('present_version: %s \nlatest_version: %s' %(present_version, self.get_version))
        if self.version_compare() == 0:
            print('\nThis program version is latest version. No Update!')
        else:
            print('\nUpdate released!\n\n[ChangeLog]')
            for i in self.__get_changelog():
                print(i)

    def version_compare(self):
        if present_version == self.get_version or present_version > self.get_version:
            return 0
        else:
            return 1
    def __get_changelog(self):
        log = []
        for i, v in enumerate(self.soup.find('div', class_='markdown-body').find_all('li')):
            log.append('%s. %s' %(i+1, (str(v.text))))
        return log
    def get_downloadinfo(self):
        files = []
        file_link = []
        for i in self.soup.find('div', class_='Box Box--condensed mt-3').find_all('a', class_ ='d-flex flex-items-center min-width-0'):
            files.append(i.text.strip())
            file_link.append('%s%s' %(URL, i.attrs['href'].strip()))
        if user_os == 'Windows':
            while(True):
                select_mod = input('Select mod for download!\n(1) ezpypi.exe\n(2) ezpypi project folder\n --> ')
                if select_mod == '1' :
                    return files[1], file_link[1]
                elif select_mod == '2' :
                    return files[0], file_link[0]
                else:
                    print('Please input correct number!')
        else:
            return files[0], file_link[0]
            
def updater(url, filename):
    wget.download(url, out='.')
    print('extracting...')
    update_file = zipfile.ZipFile('.\\%s' %filename)
    update_file.extractall('.')
    os.remove(filename)
    update_file.close()