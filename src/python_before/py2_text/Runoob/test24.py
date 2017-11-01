# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 10:39:01
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 19:52:55

# 有一分数序列：
# 2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和。

# 第一种
a = 2.0  # 分子的开始项 这个数要带0
b = 1.0  # 分母的开始项
s = 0  # 总和开始是0
for n in range(1, 21):  # 开始的前20项，从1开始，n代表次数
    s += a / b  # 这些公式太动脑子了，谁TM能想出来，WTF
    t = a
    a = a + b
    b = t  # 不要重新赋值的a 要原来的a 所以又重新加入了t
print s

# 第二种
a = 2.0  # 分子的开始项 这个数要带0
b = 1.0  # 分母的开始项
s = 0  # 总和开始是0
for n in range(1, 21):
    s += a / b
    a, b = a + b, a  # 不用再重新赋值，这样就好了
print s

# 第三种
a = 2.0  # 分子的开始项 这个数要带0
b = 1.0  # 分母的开始项
l = []
for n in range(1, 21):
    b, a = a, a + b
    l.append(a / b)
print reduce(lambda x, y: x + y, l)
