#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (49.27%)
# Total Accepted:    33.4K
# Total Submissions: 67.8K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
# 
# 示例 1:
# 
# 输入: 16
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 5
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        num = bin(num)
        if num.count('0') % 2 and num.count('1') == 1:
            return True
        else:
            return False


