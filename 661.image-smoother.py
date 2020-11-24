#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
# https://leetcode-cn.com/problems/image-smoother/description/
#
# algorithms
# Easy (54.51%)
# Total Accepted:    10.8K
# Total Submissions: 19.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入)
# ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
# 
# 示例 1:
# 
# 
# 输入:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# 输出:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 
# 
# 注意:
# 
# 
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。
# 
# 
#
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m,n = len(M),len(M[0])
        presum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        avg = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                presum[i][j] = (presum[i-1][j]+presum[i][j-1])+M[i-1][j-1]-presum[i-1][j-1]
        for i in range(m):
            for j in range(n):
                r0 = max(0,i-1)
                c0 = max(0,j-1)
                r1 = min(m,i+2)
                c1 = min(n,j+2)
                t = (r1-r0)*(c1-c0)
                avg[i][j] = (presum[r1][c1]-presum[r0][c1]-presum[r1][c0]+presum[r0][c0])//t
        return avg
