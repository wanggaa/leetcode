#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] K 连续位的最小翻转次数
#
# https://leetcode-cn.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (43.81%)
# Total Accepted:    6.7K
# Total Submissions: 15.3K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
# 
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
# 
# 
# 
# 示例 1：
# 
# 输入：[[1,1],[2,3],[3,2]]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：[[1,1],[2,2],[3,3]]
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100
# 
# 
#
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points.sort(key=lambda x:x[0])
        x1 = points[2][0] - points[1][0]
        y1 = points[2][1] - points[1][1]
        x0 = points[1][0] - points[0][0]
        y0 = points[1][1] - points[0][1]

        if x1*y0 == y1*x0:
            return False
        return True
