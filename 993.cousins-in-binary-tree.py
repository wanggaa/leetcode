#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 最高的广告牌
#
# https://leetcode-cn.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.01%)
# Total Accepted:    13.7K
# Total Submissions: 26.4K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
# 
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
# 
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。
# 
# 
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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def visit(root,d,x):
            if root is None:
                return None
            if root.val == x:
                return d
            return visit(root.left,d+1,x) or visit(root.right,d+1,x)

        def common_parent(root,x,y):
            if root.left is None and root.right is None:
                return True
            if root.left is None:
                return common_parent(root.right,x,y)
            if root.right is None:
                return common_parent(root.left,x,y)

            if root.left.val == x and root.right.val == y:
                return False
            if root.right.val == x and root.left.val == y:
                return False
            
            return common_parent(root.left,x,y) and common_parent(root.right,x,y)

        x_d = visit(root,0,x)
        y_d = visit(root,0,y)
        
        return x_d == y_d and common_parent(root,x,y)
