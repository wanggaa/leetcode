#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (36.24%)
# Total Accepted:    14.5K
# Total Submissions: 39.8K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
# 
# 示例 1:
# 
# 
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 
# 
# 示例 2:
# 
# 
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 
# 
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
# 
#
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = []
        count = []
        
        for i,n in enumerate(nums):
            if i == 0:
                length.append(1)
                count.append(1)
                continue

            # add 1 number index
            indexes = [i for i in range(len(length)) if n > nums[i]]
            
            t_len = [length[i] for i in indexes]
            max_t = max(t_len,default=0)
            t_count = [count[i] for i in indexes if length[i]==max_t]

            length.append(max_t+1)
            count.append(max(sum(t_count),1))

            # end with n,maxlength = length[n],total number
        ans = 0
        max_length = max(length)
        for i in range(len(length)):
            if length[i] == max_length:
                ans += count[i]
        return ans  



        
