#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 驼峰式匹配
#
# https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths/description/
#
# algorithms
# Medium (47.81%)
# Total Accepted:    2.9K
# Total Submissions: 6.1K
# Testcase Example:  '[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1'
#
# 给定一棵二叉树的根 root，请你考虑它所有 从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）
# 
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。
# 
# 请你删除所有不足节点，并返回生成的二叉树的根。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 
# 输出：[1,2,3,4,null,null,7,8,9,null,14]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5]
# 
# 示例 3：
# 
# 
# 输入：root = [5,-6,-6], limit = 0
# 输出：[]
# 
# 
# 
# 提示：
# 
# 
# 给定的树有 1 到 5000 个节点
# -10^5 <= node.val <= 10^5
# -10^9 <= limit <= 10^9
# 
# 
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
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        d = {}        
        def sumTree(root,val):
            if root is None:
                return
            val += root.val
            d[root] = val
            sumTree(root.left,  val)
            sumTree(root.right, val)

        sumTree(root,0)

        def deleteNode(root):
            if root is None:
                return None
            if root.left is None and root.right is None:
                if d[root] < limit:
                    return 2 
            lt = deleteNode(root.left)
            rt = deleteNode(root.right)
            
            if lt == 2 and rt == 2:
                root.left = None
                root.right = None
                return 2
            if lt == 2:
                root.left = None
                if rt is None:
                    return 2
            if rt == 2:
                root.right = None
                if lt is None:
                    return 2
            return root

        t = deleteNode(root)
        if t == 2:
            return None
        return root
