#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (58.19%)
# Total Accepted:    55K
# Total Submissions: 94.7K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1nums = []
        while l1:
            l1nums.append(l1.val)
            l1 = l1.next
        l2nums = []
        while l2:
            l2nums.append(l2.val)
            l2 = l2.next
        num1 = int(''.join([str(x) for x in l1nums])) 
        num2 = int(''.join([str(x) for x in l2nums]))
        ans = num1 + num2
        head = p = ListNode(-1)
        for c in str(ans):
            p.next = ListNode(int(c))
            p = p.next
        return head.next
        
       
        

