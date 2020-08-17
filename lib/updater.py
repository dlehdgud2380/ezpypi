from typing import ChainMap
from bs4 import BeautifulSoup
import requests
from requests.api import get
from tui import version

REALEASE_URL = 'https://github.com/dlehdgud2380/ezpypi/releases'
DOWNLOAD_URL = 'https://github.com/dlehdgud2380/ezpypi/releases/download/'
present_version = version()

class Updater:
    def __init__(self):
    #Get html source
        self.response = requests.get(REALEASE_URL)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.get_version = ''

    def __version_compare():
        if present_version == self.get_version:
            return 'newest version'
        else:
            return 'Need to update'
    def __get_title(self):
        get_data = self.soup.find('div', class_='f1 flex-auto min-width-0 text-normal').text
        return get_data.strip()
    def __get_changelog(self):
        log = []
        for i, v in enumerate(self.soup.find('div', class_='markdown-body').find_all('li')):
            log.append('%s. %s' %(i+1, (str(v.text))))
        return log


if __name__ == "__main__":
    a = Updater()
    title = a.get_title()
    log = a.get_changelog()
    print(title)
    print(log)

