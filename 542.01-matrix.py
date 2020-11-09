#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (45.03%)
# Total Accepted:    42K
# Total Submissions: 93.3K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# 
# 两个相邻元素间的距离为 1 。
# 
# 示例 1: 
# 输入:
# 
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 输出:
# 
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 示例 2: 
# 输入:
# 
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# 
# 输出:
# 
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 注意:
# 
# 
# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
# 
# 
#
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        def valid(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            return True

        offsets = [[-1,0],[1,0],[0,-1],[0,1]]
        def update(matrix):
            nmat = [[float('inf')]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        nmat[i][j] = 0
                        continue
                    for t in offsets:
                        ni,nj = i+t[0],j+t[1]
                        if valid(ni,nj):
                            nmat[i][j] = min(mat[ni][nj],nmat[i][j])
                    nmat[i][j] += 1
            return nmat
        mat = matrix.copy()
        while True:
            nmat = update(mat)
            if nmat == mat:
                break
            nmat,mat = mat,nmat
        return mat

        


























        
