#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
# https://leetcode-cn.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (72.46%)
# Total Accepted:    13.7K
# Total Submissions: 18.9K
# Testcase Example:  '13'
#
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。
# 
# 例如，
# 
# 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
# 
# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
# 
#
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        strs = [str(n) for n in range(1,n+1)]
        strs.sort()
        return [int(s) for s in strs] 
