#
# @lc app=leetcode.cn id=1222 lang=python3
#
# [1222] 删除被覆盖区间
#
# https://leetcode-cn.com/problems/queens-that-can-attack-the-king/description/
#
# algorithms
# Medium (66.13%)
# Total Accepted:    4.2K
# Total Submissions: 6.3K
# Testcase Example:  '[[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]\n[0,0]'
#
# 在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。
# 
# 「黑皇后」在棋盘上的位置分布用整数坐标数组 queens 表示，「白国王」的坐标用数组 king 表示。
# 
# 「黑皇后」的行棋规定是：横、直、斜都可以走，步数不受限制，但是，不能越子行棋。
# 
# 请你返回可以直接攻击到「白国王」的所有「黑皇后」的坐标（任意顺序）。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
# 输出：[[0,1],[1,0],[3,3]]
# 解释： 
# [0,1] 的皇后可以攻击到国王，因为他们在同一行上。 
# [1,0] 的皇后可以攻击到国王，因为他们在同一列上。 
# [3,3] 的皇后可以攻击到国王，因为他们在同一条对角线上。 
# [0,4] 的皇后无法攻击到国王，因为她被位于 [0,1] 的皇后挡住了。 
# [4,0] 的皇后无法攻击到国王，因为她被位于 [1,0] 的皇后挡住了。 
# [2,4] 的皇后无法攻击到国王，因为她和国王不在同一行/列/对角线上。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
# 输出：[[2,2],[3,4],[4,4]]
# 
# 
# 示例 3：
# 
# 
# 
# 输入：queens =
# [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]],
# king = [3,4]
# 输出：[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= queens.length <= 63
# queens[0].length == 2
# 0 <= queens[i][j] < 8
# king.length == 2
# 0 <= king[0], king[1] < 8
# 一个棋盘格上最多只能放置一枚棋子。
# 
# 
#
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # max number is 8
        # king ijkl,diag*4(r-c==king,r+c==king)
        # quene sorted by x,y index if * 8, visited * 8, O(n) * 8 
        # begin from north
        kx,ky = king
        visited = [[] for _ in range(8)]
        for x,y in queens:
            if x == kx and y > ky:
                if visited[0] == []:
                    visited[0] = [x,y]
                visited[0][0] = x
                visited[0][1] = min(visited[0][1],y)
                continue
            if x-y == kx-ky and x > kx:
                if visited[1] == []:
                    visited[1] = [x,y]
                visited[1][0] = min(visited[1][0],x)
                visited[1][1] = min(visited[1][1],y)
                continue
            if x > kx and y == ky:
                if visited[2] == []:
                    visited[2] = [x,y]
                visited[2][0] = min(visited[2][0],x)
                visited[2][1] = y
                continue
            if x+y == kx+ky and x > kx:
                if visited[3] == []:
                    visited[3] = [x,y]
                visited[3][0] = min(visited[3][0],x)
                visited[3][1] = max(visited[3][1],y)
                continue
            if x == kx and y < ky:
                if visited[4] == []:
                    visited[4] = [x,y]
                visited[4][0] = x
                visited[4][1] = max(visited[4][1],y)
                continue
            if x-y == kx-ky and x < kx:
                if visited[5] == []:
                    visited[5] = [x,y]
                visited[5][0] = max(visited[5][0],x)
                visited[5][1] = max(visited[5][1],y)
                continue
            if x < kx and y == ky:
                if visited[6] == []:
                    visited[6] = [x,y]
                visited[6][0] = max(visited[6][0],x)
                visited[6][1] = y
                continue
            if x+y == kx+ky and x < kx:
                if visited[7] == []:
                    visited[7] = [x,y]
                visited[7][0] = max(visited[7][0],x)
                visited[7][1] = min(visited[7][1],y)
                continue
        ans = [q for q in visited if q != []]
        return ans
        


