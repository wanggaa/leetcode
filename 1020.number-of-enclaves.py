#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 最长湍流子数组
#
# https://leetcode-cn.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (52.41%)
# Total Accepted:    6.1K
# Total Submissions: 11.6K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。
# 
# 移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。
# 
# 返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释： 
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 
# 示例 2：
# 
# 输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# 所有行的大小都相同
# 
# 
#
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        import numpy as np
        m,n = len(A)+2,len(A[0])+2
        A = np.array(A)
        B = np.ones((m,n))
        B[1:-1,1:-1] = A
        

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if B[i][j] == 0:
                return
            if B[i][j] == -1:
                return
            
            B[i][j] = -1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        dfs(0,0)
        ans = 0
        for i in range(m):
            for j in range(n):
                if B[i,j] == 1:
                    ans += 1
        return ans
        
