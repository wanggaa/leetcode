#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] 学生出勤记录 II
#
# https://leetcode-cn.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (42.08%)
# Total Accepted:    3.6K
# Total Submissions: 8.5K
# Testcase Example:  '1'
#
# 给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 10^9 + 7的值。
# 
# 学生出勤记录是只包含以下三个字符的字符串：
# 
# 
# 'A' : Absent，缺勤
# 'L' : Late，迟到
# 'P' : Present，到场
# 
# 
# 如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。
# 
# 示例 1:
# 
# 
# 输入: n = 2
# 输出: 8 
# 解释：
# 有8个长度为2的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# 只有"AA"不会被视为可奖励，因为缺勤次数超过一次。
# 
# 注意：n 的值不会超过100000。
# 
#
class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10**9+7
        nA0,nA1,nA0L,nA1L,nA0LL,nA1LL = 1,0,0,0,0,0
        for _ in range(n):
            nA0,nA1,nA0L,nA1L,nA0LL,nA1LL = (nA0+nA0L+nA0LL)%M,(nA0+nA0L+nA1+nA1L+nA0LL+nA1LL)%M,nA0,nA1,nA0L,nA1L
        return (nA0+nA1+nA0L+nA1L+nA0LL+nA1LL) % M
            
