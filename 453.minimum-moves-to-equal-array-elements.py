#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (54.86%)
# Total Accepted:    17.5K
# Total Submissions: 31.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。
# 
# 
# 
# 示例:
# 
# 输入:
# [1,2,3]
# 
# 输出:
# 3
# 
# 解释:
# 只需要3次移动（注意每次移动会增加两个元素的值）：
# 
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# 
#
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minv = min(nums) 
        ans = sum([n-minv for n in nums])
        return ans
