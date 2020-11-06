#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] N 天后的牢房
#
# https://leetcode-cn.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (50.79%)
# Total Accepted:    35.5K
# Total Submissions: 70K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
# 
# 
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 
# 
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
# 
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
# 
# 
# 示例 3：
# 
# 输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2
# 
# 
#
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def valid(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            return True
        
        def infect(grid):
            changed = False
            offsets = [[-1,0],[1,0],[0,-1],[0,1]]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] != 2:
                        continue
                    for t in offsets:
                        ti = t[0]+i
                        tj = t[1]+j
                        if valid(ti,tj):
                            if grid[ti][tj] == 1:
                                changed = True
                                grid[ti][tj] = -1

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == -1:
                        grid[i][j] = 2
            return grid,changed
                            

        time = 0
        while True:
            grid,changed = infect(grid) 
            if not changed:
                break
            else:
                time += 1
        for line in grid:
            if 1 in line:
                return -1 
        return time
