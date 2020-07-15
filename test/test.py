import requests
from bs4 import BeautifulSoup

address = 'https://pypi.org/project/beautifulsoup4/'
response = requests.get(address).text
soup = BeautifulSoup(response, 'html.parser')
get_md = soup.find('div', id="description")
description = []

#basecode
start_part = []
end_part = []
start_f = open("html_start", r).read()
end_f = open("html_end", r).read()
while true:
    for line in start_f:
        start_f.append(line)
    for line in end_f:
        end_f.append(line)

f = open("test/test.html", 'w')

for md in get_md:
    description.append(str(md))

for i in range(0, len(description)):
    f.write(description[i])
    print('%d line wrotten' %i)
f.close()