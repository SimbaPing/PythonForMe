# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 20:30:53
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 21:19:56

# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

# one
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
print fib(10)

# two
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + (n - 2)
print fib(10)

# three
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print fib(10)

# 我觉得这些答案都不好，但我还不会做
# 看来数学还得好好学
