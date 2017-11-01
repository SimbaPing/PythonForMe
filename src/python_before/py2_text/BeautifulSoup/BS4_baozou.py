# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-11-26 12:18:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-07 17:12:35

from bs4 import BeautifulSoup
import os
import sys
import urllib2
import time
import random
import urllib
import requests
# 创建文件夹
path = os.getcwd()  # 获取当前路径
new_path = os.path.join(path, u'暴走漫画')  # 在当前路径中创建文件夹
if not os.path.isdir(new_path):
    os.mkdir(new_path)


def page_loop(page=1):
    urlurl = 'http://baozoumanhua.com/baoman'
    req_header = {
    'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"',
 }
    req_timeout = 5
    urll = urllib2.Request(urlurl, None, req_header)
    urlu = urllib2.urlopen(urll, None, req_timeout)
    content = urlu.read()
    soup = BeautifulSoup(content, 'lxml')
    my_girl = soup.find_all('img', class_="lazy")
    for girl in my_girl:
        link = girl.get('data-url')
        flink = urllib2.urlopen(link, None, req_timeout)
        print flink
        content2 = urllib2.urlopen(flink).read()
        print content2

        #with open(u'暴走漫画'+'/'+time.strftime('%H-%M-%S')+random.choice('qwertyuiopasdfghjklzxcvbnm')+flink[-5:],'wb') as code:          #在OSC上现学的
        with open(u'暴走漫画'+'/'+flink[-11:],'wb') as code:
            code.write(content2)

    page = int(page) + 1
    print u'开始抓取下一页'
    print 'the %s page' % page
    page_loop(page)

page_loop()
