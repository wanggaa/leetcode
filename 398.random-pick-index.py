#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#
# https://leetcode-cn.com/problems/random-pick-index/description/
#
# algorithms
# Medium (62.87%)
# Total Accepted:    8.3K
# Total Submissions: 13.2K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
# 
# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
# 
# 示例:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
# solution.pick(3);
# 
# // pick(1) 应该返回 0。因为只有nums[0]等于1。
# solution.pick(1);
# 
# 
#
class Solution:

    def __init__(self, nums: List[int]):
        import random
        self.d = {}
        for i in range(len(nums)):
            if nums[i] not in self.d:
                self.d[nums[i]] = []
            self.d[nums[i]].append(i)

    def pick(self, target: int) -> int:
        t = self.d[target]
        return random.choice(t)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
