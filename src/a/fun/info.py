import requests
from bs4 import BeautifulSoup

def getCharacters(start):
    url="https://en.wikipedia.org/wiki/List_of_Marvel_Comics_characters:_%s"%start
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    soup.prettify()
    d=[]
    for i in soup.find_all("span",class_="mw-headline"):
        k=i.text
        d.append(k)
        e=d[1:]
    return e


def getCharacterImage(name):
    url="https://en.wikipedia.org/wiki/%s"%name
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    soup.prettify()
    k=0
    for i in soup.find_all("img"):
        if k==1:
            d=i['src']
            break
        k=k+1
    return d
