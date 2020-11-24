#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] Powerful Integers
#
# https://leetcode-cn.com/problems/powerful-integers/description/
#
# algorithms
# Easy (40.35%)
# Total Accepted:    8.7K
# Total Submissions: 21.6K
# Testcase Example:  '2\n3\n10'
#
# 给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
# 
# 返回值小于或等于 bound 的所有强整数组成的列表。
# 
# 你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释： 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 
# 示例 2：
# 
# 输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
# 
# 
#
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        import math
        ans = set()
        xp,yp = [1],[1]
        
        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        if x != 1:
            while xp[-1] < bound:
                xp.append(xp[-1]*x)
        if y != 1:
            while yp[-1] < bound:
                yp.append(yp[-1]*y)
        
        for x in xp:
            for y in yp:
                if x+y>bound:
                    continue
                ans.add(x+y)
        return ans
        
