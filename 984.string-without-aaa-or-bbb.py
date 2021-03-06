#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 移除最多的同行或同列石头
#
# https://leetcode-cn.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Medium (39.30%)
# Total Accepted:    5.9K
# Total Submissions: 15.1K
# Testcase Example:  '1\n2'
#
# 给定两个整数 A 和 B，返回任意字符串 S，要求满足：
# 
# 
# S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
# 子串 'aaa' 没有出现在 S 中；
# 子串 'bbb' 没有出现在 S 中。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = 1, B = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
# 
# 
# 示例 2：
# 
# 输入：A = 4, B = 1
# 输出："aabaa"
# 
# 
# 
# 提示：
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# 对于给定的 A 和 B，保证存在满足要求的 S。
# 
# 
#
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        a,b = max(A,B),min(A,B)
        s_ans = ''
        while a > b and b != 0:
            s_ans += 'aab'
            a -= 2
            b -= 1
        if a == b:
            s_ans += 'ab'* a
        if b == 0:
            s_ans += 'a' * a
        if A<B:
            s_ans = ''.join(['b' if c == 'a' else 'a' for c in s_ans])
        return s_ans

