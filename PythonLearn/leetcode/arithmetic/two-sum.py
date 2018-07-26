#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: two-sum
.......date: 2018/7/25 9:35
created with IntelliJ IDEA
description:
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j] and i != j:
                    print([i, j])


if __name__ == '__main__':
    a = Solution()
    a.twoSum([2, 7, 11, 15], 9)
