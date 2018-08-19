# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
.....author: Ping
....contact: uppjs@qq.com
.......file: pic1.py
.......time: 2018/06/17 21:45:40
Created with Visual Studio Code.
description:
'''

from PIL import Image

im = Image.open('C:\\Users\\pjs\\GitHub\\learnpython\\mypic.jpg')

w, h = im.size

im.thumbnail((w//2, h//2))
im.save('C:\\Users\\pjs\\GitHub\\learnpython\\my.jpg')