#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
# https://leetcode-cn.com/problems/rectangle-area/description/
#
# algorithms
# Medium (43.78%)
# Total Accepted:    13.5K
# Total Submissions: 30.7K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
# 
# 每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
# 
# 
# 
# 示例:
# 
# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
# 
# 说明: 假设矩形面积不会超出 int 的范围。
# 
#
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x = max(0,min(G,C)-max(A,E))
        y = max(0,min(D,H)-max(B,F))
        return (C-A)*(D-B)+(G-E)*(H-F)-x*y
