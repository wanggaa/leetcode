#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 独特的电子邮件地址
#
# https://leetcode-cn.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (68.04%)
# Total Accepted:    21K
# Total Submissions: 30.9K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
# 
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[1,1,1,1,1,null,1]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[2,2,2,5,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 给定树的节点数范围是 [1, 100]。
# 每个节点的值都是整数，范围为 [0, 99] 。
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None and root.right is not None:
            return self.isUnivalTree(root.right) and root.val == root.right.val
        if root.left is not None and root.right is None:
            return self.isUnivalTree(root.left) and root.val == root.left.val
        return root.val == root.left.val == root.right.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

