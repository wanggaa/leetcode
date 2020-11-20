#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (58.10%)
# Total Accepted:    32.5K
# Total Submissions: 55.7K
# Testcase Example:  '"bbbab"'
#
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
# 
# 
# 
# 示例 1:
# 输入:
# 
# "bbbab"
# 
# 
# 输出:
# 
# 4
# 
# 
# 一个可能的最长回文子序列为 "bbbb"。
# 
# 示例 2:
# 输入:
# 
# "cbbd"
# 
# 
# 输出:
# 
# 2
# 
# 
# 一个可能的最长回文子序列为 "bb"。
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 只包含小写英文字母
# 
# 
#
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans = 1 
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i,n):
                if i == j :
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    ans = max(ans,dp[i][j])     
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return ans 

if __name__ == '__main__':
    s = Solution()
    ans = s.longestPalindromeSubseq("a")
