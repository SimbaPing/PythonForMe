#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: pic4
.......date: 2018/8/21 22:47
created with IntelliJ IDEA
description:
"""
from PIL import Image

img = Image.open("10.jpg")
x = img.size[0]
y = img.size[1]
print(x)
print(y)
x_s = 100
y_s = int(y * x_s / x)
print(y_s)
rxy = (x_s, y_s)
print(rxy)
out = img.resize(rxy)
out.save("re-10.jpg")
