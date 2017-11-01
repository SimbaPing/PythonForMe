# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 20:01:52
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 22:57:49

# 利用递归方法求5!
def fun(j):  # 定义了一个函数
    sum = 0  # 定一件属性 求和
    if j == 0:  #第一个例外，当ｊ为０时候，和等于１
        sum = 1
    else:  # 不然
        sum = j * fun(j - 1)  # 终极公式 嵌套循环
    return sum

for i in range(5):  # 从0开始遍历 依次打印
    print '%d! = %d' % (i, fun(i))

# 循环中有循环，我暂时还写不出这种简单的东西
