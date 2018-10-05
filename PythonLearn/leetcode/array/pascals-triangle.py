#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/3 22:14
Filename: pascals-triangle.py
Contact: uppjs@qq.com
Description: 杨辉三角形
"""


class Solution:
    # 想不出来，不是自己写的
    @staticmethod
    def generate(numrows):
        result = []  # 声明一个空 list
        for i in range(numrows):  # 迭代，从 0 到 n-1 项
            result.append([])  # 在空 list 依次加入一个 list
            for j in range(i + 1):  # 迭代，首项单个值，依次 +1，相当于每个嵌套 list 进行单独操作
                if j in (0, i):  # 如果 j 为 0 或 1，
                    result[i].append(1)  # 也就是所有 list 的首项都是 1
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])  # 双层嵌套中放个这个我还有点蒙
        return result

    @staticmethod
    # 这个直接不懂
    def generate2(numrows):
        if not numrows:  # 不写就是空
            return []
        res = [[1]]  # 声明这个
        for i in range(1, numrows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numrows]

    @staticmethod
    def generate3(numrows):
        """
        :type numrows: int
        :rtype: List[List[int]]
        """
        if numrows == 0:  # 喜欢
            return []
        if numrows == 1:
            return [[1]]
        res = [[1], [1, 1]]  # 非 0 和 1 时，自己先声明一下这个

        def add(nums):
            res0 = nums[:1]
            for i, j in enumerate(nums):  # 哈哈 enumerate
                if i < len(nums) - 1:
                    res0 += [nums[i] + nums[i + 1]]
            res0 += nums[:1]
            return res0

        while len(res) < numrows:
            res.extend([add(res[-1])])
        return res


if __name__ == "__main__":
    print(Solution().generate(6))
