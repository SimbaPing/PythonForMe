# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-11-06 12:20:59
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-06 12:36:20
import urllib
import re


def getHtml(url):  # 获取网页
    page = urllib.urlopen(url)  # 打开一个URL地址
    html = page.read()  # 读取page数据
    return html


def getImg(html):  # 获取图片
    reg = r'src="(.+?\.jpg)"pic_ext'
    imgre = re.compile(reg)  # 把正则表达式编译成一个正则表达式对象
    imglist = re.findall(imgre, html)  # 读取HTML中包含imgre的数据
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)
