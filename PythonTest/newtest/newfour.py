"""Created with IntelliJ by Django on 2020/11/22 15:11"""

import ssl
import os
import urllib.request
import requests
from bs4 import BeautifulSoup

# ssl._create_default_https_context = ssl._create_unverified_context
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; WOW64)'
           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 '
           'Safari/537.36',
           }
if not os.path.exists('./插画素材/'):
    os.mkdir('./插画素材/')
else:
    pass

url = 'https://www.tupianzj.com/meinv/mm/meizitu/'
html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, 'lxml')
images_data = soup.find('ul', class_='d1 ico3').find_all_next('li')
for image in images_data:
    images_url = image.find_all('img')
    for _ in images_url:
        print(_['src'], _['alt'])


urllib.request.urlretrieve(_['src'], './插画素材/' + _['alt'] + '.jpg')

