#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.90%)
# Total Accepted:    54.3K
# Total Submissions: 136.1K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 
#
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        
        def valid(s):
            if len(s) <= 1:
                return True
            i,j = 0,len(s)-1
            while i<j and s[i] == s[j]:
                i += 1
                j -= 1
            if i >= j:
                return True
            else:
                return False

        return valid(s[i:j]) or valid(s[i+1:j+1])
