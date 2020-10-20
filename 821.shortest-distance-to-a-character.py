#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 打砖块
#
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (67.92%)
# Total Accepted:    15.4K
# Total Submissions: 22.7K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
# 
# 示例 1:
# 
# 
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 说明:
# 
# 
# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。
# 
# 
#
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [0 if c == C else float('inf') for c in S]
        for k in range(len(ans)):
            if ans[k] == 0:
                j = k+1
                while j < len(ans) and ans[j] != 0:
                    ans[j] = ans[j-1] + 1
                    j += 1
                i = k-1
                while i >= 0 and ans[i] > ans[i+1]:
                    ans[i] = ans[i+1] + 1
                    i -= 1
        return ans
