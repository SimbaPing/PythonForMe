#
# [9] Palindrome Number
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (51.52%)
# Total Accepted:    27.6K
# Total Submissions: 53.6K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            # 因为知道是一个整数，所以将它变为字符串
            str_x = str(x)
            # 将字符串倒置
            str_x = str_x[::-1]
            # 将字符串还原为整数
            y = int(str_x)
            if x == y:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    pOne = Solution()
    pOne.isPalindrome(12321)
