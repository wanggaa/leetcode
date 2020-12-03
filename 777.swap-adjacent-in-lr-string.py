#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 托普利茨矩阵
#
# https://leetcode-cn.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (31.91%)
# Total Accepted:    4.1K
# Total Submissions: 12.9K
# Testcase Example:  '"RXXLRXRXL"\n"XRLXXRRLX"'
#
# 在一个由 'L' , 'R' 和 'X'
# 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时，
# 返回True。
# 
# 
# 
# 示例 :
# 
# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。
# 
# 
#
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start)!=len(end) or start.count('L')!=end.count('L') or start.count('R')!=end.count('R'):
            return False
        sp,ep = 0,0
        while True:
            while sp != len(start) and start[sp] == 'X':
                sp += 1
            while ep != len(end) and end[ep] == 'X':
                ep += 1
            if sp == ep == len(start):
                return True
            if start[sp] == end[ep]:
                if start[sp] == 'L' and sp < ep:
                    return False
                if start[sp] == 'R' and sp > ep:
                    return False
                    

                sp += 1
                ep += 1
            else:
                return False
