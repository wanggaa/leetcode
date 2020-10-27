#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 最大频率栈
#
# https://leetcode-cn.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (61.84%)
# Total Accepted:    8K
# Total Submissions: 12.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
# 
# 下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
# 
# 
# 
# 示例：
# 
# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：12
# 解释：
# 可能的下降路径有：
# 
# 
# 
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 
# 
# 和最小的下降路径是 [1,4,7]，所以答案是 12。
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
# 
# 
#
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        dp_dict ={}
        # i row, j col
        def dp_helper(i,j):
            if j < 0 or j >= len(A[0]):
                return float('inf')
            if i >= len(A):
                return 0

            min_v = float('inf')
            for next_j in range(j-1,j+2):
                t = (i+1,next_j)
                if t not in dp_dict:
                    dp_dict[t] = dp_helper(i+1,next_j)
                min_v = min(min_v,dp_dict[t])

            return min_v + A[i][j]
        return min([dp_helper(0,j) for j in range(len(A[0]))])

