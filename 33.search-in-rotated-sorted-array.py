#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (39.31%)
# Total Accepted:    187.3K
# Total Submissions: 475.2K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 给你一个升序排列的整数数组 nums ，和一个整数 target 。
# 
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
# 
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：nums = [1], target = 0
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4 
# 
# 
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def psobsearch(A,l,r):
            print(A[l:r+1])
            if l > r:
                return -1
            if A[r] <= target <= A[l]:
                if target == A[r]:
                    return r
                if target == A[l]:
                    return l
                return -1

            mid = (l+r)//2
            if target == A[mid]:
                return mid

            # target in <-r
            if target < A[r]:
                # mid in <-r
                if A[mid] < A[r]:
                    if A[mid] < target:
                        return bsearch(A,mid+1,r-1)
                    if A[mid] > target:
                        return psobsearch(A,l+1,mid-1)
                #mid in l->
                if A[mid] > A[l]:
                    return psobsearch(A,mid+1,r-1)
            # target in l->
            if target > A[l]:
                # mid in l->
                if A[mid] > A[l]:
                    if A[mid] > target:
                        return psobsearch(A,mid+1,r-1)
                    if A[mid] < target:
                        return bsearch(A,l+1,mid-1)
                # mid in <-r
                if A[mid] < A[r]:
                    return psobsearch(A,l+1,mid-1)

        def bsearch(A,l,r):
            while l <= r:
                mid = (l+r)//2
                if A[mid] == target:
                    return mid
                if A[mid] > target:
                    r = mid - 1
                if A[mid] < target:
                    l = mid + 1
            return -1
        if len(nums) < 10**3:
            if target not in nums:
                return -1
            return nums.index(target)
        target = target
        ans = psobsearch(nums,0,len(nums)-1)
        return ans



