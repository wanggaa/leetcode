#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 具有所有最深节点的最小子树
#
# https://leetcode-cn.com/problems/monotonic-array/description/
#
# algorithms
# Easy (53.35%)
# Total Accepted:    19.3K
# Total Submissions: 36.2K
# Testcase Example:  '[1,2,2,3]'
#
# 如果数组是单调递增或单调递减的，那么它是单调的。
# 
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A
# 是单调递减的。
# 
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,2,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：[6,5,4,4]
# 输出：true
# 
# 
# 示例 3：
# 
# 输入：[1,3,2]
# 输出：false
# 
# 
# 示例 4：
# 
# 输入：[1,2,4,5]
# 输出：true
# 
# 
# 示例 5：
# 
# 输入：[1,1,1]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
#
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True
        increase = 0
        for i in range(1,len(A)):
            if A[i-1] == A[i]:
                continue
            if A[i-1] < A[i]:
                if increase == -1:
                    return False
                increase = 1
            if A[i-1] > A[i]:
                if increase == 1:
                    return False
                increase = -1
        return True

