#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 工作计划的最低难度
#
# https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
#
# algorithms
# Medium (64.76%)
# Total Accepted:    5.6K
# Total Submissions: 8.5K
# Testcase Example:  '[2,3,1,3,1,null,1]'
#
# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
# 
# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root = [2,3,1,3,1,null,1]
# 输出：2 
# 解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
# ⁠    在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1]
# 存在回文排列 [1,2,1] 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：root = [2,1,1,1,3,null,null,null,null,null,1]
# 输出：1 
# 解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
# ⁠    这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
# 
# 
# 示例 3：
# 
# 输入：root = [9]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 给定二叉树的节点数目在 1 到 10^5 之间。
# 节点值在 1 到 9 之间。
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        # return path?
        def visit(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [[root.val]]
            l_paths = visit(root.left)
            r_paths = visit(root.right)
            paths = l_paths + r_paths
            paths = [[root.val] + path for path in paths]
            return paths

        paths = visit(root)
        ans = 0
        for path in paths:
            symbol = False
            keys = set(path)
            for k in keys:
                if path.count(k) % 2:
                    if symbol:
                        ans -= 1
                        break
                    symbol = True
            ans += 1

        return ans
