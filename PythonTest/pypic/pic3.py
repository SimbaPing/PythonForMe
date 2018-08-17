#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: pic3
.......date: 2018/8/17 15:50
created with IntelliJ IDEA
description:
"""

from PIL import Image

# 打开
im = Image.open('10.jpg')  # 打开图片
# im.show()  # 展示图片 真打开

# 保存，保存为其他格式
im.save("100.png")  # 另存为某格式
im = Image.open("100.png")
# im.show()

# format
print(im.format)  # 打印照片格式 例如 JPEG PNG

# mode
print(im.mode)  # 打印照片模式 例如 RGB CMYK

# convert
im_con = im.convert('CMYK')  # 将图片转换模式 还有一种 im.convert(mode, matrix)
print(im_con.mode)

# size
print(im.size)  # 图片的高和宽

# palette
# info 储存图像相关数据的字典

# new 新建
# image.new(mode, size) 或者 image.new(mode, size, color)
# im_new = Image.new("RGB", (128, 128), "#FF0000")
im_new = Image.new("RGB", (128, 128))  # 造图
# im_new.show()

# crop
box = (30, 10, 70, 70)
region = im.crop(box)
# region.show()

# paste
# filter 滤镜
# blend 混合
# split 分离
# composite 合成物
# eval 重新计算求出结果
# merge 合成
# draft
