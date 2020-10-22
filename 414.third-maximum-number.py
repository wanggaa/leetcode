#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (35.44%)
# Total Accepted:    37.3K
# Total Submissions: 105.2K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
# 
# 示例 1:
# 
# 
# 输入: [3, 2, 1]
# 
# 输出: 1
# 
# 解释: 第三大的数是 1.
# 
# 
# 示例 2:
# 
# 
# 输入: [1, 2]
# 
# 输出: 2
# 
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
# 
# 
# 示例 3:
# 
# 
# 输入: [2, 2, 3, 1]
# 
# 输出: 1
# 
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
# 
# 
#
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        max_v = [float('-inf')] * 3
        for n in nums:
            t = min(max_v)
            if n > t:
                max_v[max_v.index(t)] = n
        if min(max_v) == float('-inf'):
            return max(max_v)
        return min(max_v)
