# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 22:53:31
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 23:15:41

# 利用递归函数调用方式，
# 将所输入的5个字符，以相反顺序打印出来


def output(s, l):  # 定义字符串s 以及长度l
    if l == 0:  # 没有长度 那就趁早结束
        return
    print s[l - 1]
    output(s, l - 1)

# 这些东西都要放到最后 呵呵
s = raw_input('Input a string:')
l = len(s)
output(s, l)  # 启动定义 所以这个要放在最后
