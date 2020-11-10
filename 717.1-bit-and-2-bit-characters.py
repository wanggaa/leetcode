#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#
# https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (49.67%)
# Total Accepted:    22.6K
# Total Submissions: 45.3K
# Testcase Example:  '[1,0,0]'
#
# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
# 
# 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
# 
# 示例 1:
# 
# 
# 输入: 
# bits = [1, 0, 0]
# 输出: True
# 解释: 
# 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# bits = [1, 1, 1, 0]
# 输出: False
# 解释: 
# 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
# 
# 
# 注意:
# 
# 
# 1 <= len(bits) <= 1000.
# bits[i] 总是0 或 1.
# 
# 
#
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0:
            return False
        if len(bits) == 1:
            return bits[0] == 0
        valid = [True]
        valid.append(bits[0] == 0)
        for i in range(1,len(bits)):
            if bits[i] == 0 and valid[-1] == True:
                valid.append(True)
            elif bits[i] == 0 and bits[i-1] == 1 and valid[-2] == True:
                valid.append(True)
            elif bits[i] == 1 and bits[i-1] == 1 and valid[-2] == True:
                valid.append(True)
            else:
                valid.append(False)
         
        if valid[-3] == True and bits[-2] == 1:
            return False
        return valid[-1]
            
