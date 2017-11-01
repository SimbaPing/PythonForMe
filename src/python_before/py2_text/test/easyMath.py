# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-05 15:23:08
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-05 16:01:44
from operator import add, sub  # 从模块中导入我们会用到的函数 经营者
from random import randint, choice  # 同上 随机

ops = {'+': add, '-': sub}  # 字典 全局变量
MAXTRIES = 2  # 最大尝试数


def doprob():  # 定义一个函数 do prob 做题 核心引擎
    op = choice('+-')  # choice 函数：随机选择加减
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)  # 一个匿名函数
    ans = ops[op](*nums)  # 正确答案
    pr = '%d %s %d =' % (nums[0], op, nums[1])  # 打印计算式
    oops = 0
    while True:  # 处理有效无效的控制循环
        try:
            if int(raw_input(pr)) == ans:
                print "correct"
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except(KeyboardInterrupt,
               EOFError, ValueError):
            print 'invalid input... try again'


def main():  # 程序的主入口
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except(KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
