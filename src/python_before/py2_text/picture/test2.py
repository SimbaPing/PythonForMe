# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-12-07 20:29:33
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-08 20:34:00

import urllib.request
import re, os
from bs4 import BeautifulSoup

url = "http://jandan.net/ooxx/page-2257#comments"

path = os.getcwd()  # 获取当前路径
new_path = os.path.join(path, u'暴走漫画')  # 在当前路径中创建文件夹
if not os.path.isdir(new_path):
    os.mkdir(new_path)

req_header = {
    'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"',
}
urls = urllib.request(url, None, req_header)

html = urllib2.urlopen(urls)
soup = BeautifulSoup(html, 'lxml')
pics = soup.find_all('img')
print(pics)
x = 0
os.chdir(u'暴走漫画')
for pic in pics:
    imgurl = pic['src']
    urllib.urlretrieve(imgurl, '%s.jpg' % x)
    x += 1
