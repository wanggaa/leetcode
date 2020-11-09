#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# https://leetcode-cn.com/problems/summary-ranges/description/
#
# algorithms
# Medium (53.61%)
# Total Accepted:    15.7K
# Total Submissions: 29.1K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个无重复元素的有序整数数组 nums 。
# 
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
# nums 的数字 x 。
# 
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
# 
# 
# "a->b" ，如果 a != b
# "a" ，如果 a == b
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# 
# 
# 示例 2：
# 
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
# 
# 
# 示例 3：
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 4：
# 
# 输入：nums = [-1]
# 输出：["-1"]
# 
# 
# 示例 5：
# 
# 输入：nums = [0]
# 输出：["0"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中的所有值都 互不相同
# 
# 
#
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return [] 
        pre = nums[0]
        ans = [[pre]]
        for n in nums[1:]:
            if n == pre+1:
                pre = n
                continue
            if n != pre+1:
                if ans[-1][-1] != pre:
                    ans[-1].append(pre)
                pre = n
                ans.append([pre])
        if ans[-1][-1] != nums[-1]:
            ans[-1].append(nums[-1])

        ans = ['%d->%d'%(t[0],t[1]) if len(t) == 2 else '%d'%t[0] for t in ans]
        return ans

