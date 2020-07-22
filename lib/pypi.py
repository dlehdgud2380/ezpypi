#pypi scraping library

import os
import platform
import requests
from bs4 import BeautifulSoup
import webview

ADDRESS_PYPI = 'https://pypi.org/'
SEARCH = 'search/?q='
PROJECT = 'project/'
PAGE = '&page='

def clear_term():
    user_os = platform.system()
    if user_os == 'Windows' :
        os.system('cls')
    else:
        os.system('clear')

#check server response
def response_test(address):
    response = requests.get(address)
    if response != 200 :
        print ("Can't connect server")
        return response
    else :
        pass

#get html source
def get_html(address):
    html = requests.get(address).text
    return html

#parse pypi search result page
class Pypi_listpage:
    def __init__(self, word):
        if word == '':
            print('Please type correct word!')
        else:
            self.soup = BeautifulSoup(get_html(ADDRESS_PYPI + SEARCH + word), 'html.parser')

            #get package infos
            self.name = self.soup.find_all('span', class_='package-snippet__name')
            self.version = self.soup.find_all('span', class_='package-snippet__version')
            self.released = self.soup.find_all('span', class_='package-snippet__released')
            self.description = self.soup.find_all('p', class_='package-snippet__description')

            #listed item -> self.package_list[0: name, 1: version, 2: released, 3: description][item_number]
            self.package_list = [] 
            self.__data_listing()

    def __data_arrange(self, variable):
        arranged_data = [] 
        for i in variable:
            arranged_data.append(i.get_text(' ', strip=True))
        self.package_list.append(arranged_data)

    def __data_listing(self):
        arrange_order = [self.name, self.version, self.released, self.description]
        for i in range(0, len(arrange_order)):
            self.__data_arrange(arrange_order[i])

    def print_searchresult(self):
        for i in range(0, len(self.package_list[0])):
            print(str(i) + '. ' + self.package_list[0][i])

    def singleitem(self, itemnum):
        item_info = []
        for i in range(0, len(self.package_list)):
            item_info.append(self.package_list[i][itemnum])
        return item_info

#parse pypi single item page
class Pypi_itempage:
    def __init__(self, word):
        self.word = word
        self.soup = BeautifulSoup(get_html(ADDRESS_PYPI + PROJECT + word), 'html.parser')
        self.xmlsoup = BeautifulSoup(get_html(ADDRESS_PYPI + 'rss/' + PROJECT + word + '/' + 'releases.xml'), "html.parser")
    def release_history(self):
        version_history = []
        for version in self.xmlsoup.find_all('item'):
            version_history.append(str(version.title.text))
            print(version.title.text)
        return version_history
    def homepage_link(self):
        try:
            link = self.soup.find('a', class_='vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed').attrs['href']
            print(link)
        except e:
            print('Can`t found homepage link!')
    def webview_description(self):
        description = []
        start_part = []
        end_part = []
        get_md = self.soup.find('div', id="description")

        #base setting
        start_f = open("lib/asset/html_start.txt", 'r').read()
        end_f = open("lib/asset/html_end.txt", 'r').read()
        for line in start_f:
            start_part.append(line)
        for line in end_f:
            end_part.append(line)
        f = open("lib/description.html", 'w')

        #Assemble data
        for i in range(0, len(start_part)):
            description.append(start_part[i])
        for md in get_md:
            description.append(str(md))
        for i in range(0, len(end_part)):
            description.append(end_part[i])

        #Write Html
        for i in range(0, len(description)):
            f.write(description[i])
        f.close()

        #open Webview
        window = webview.create_window(self.word + ' ' + self.release_history()[0] , "description.html")
        webview.start()

 #Debug
if __name__ == "__main__":
    clear_term()
    print("Wellcome To Pypi \n\n\n\n\n")
    word = input("Search Projects: ")
    clear_term()
    a = Pypi_listpage(word)
    a.print_searchresult()
    select = input("select number: ")
    clear_term()
    ab = Pypi_itempage(a.singleitem(int(select))[0])
    ab.release_history()
    ab.homepage_link()
    ab.webview_description()