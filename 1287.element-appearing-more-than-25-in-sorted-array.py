#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 公交站间的距离
#
# https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (60.81%)
# Total Accepted:    9.7K
# Total Submissions: 16K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
# 
# 请你找到并返回这个整数
# 
# 
# 
# 示例：
# 
# 
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
# 
#
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        min_len = length // 4
        for i in range(min_len,length):
            if arr[i-min_len] == arr[i]:
                return arr[i]
