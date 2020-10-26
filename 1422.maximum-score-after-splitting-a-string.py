#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 划分数组为连续数字的集合
#
# https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/description/
#
# algorithms
# Easy (53.44%)
# Total Accepted:    6.7K
# Total Submissions: 12.5K
# Testcase Example:  '"011101"'
#
# 给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右
# 子字符串）所能获得的最大得分。
# 
# 「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "011101"
# 输出：5 
# 解释：
# 将字符串 s 划分为两个非空子字符串的可行方案有：
# 左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5 
# 左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4 
# 左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3 
# 左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2 
# 左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3
# 
# 
# 示例 2：
# 
# 输入：s = "00111"
# 输出：5
# 解释：当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5
# 
# 
# 示例 3：
# 
# 输入：s = "1111"
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= s.length <= 500
# 字符串 s 仅由字符 '0' 和 '1' 组成。
# 
# 
#
class Solution:
    def maxScore(self, s: str) -> int:
        n0 = [0]
        n1 = [0]
        for c in s:
            if c == '0':
                n0.append(n0[-1]+1)
                n1.append(n1[-1])
            if c == '1':
                n0.append(n0[-1])
                n1.append(n1[-1]+1)
        maxv = 0
        t1 = n1[-1]
        for i in range(1,len(s)):
            maxv = max(maxv,n0[i] + t1 - n1[i])
        return maxv

