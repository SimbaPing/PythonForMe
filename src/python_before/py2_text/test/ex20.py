# -*- coding:utf-8 -*-
from sys import argv

script, input_file = argv


def print_all(f):  # 定义了 f ，f只是一个变量名
    print f.read()  # f 只读


def rewind(f):
    f.seek(0)  # 重新定义这个文件从零开始


def print_a_line(line_count, f):  # 定义了两个参数
    print line_count, f.readline()  # 前面数字是多少，就读哪一行


current_file = open(input_file)  # 现在的文件=打开input文件

print "First let's print the whole file:\n"

print_all(current_file)  # 根据之前的def，只读现在文件

print "Now let's rewind, kind of like a tape."

rewind(current_file)  # 退回去，重新开始计算文件

print "Let's print three lines:"

# 前一个参数计数，后一个参数得数
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
