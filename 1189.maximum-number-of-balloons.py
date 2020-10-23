#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] 加密数字
#
# https://leetcode-cn.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (63.75%)
# Total Accepted:    14.5K
# Total Submissions: 22.8K
# Testcase Example:  '"nlaebolko"'
#
# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
# 
# 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：text = "nlaebolko"
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 
# 输入：text = "loonbalxballpoon"
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：text = "leetcode"
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 10^4
# text 全部由小写英文字母组成
# 
# 
#
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dalpha = {}
        for n in text:
            dalpha[n] = dalpha.get(n,0) + 1
        minv = float('inf')
        for k in 'balon':
            if k == 'l' or k == 'o':
                t = dalpha.get(k,0)//2
            else:
                t = dalpha.get(k,0)
            minv = min(minv,t)
        return minv
