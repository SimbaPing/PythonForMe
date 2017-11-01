# -*- coding:utf-8 -*-

from sys import argv  # 一个list，包含所有参数
from os.path import exists  # 判断文件是否存在

script, from_file, to_file = argv  # list 源码 从文件 到文件

print "Copying from %s to %s" % (from_file, to_file)  # 从文件到文件

# We could do these two on one line too, how?
in_file = open(from_file)  # in文件读取from文件
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)  # in文件有多长

print "Does the output file exist? %r" % exists(to_file)  # 是否存在to，返回true或false
print "Ready, hit RETURN to countinue, CTRL-C to abort."
raw_input()  # 输入命令

out_file = open(to_file, 'w')  # 把to的数据写入out
out_file.write(indata)

print "Alright, all done."

out_file.close()  # 关闭这两个
in_file.close()
