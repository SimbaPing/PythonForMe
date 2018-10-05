#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/6 3:21
Filename: t-pascals-trangle.py
Contact: uppjs@qq.com
Description: 
"""


def generate3(numrows):
    """
    :type numrows: int
    :rtype: List[List[int]]
    """
    if numrows == 0:
        return []
    if numrows == 1:
        return [[1]]
    res = [[1], [1, 1]]

    def add(nums):
        res0 = nums[:1]
        for i, j in enumerate(nums):
            if i < len(nums) - 1:
                res0 += [nums[i] + nums[i + 1]]
        res0 += nums[:1]
        return res0

    while len(res) < numrows:
        res.extend([add(res[-1])])
    return print(res)


generate3(10)


# 想不出来，不是自己写的
def generate(numrows):
    result = []  # 声明一个空 list
    for i in range(numrows):  # 迭代，从 0 到 n-1 项
        result.append([])  # 在空 list 依次加入一个 list
        for j in range(i + 1):  # 迭代，首项单个值，依次 +1，相当于每个嵌套 list 进行单独操作
            if j in (0, i):  # 如果 j 为 0 或 1，
                result[i].append(1)  # 也就是所有 list 的首项都是 1
            else:
                result[i].append(result[i - 1][j - 1] + result[i - 1][j])  # 双层嵌套中放个这个我还有点蒙
    return print(result)


generate(10)
