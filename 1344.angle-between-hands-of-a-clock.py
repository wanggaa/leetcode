#
# @lc app=leetcode.cn id=1344 lang=python3
#
# [1344] 最大相等频率
#
# https://leetcode-cn.com/problems/angle-between-hands-of-a-clock/description/
#
# algorithms
# Medium (58.93%)
# Total Accepted:    3.8K
# Total Submissions: 6.4K
# Testcase Example:  '12\n30'
#
# 给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：hour = 12, minutes = 30
# 输出：165
# 
# 
# 示例 2：
# 
# 
# 
# 输入：hour = 3, minutes = 30
# 输出；75
# 
# 
# 示例 3：
# 
# 
# 
# 输入：hour = 3, minutes = 15
# 输出：7.5
# 
# 
# 示例 4：
# 
# 输入：hour = 4, minutes = 50
# 输出：155
# 
# 
# 示例 5：
# 
# 输入：hour = 12, minutes = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= hour <= 12
# 0 <= minutes <= 59
# 与标准答案误差在 10^-5 以内的结果都被视为正确结果。
# 
# 
#
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour%12)/12. + minutes/720.
        m = minutes/60.
        t = abs(h-m)
        t = min(t,1-t)
        return t*360