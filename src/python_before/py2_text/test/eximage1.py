# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-06 20:51:48
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-06 22:34:32

from PIL import  Image
im = Image.open('06.jpg')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('06.png', 'PNG')
