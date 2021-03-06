#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (40.10%)
# Total Accepted:    36.2K
# Total Submissions: 90.2K
# Testcase Example:  '[0,0,0,1]'
#
# 在一个给定的数组nums中，总是存在一个最大元素 。
# 
# 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
# 
# 如果是，则返回最大元素的索引，否则返回-1。
# 
# 示例 1:
# 
# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
# 
# 
# 
# 
# 示例 2:
# 
# 输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4没有超过3的两倍大, 所以我们返回 -1.
# 
# 
# 
# 
# 提示:
# 
# 
# nums 的长度范围在[1, 50].
# 每个 nums[i] 的整数范围在 [0, 100].
# 
# 
#
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = -1
        max_2v = max_1v = 0
        for i in range(len(nums)):
            n = nums[i]
            if n >= max_1v:
                max_2v = max_1v
                max_1v = n
                max_index = i
            elif n > max_2v:
                max_2v = n
        if max_1v >= 2*max_2v:
            return max_index 
        else:
            return -1 
