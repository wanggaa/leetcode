#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (46.95%)
# Total Accepted:    17.3K
# Total Submissions: 36.9K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,2,5,null,null,5,7]
# 输出：5
# 解释：最小的值是 2 ，第二小的值是 5 。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [2,2,2]
# 输出：-1
# 解释：最小的值是 2, 但是不存在第二小的值。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 25] 内
# 1 
# 对于树中每个节点 root.val == min(root.left.val, root.right.val)
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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return -1

        lt = self.findSecondMinimumValue(root.left)
        rt = self.findSecondMinimumValue(root.right)

        if root.left.val == root.right.val:
            if lt == rt == -1:
                return -1
            if lt == -1:
                return rt
            if rt == -1:
                return lt
            return min(rt,lt)

        if root.val == root.left.val:
            if lt == -1:
                return root.right.val
            return min(root.right.val,lt)
        if root.val == root.right.val:
            if rt == -1:
                return root.left.val
            return min(root.left.val,rt)

