#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: 两数之和
.......date: 2018/7/24 22:09
created with IntelliJ IDEA
description:
"""


class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i in range(len(self.nums) - 1):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return print([i, j])


if __name__ == '__main__':
    a = Solution(20, 10)
    print(a.twoSum())
