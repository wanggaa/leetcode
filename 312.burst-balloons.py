#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (67.15%)
# Total Accepted:    32.9K
# Total Submissions: 49K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 说明:
# 
# 
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 示例:
# 
# 输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
#
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp_dict = {}

        def dp(i,j):
            if j-i < 2:
                return 0
            ans = []
            for t in range(i+1,j):
                if (i,t) not in dp_dict:
                    dp_dict[(i,t)] = dp(i,t)
                l_ans = dp_dict[(i,t)]
                if (t,j) not in dp_dict:
                    dp_dict[(t,j)] = dp(t,j)
                r_ans = dp_dict[(t,j)]
                ans.append(nums[i]*nums[t]*nums[j]+l_ans+r_ans)
            return max(ans)
        
        return dp(0,len(nums)-1)
