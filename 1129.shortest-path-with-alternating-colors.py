#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 最长字符串链
#
# https://leetcode-cn.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (35.89%)
# Total Accepted:    4.5K
# Total Submissions: 12.4K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。
# 
# red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j]
# 对表示从节点 i 到节点 j 的蓝色有向边。
# 
# 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X
# 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]
# 
# 
# 示例 2：
# 
# 输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# 输出：[0,1,-1]
# 
# 
# 示例 3：
# 
# 输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# 输出：[0,-1,-1]
# 
# 
# 示例 4：
# 
# 输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# 输出：[0,1,2]
# 
# 
# 示例 5：
# 
# 输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# 输出：[0,1,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n
# 
# 
#
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_d,blue_d = {},{}
        for start,end in red_edges:
            if start not in red_d:
                red_d[start] = [end]
            else:
                red_d[start].append(end)
        for start,end in blue_edges:
            if start not in blue_d:          
                blue_d[start] = [end]
            else:
                blue_d[start].append(end)

        path = [float('inf')] * n
        path_len = 0
        

        red_node = [0]
        blue_node = [0]
        r_visited = set()
        b_visited = set()
        while float('inf') in path:
            prv = r_visited.copy()
            brv = b_visited.copy()
            for n in red_node:
                path[n] = min(path[n],path_len)
                r_visited.add(n)
            for n in blue_node:
                path[n] = min(path[n],path_len)
                b_visited.add(n)
            new_blue_end = []
            for n in red_node:
                new_blue_end += blue_d.get(n,[])
            new_red_end = []
            for n in blue_node:
                new_red_end += red_d.get(n,[])
            red_node = list(set(new_red_end))
            blue_node = list(set(new_blue_end))
            path_len += 1
            if prv == r_visited and brv == b_visited:
                break

        path = [l if l!=float('inf') else -1 for l in path]
        return path
