#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 相似字符串组
#
# https://leetcode-cn.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (51.66%)
# Total Accepted:    4.2K
# Total Submissions: 8.2K
# Testcase Example:  '1'
#
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
# 
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：1
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：10
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：16
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：24
# 输出：false
# 
# 
# 示例 5：
# 
# 输入：46
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 
# 
#
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        set2 = [1]
        for i in range(10**9):
            t = set2[-1] * 2
            if t > 10 ** 9:
                break
            set2.append(t)
        d_t = []
        for p2 in set2:
            s = str(p2)
            d = {}
            for k in range(10):
                k = str(k)
                t = s.count(k)
                if t:
                    d[k]=t
            d_t.append(d)
        d = {}
        for k in range(10):
            k = str(k)
            N = str(N)
            t = N.count(k)
            if t:
                d[k] = t
        return d in d_t

