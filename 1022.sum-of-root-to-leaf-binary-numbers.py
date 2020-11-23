#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 不同路径 III
#
# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (67.01%)
# Total Accepted:    12.3K
# Total Submissions: 18.2K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1
# -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
# 
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
# 
# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,0,1,0,1,0,1]
# 输出：22
# 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 示例 2：
# 
# 
# 输入：root = [0]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：1
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,1]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的结点数介于 1 和 1000 之间。
# Node.val 为 0 或 1 。
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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0

        def visit(root,v):
            if root is None:
                return
            if root.left is None and root.right is None:
                nonlocal ans
                ans += v*2+root.val
                return
            if root.left is not None:
                visit(root.left,v*2+root.val)
            if root.right is not None:
                visit(root.right,v*2+root.val)
        
        visit(root,0)
        return ans
