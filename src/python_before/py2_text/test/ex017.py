# -*- coding:utf-8 -*-

from sys import argv  # 一个list，包含所有参数
from os.path import exists  # 判断文件是否存在

script, from_file, out_file = argv  # list 源码 从文件 到文件

print "Copying from %s to %s" % (from_file, out_file)  # 从文件到文件

# We could do these two on one line too, how?
out_file = open(from_file,'w')

print "The input file is %d bytes long" % len(out_file)  # in文件有多长

print "Does the output file exist? %r" % exists(out_file)  # 不懂
print "Ready, hit RETURN to countinue, CTRL-C to abort."
raw_input()  # 输入命令

out_file.write(out_file)

print "Alright, all done."

out_file.close()  # 关闭这两个
from_file.close()
