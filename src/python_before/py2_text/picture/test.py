# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-30 12:08:37
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-07 22:09:59

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    print reg
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        print imgurl
         urllib.urlretrieve(imgurl,'%s.jpg' % x)
         x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)
