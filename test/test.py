import requests
from bs4 import BeautifulSoup
import webview

address = 'https://pypi.org/project/beautifulsoup4/'
response = requests.get(address).text
soup = BeautifulSoup(response, 'html.parser')
get_md = soup.find('div', id="description")
description = []

#basecode
start_part = []
end_part = []
start_f = open("test/html_start.txt", 'r').read()
end_f = open("test/html_end.txt", 'r').read()
for line in start_f:
    start_part.append(line)
for line in end_f:
    end_part.append(line)

f = open("test/test.html", 'w')

for i in range(0, len(start_part)):
    description.append(start_part[i])

for md in get_md:
    description.append(str(md))

for i in range(0, len(end_part)):
    description.append(end_part[i])

for i in range(0, len(description)):
    f.write(description[i])
    print('%d line wrotten' %i)
f.close()

window = webview.create_window('Description', 'test.html')
webview.start()