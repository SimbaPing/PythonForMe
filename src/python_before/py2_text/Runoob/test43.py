# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-26 12:05:33
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-26 12:36:54
# 模仿静态变量(static)另一案例


class Num:
    nNum = 1　# 局部变量

    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if __name__ == '__main__':
    nNum = 2  #　全局变量
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()  # 循环三遍局部变量
