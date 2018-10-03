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
    @staticmethod
    # @return a list of lists of integers
    def generate(numrows):
        result = []
        for i in range(numrows):
            result.append([])
            for j in range(i + 1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        return result

    @staticmethod
    def generate2(numrows):
        if not numrows: return []
        res = [[1]]
        for i in range(1, numrows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numrows]

    @staticmethod
    def generate3(numrows):
        """
        :type numrows: int
        :rtype: List[List[int]]
        """
        if numrows == 0: return []
        if numrows == 1: return [[1]]
        res = [[1], [1, 1]]

        def add(nums):
            res = nums[:1]
            for i, j in enumerate(nums):
                if i < len(nums) - 1:
                    res += [nums[i] + nums[i + 1]]
            res += nums[:1]
            return res

        while len(res) < numrows:
            res.extend([add(res[-1])])
        return res


if __name__ == "__main__":
    print(Solution().generate(6))
