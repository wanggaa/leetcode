#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 子数组中占绝大多数的元素
#
# https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (49.85%)
# Total Accepted:    7.3K
# Total Submissions: 14.5K
# Testcase Example:  '[3,6,5,1,8]'
#
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 
# 示例 2：
# 
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        t = sum(nums)
        nums.sort()
        n1 = [n for n in nums if n%3==1]
        n2 = [n for n in nums if n%3==2]
        
        if t % 3 == 1:
            if len(n1) == 0 and len(n2) <= 1:
                return 0
            if len(n2) <= 1:
                return t-n1[0]
            if len(n1) == 0:
                return t-n2[0]-n2[1]
            m = min(n1[0],n2[0]+n2[1])
            return t - m
        if t % 3 == 2:
            if len(n1) <= 1 and len(n2) == 0:
                return 0
            if len(n1) <= 1:
                return t-n2[0]
            if len(n2) == 0:
                return t-n1[0]-n1[1]
            m = min(n1[0]+n1[1],n2[0])
            return t - m
        return t
