#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#
# https://leetcode-cn.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (56.94%)
# Total Accepted:    3.9K
# Total Submissions: 6.8K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
#  '[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 实现一个带有buildDict, 以及 search方法的魔法字典。
# 
# 对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。
# 
# 对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
# 
# 示例 1:
# 
# 
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# 
# 
# 注意:
# 
# 
# 你可以假设所有输入都是小写字母 a-z。
# 为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。
# 请记住重置MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅这里了解更多详情。
# 
# 
#
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.alpha = 'abcdefghijklmnopqrstuvwxyz' 

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set()
        for word in dictionary:
            for i in range(len(word)):
                for c in self.alpha:
                    t = list(word)
                    t[i] = c
                    t = ''.join(t)
                    if t == word:
                        continue
                    self.words.add(t)

    def search(self, searchWord: str) -> bool:
        if searchWord in self.words:
            return True
        else:
            return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
