# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 17:30:36
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 18:07:30

# 对10个数进行排序。
if __name__ == '__main__':
    # 输入十个数并打印
    N = 10
    print 'please input ten num:\n'
    l = []
    for i in range(N):  # 向ｌ里添加输入的整数　输入Ｎ次
        l.append(int(raw_input('input a number:\n')))
    print
    for i in range(N):
        print l[i]  # 这个地方得好好看一下什么意思
    print
    # 将这十个数从小到大排序
    # 好复杂，看不懂
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if l[min] > l[j]:min = j
        l[i], l[min] = l[min], l[i]
    print 'after sorted'
    for i in range(N):
        print l[i]
