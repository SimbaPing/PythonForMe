# coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/'
html = urlopen(url)
bsObj = BeautifulSoup(html, "lxml")
ulList = bsObj.findAll('ul')

print(ulList)