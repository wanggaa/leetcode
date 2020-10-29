#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# https://leetcode-cn.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (36.45%)
# Total Accepted:    24.2K
# Total Submissions: 66.3K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aacecaaa"
# 输出："aaacecaaa"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abcd"
# 输出："dcbabcd"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s 仅由小写英文字母组成
# 
# 
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        rs = s[::-1]
        sp = 0
        while rs[sp:] != s[:len(s)-sp]:
            sp += 1
        return rs[:sp] + s
