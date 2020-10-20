#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (52.57%)
# Total Accepted:    348.3K
# Total Submissions: 662.5K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0],nums[0]
            link,maxv = helper(nums[1:])
            link = max(link+nums[0],nums[0])
            maxv = max(maxv,link)
            return link,maxv
        if not nums:
            return 0
        link = [nums[0]]
        maxv = [nums[0]]

        for n in nums[1:]:
            link.append(max(link[-1]+n,n))
            maxv.append(max(maxv[-1],link[-1]))

        return maxv[-1]


