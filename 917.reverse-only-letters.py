#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 救生艇
#
# https://leetcode-cn.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (56.17%)
# Total Accepted:    20.4K
# Total Submissions: 36.2K
# Testcase Example:  '"ab-cd"'
#
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入："ab-cd"
# 输出："dc-ba"
# 
# 
# 示例 2：
# 
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 
# 
# 示例 3：
# 
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 提示：
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S 中不包含 \ or "
# 
# 
#
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = [c for c in S if c.isalpha()]
        s = list(reversed(s))
        ans = []
        sp = 0
        for c in S:
            if c.isalpha():
                ans.append(s[sp])
                sp += 1
            else:
                ans.append(c)
        return ''.join(ans)
