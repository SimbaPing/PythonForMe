# -*- coding:utf-8 -*-

import re
import urllib.request
import os

os.mkdir('pic1')  # 创建这个文件夹，如果已经创建就报错


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


# ------ getHtml()内输入任意帖子的URL ------
html = getHtml("http://jandan.net/pic/page-227#comments")
# ------ 修改html对象内的字符编码为UTF-8 ------
html = html.decode('UTF-8')


def getImg(html):
    reg = r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


imgList = getImg(html)
imgName = 0
for imgPath in imgList:
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    f = open("pic/" + str(imgName) + ".jpg", 'wb')
    f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    imgName += 1

print("All Done!")
