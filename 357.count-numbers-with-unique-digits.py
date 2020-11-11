#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (51.36%)
# Total Accepted:    15.3K
# Total Submissions: 29.7K
# Testcase Example:  '2'
#
# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
# 
# 示例:
# 
# 输入: 2
# 输出: 91 
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
# 
# 
#
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1 
        import math
        f9 = math.factorial(9)
        ans = 10
        n-1
        for k in range(1,n):
            if k > 10:
                break
            ans += 9*f9//math.factorial(9-k)
            
        return ans
