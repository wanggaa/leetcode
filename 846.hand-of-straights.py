#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode-cn.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (49.25%)
# Total Accepted:    6K
# Total Submissions: 12.1K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# 爱丽丝有一手（hand）由整数数组给定的牌。 
# 
# 现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。
# 
# 如果她可以完成分组就返回 true，否则返回 false。
# 
# 
# 
# 注意：此题目与 1296
# 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
# 输出：true
# 解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
# 
# 示例 2：
# 
# 
# 输入：hand = [1,2,3,4,5], W = 4
# 输出：false
# 解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 1 
# 
# 
#
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        if W == 1:
            return True

        total = len(hand) // W
        hand.sort()

        minv = []
        count = 0
        sp = 0
        while sp < len(hand):
            if not minv:
                minv.append([hand[sp]])
                sp += 1
                continue
            if minv[count][-1] == hand[sp] - 1:
                minv[count].append(hand[sp])
                if len(minv[count]) == W:
                    minv.pop(count)
                else:
                    count = (1+count) % len(minv)
                sp += 1
                continue
            if len(minv) >= total:
                return False
            minv.append([hand[sp]])
            sp += 1
        if len(minv) != 0:
            return False
        return True
        
        
            
