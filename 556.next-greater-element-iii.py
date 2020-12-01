#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
# https://leetcode-cn.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (32.00%)
# Total Accepted:    7.6K
# Total Submissions: 23.8K
# Testcase Example:  '12'
#
# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
# 
# 示例 1:
# 
# 
# 输入: 12
# 输出: 21
# 
# 
# 示例 2:
# 
# 
# 输入: 21
# 输出: -1
# 
# 
#
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        slen = len(s)
        stack = []
        for i in reversed(range(slen)):
            t = None
            while stack and s[i] < s[stack[-1]]:
                t = stack.pop(-1)
            stack.append(i)
            if t is not None:
                print(stack)
                s[i],s[t] = s[t],s[i]
                ans = int(''.join(s[:i+1] + sorted(s[i+1:])))
                if ans >= 2**31:
                    break
                return ans
        return -1
            
