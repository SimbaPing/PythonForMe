# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 16:58:56
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 17:03:22

# 练习函数调用


def hello_world():
    print 'hello world'


def three_hellos():
    for i in range(3):
        hello_world()  # 如果有情况就搞三遍这个
if __name__ == '__main__':  # 意思貌似是直接运行这个文件
    three_hellos()  # 去调用后一个def
