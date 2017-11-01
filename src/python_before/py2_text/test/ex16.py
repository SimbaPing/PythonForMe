# -*- coding:utf-8 -*-

from sys import argv  # 从 sys 里面解包 argv

script, filename = argv  # 脚本名字 文件名字 用 argv 赋予他们力量

print "We're going to erase %r." % filename  # 我们去擦除文件
print "If you don't want that, hit CTRL-C(^C)."  # 没用的废话
print "If you want that, hit RETURN."  # 没用的废话

raw_input("?")   # 提示了一个问号

print "Opening the file..."  # 打开文件
target = open(filename, 'w')  # 目标 打来文件 并开始准备写入文件 w代表写入模式

print "Trunncating the file. Goodbye!"
target.truncate()  # 目标。清空文件

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")  # 准备好要输入的三行
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)  # 写入刚才的三行
target.write("\n")  # 换行符
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()  # 写完了，目标 关闭
