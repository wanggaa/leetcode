#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#
# https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes/description/
#
# algorithms
# Hard (54.82%)
# Total Accepted:    3.3K
# Total Submissions: 6.1K
# Testcase Example:  '[[1,2,3],[0],[0],[0]]'
#
# 给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 
# 
# graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。
# 
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一个可能的路径为 [1,0,2,0,3]
# 
# 示例 2：
# 
# 输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一个可能的路径为 [0,1,4,2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= graph.length <= 12
# 0 <= graph[i].length < graph.length
# 
# 
#
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited_list = []
        visited_set = set() 
        node_number = len(graph)
        all_visited = 2**(node_number)-1
        for i in range(node_number):
            visited_list.append([2**i,i,0])
            visited_set.add((2**i,i))
        while True:
            cur_set,cur_node,path_len = visited_list.pop(0)
            if cur_set == all_visited:
                return path_len
            
            for node in graph[cur_node]: 
                new_pair = (cur_set|(2**node),node)
                if new_pair in visited_set:
                    continue
                visited_set.add(new_pair)
                visited_list.append([new_pair[0],new_pair[1],path_len+1])
        

