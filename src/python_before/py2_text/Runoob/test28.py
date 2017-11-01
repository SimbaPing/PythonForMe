# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 23:15:54
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 23:36:21

# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第3个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。
# 请问第五个人多大？

# 依次差值为2 倒叙数学公式
def age(n):
    if n == 1:  # 确切答案，第一个人，10岁 已知明确条件
        c =10
    else:
        c = age(n - 1) + 2  # 一个嵌套
    return c

print age(5)
