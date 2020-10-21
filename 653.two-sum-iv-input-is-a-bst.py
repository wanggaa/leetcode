#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (56.83%)
# Total Accepted:    22.7K
# Total Submissions: 39.9K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 
# 案例 1:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# 输出: True
# 
# 
# 
# 
# 案例 2:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# 输出: False
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def visit(root):
            if root is None:
                return
            for n in visit(root.left): yield n
            yield root.val
            for n in visit(root.right): yield n

        vals = list(visit(root))
        i,j = 0,len(vals)-1
        while i < j:
            t = vals[i] + vals[j]
            if t == k:
                return True
            if t > k:
                j -= 1
            if t < k:
                i += 1
        return False
        
