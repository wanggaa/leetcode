#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (47.37%)
# Total Accepted:    11.6K
# Total Submissions: 24.5K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# 
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
# 
# 若无答案，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：
# words = ["w","wo","wor","worl", "world"]
# 输出："world"
# 解释： 
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
# 
# 
# 示例 2：
# 
# 输入：
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出："apple"
# 解释：
# "apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
# 
# 
# 
# 
# 提示：
# 
# 
# 所有输入的字符串都只包含小写字母。
# words数组长度范围为[1,1000]。
# words[i]的长度范围为[1,30]。
# 
# 
#
class Solution:
    def longestWord(self, words: List[str]) -> str:
        dword = {}
        for word in words:
            t = len(word)
            if t in dword:
                dword[t].append(word)
            else:
                dword[t] = [word]
        
        valid = dword[1]
        length = 2
        while True:
            next_valid = []
            for word in dword.get(length,[]):
                if word[:-1] in valid:
                    next_valid.append(word)
            if not next_valid:
                break
            valid = next_valid
            length += 1
        valid.sort()
        return valid[0]

               
