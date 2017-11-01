# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-12-04 22:35:24
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-07 17:15:49

import os
import re
import urllib2
import urllib
import requests
from bs4 import BeautifulSoup

urlurl = 'http://www.dbmeinv.com/'

path = os.getcwd()  # 获取当前路径
new_path = os.path.join(path, u'暴走漫画')  # 在当前路径中创建文件夹
if not os.path.isdir(new_path):
    os.mkdir(new_path)

req_header = {
    'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"',
}
urls = urllib2.Request(urlurl, None, req_header)
url = urllib.urlopen(urls)
soup = BeautifulSoup(url, 'lxml')
souplink = soup.find_all('img', class_='height_min')
page = 0
for i in souplink:
    urll = i['src']
    print urll
    m = urllib2.urlopen(urll).read()
    print m
    page += 1
'''
    f = open(u'暴走漫画' + 'one' + str(page), 'wb')
    f.write(m)
    f.close()
'''
