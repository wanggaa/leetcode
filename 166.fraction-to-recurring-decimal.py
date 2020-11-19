#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (27.86%)
# Total Accepted:    17.1K
# Total Submissions: 61.4K
# Testcase Example:  '1\n2'
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
# 
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 
# 如果存在多个答案，只需返回 任意一个 。
# 
# 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：numerator = 1, denominator = 2
# 输出："0.5"
# 
# 
# 示例 2：
# 
# 
# 输入：numerator = 2, denominator = 1
# 输出："2"
# 
# 
# 示例 3：
# 
# 
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"
# 
# 
# 示例 4：
# 
# 
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"
# 
# 
# 示例 5：
# 
# 
# 输入：numerator = 1, denominator = 5
# 输出："0.2"
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# denominator != 0
# 
# 
#
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        symbol = 1
        if numerator == 0:
            return '0'
        if numerator < 0:
            symbol *= -1
            numerator *= -1
        if denominator < 0:
            symbol *= -1
            denominator *= -1

        t = numerator // denominator
        x = numerator % denominator 
        nums = []
        ans = []
        while True:
            if x == 0:
                break
            ans.append(x // denominator)
            x = (x % denominator) * 10
            if x in nums:
                ans.insert(1+nums.index(x),'(')
                ans.append(')')
                break
            nums.append(x)
        
        ans = ans[1:]
        valid = [str(a) for a in ans]
        ans = str(t)
        if len(valid) != 0:
            ans = ans + '.' + ''.join(valid)
        if symbol == -1:
            ans = '-' + ans
        return ans
                
