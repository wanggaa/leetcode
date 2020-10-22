#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 非重叠矩形中的随机点
#
# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (39.05%)
# Total Accepted:    42.1K
# Total Submissions: 107.7K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# 给定一副牌，每张牌上都写着一个整数。
# 
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 
# 
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 
# 
# 仅当你可选的 X >= 2 时返回 true。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 
# 
# 示例 2：
# 
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 3：
# 
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 4：
# 
# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 
# 
# 示例 5：
# 
# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
# 
# 
# 
# 提示：
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
# 
# 
# 
# 
#
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1:
            return False
        def common(x,y):
            while y%x != 0:
                t = x
                x = y%x
                y = t
            return x

        vdict = {}
        for n in deck:
            vdict[n] = vdict.get(n,0) + 1

        nums = []
        for k in vdict:
            nums.append(vdict[k])

        print(nums)
        while len(nums) > 1:
            x = nums.pop(-1)
            y = nums.pop(-1)
            t = common(x,y)
            if t == 1:
                return False
            nums.append(t)
        return True
