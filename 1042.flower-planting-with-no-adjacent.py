#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 合并石头的最低成本
#
# https://leetcode-cn.com/problems/flower-planting-with-no-adjacent/description/
#
# algorithms
# Easy (51.58%)
# Total Accepted:    8.7K
# Total Submissions: 16.8K
# Testcase Example:  '3\n[[1,2],[2,3],[3,1]]'
#
# 有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi
# 的双向路径。在每个花园中，你打算种下四种花之一。
# 
# 另外，所有花园 最多 有 3 条路径可以进入或离开.
# 
# 你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
# 
# 以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4
# 表示。保证存在答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, paths = [[1,2],[2,3],[3,1]]
# 输出：[1,2,3]
# 解释：
# 花园 1 和 2 花的种类不同。
# 花园 2 和 3 花的种类不同。
# 花园 3 和 1 花的种类不同。
# 因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4, paths = [[1,2],[3,4]]
# 输出：[1,2,1,2]
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# 输出：[1,2,3,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# paths[i].length == 2
# 1 i, yi 
# xi != yi
# 每个花园 最多 有 3 条路径可以进入或离开
# 
# 
#
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        flowers = [0] * n
        
        pure_paths = []
        for a,b in paths:
            pure_paths.append([a-1,b-1])

        paths = pure_paths

        d = {}
        for a,b in paths:
            d[a] = d.get(a,[])+[b]
            d[b] = d.get(b,[])+[a]
       
        stack = [1]
        colors = [1,2,3,4]
        while 0 in flowers:
            stack = [flowers.index(0)]
            while stack:
                t = stack.pop(0)
                if t not in d:
                    flowers[t] = 1
                    continue
                if flowers[t]:
                    continue
                stack = stack + d[t]
                
                for c in colors:
                    symbol = True
                    for n in d[t]:
                        if c == flowers[n]:
                            symbol = False
                            break
                    if symbol:
                        flowers[t] = c
                        break
        return flowers
