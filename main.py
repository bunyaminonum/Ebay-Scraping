import requests
from bs4 import BeautifulSoup


def parcala(string):
    par = string.split('/')
    if 'itm' in par:
        return par

r = requests.get('https://www.ebay.co.uk/sch/171146/i.html?_from=R40&_nkw=dress&LH_TitleDesc=0')
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.findAll('a')
linklist = []
for i in a:
    href = i.get('href')
    parcala = href.split('/')
    if 'itm' in parcala:
        linklist.append(href)

for b in linklist:
    r = requests.get(b)
    soup = BeautifulSoup(r.content, 'html.parser')
    price = soup.findAll('div', {'class':'mainPrice'})
    for prc in price:
        print(prc.get_text(), b)
