#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 可被 5 整除的二进制前缀
#
# https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (58.63%)
# Total Accepted:    30.1K
# Total Submissions: 51.3K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
# 
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
# 
# 
# 
# 示例 1：
# 
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 
# 
# 示例 2：
# 
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 
# 
# 示例 3：
# 
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] 和 str2[i] 为大写英文字母
# 
# 
#
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1,str2 = str2,str1

        while True:
            if str1 == str2:
                return str1
            if not str1.startswith(str2):
                return ""
            while str1.startswith(str2):
                str1 = str1[len(str2):]
            if len(str1) == 0:
                return str2
            str1,str2 = str2,str1
