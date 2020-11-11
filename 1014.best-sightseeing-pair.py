#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最接近原点的 K 个点
#
# https://leetcode-cn.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (53.17%)
# Total Accepted:    28.1K
# Total Submissions: 52.9K
# Testcase Example:  '[8,1,5,2,6]'
#
# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
# 
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
# 
# 返回一对观光景点能取得的最高分。
# 
# 
# 
# 示例：
# 
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
# 
# 
#
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left,right = [],[]
        for i in range(len(A)):
            left.append(A[i]+i)
            right.append(A[i]-i)

        stack = []
        
        for r in reversed(right):
            if not stack or r >= stack[-1]:
                stack.append(r)
        maxv = float('-inf')
        maxl = float('-inf')
        for i in range(len(left)):
            maxl = max(maxl,left[i])
            if right[i] == stack[-1]:
                stack.pop(-1)
            if stack:
                maxv = max(maxv,stack[-1]+maxl)
        return maxv

        
