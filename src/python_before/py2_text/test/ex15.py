# -*- coding:utf-8 -*-

from sys import argv  # 使用 argv 来获取文件名

script, filename = argv

txt = open(filename)  # open 接受一个参数并返回一个值

print "%s," % script
print "Here's your file %r:" % filename
print txt.read()  # 读取这个文件内容

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
