#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Easy (66.90%)
# Total Accepted:    18.6K
# Total Submissions: 27.8K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L)
# 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
# 
# 示例 1:
# 
# 
# 输入: 
# ⁠   1
# ⁠  / \
# ⁠ 0   2
# 
# ⁠ L = 1
# ⁠ R = 2
# 
# 输出: 
# ⁠   1
# ⁠     \
# ⁠      2
# 
# 
# 示例 2:
# 
# 
# 输入: 
# ⁠   3
# ⁠  / \
# ⁠ 0   4
# ⁠  \
# ⁠   2
# ⁠  /
# ⁠ 1
# 
# ⁠ L = 1
# ⁠ R = 3
# 
# 输出: 
# ⁠     3
# ⁠    / 
# ⁠  2   
# ⁠ /
# ⁠1
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
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val < low:
            return self.trimBST(root.right,low,high)
        if root.val > high:
            return self.trimBST(root.left,low,high)
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)        
        return root
