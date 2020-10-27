#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
#
# https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (32.46%)
# Total Accepted:    2.6K
# Total Submissions: 8K
# Testcase Example:  '1'
#
# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。
# 
# 示例 1:
# 
# 输入: 5
# 输出: 5
# 解释: 
# 下面是带有相应二进制表示的非负整数<= 5：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
# 
# 说明: 1 <= n <= 10^9
# 
#
class Solution:
    def findIntegers(self, num: int) -> int:
        target = bin(num)[2:]
        hc0,hc1,nc0,nc1=1,0,0,0
        for c in target:
            if c == '0':
                hc0,hc1,nc0,nc1 = hc0+hc1,0,nc0+nc1,nc0
                continue
            if c == '1':
                hc0,hc1,nc0,nc1 = 0,hc0,hc0+hc1+nc0+nc1,nc0
                continue
        return hc0+hc1+nc0+nc1
