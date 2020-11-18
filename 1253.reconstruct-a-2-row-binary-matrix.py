#
# @lc app=leetcode.cn id=1253 lang=python3
#
# [1253] 将矩阵按对角线排序
#
# https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix/description/
#
# algorithms
# Medium (38.37%)
# Total Accepted:    4K
# Total Submissions: 10.4K
# Testcase Example:  '2\n1\n[1,1,1]'
#
# 给你一个 2 行 n 列的二进制数组：
# 
# 
# 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
# 第 0 行的元素之和为 upper。
# 第 1 行的元素之和为 lower。
# 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
# 
# 
# 你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
# 
# 如果有多个不同的答案，那么任意一个都可以通过本题。
# 
# 如果不存在符合要求的答案，就请返回一个空的二维数组。
# 
# 
# 
# 示例 1：
# 
# 输入：upper = 2, lower = 1, colsum = [1,1,1]
# 输出：[[1,1,0],[0,0,1]]
# 解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
# 
# 
# 示例 2：
# 
# 输入：upper = 2, lower = 3, colsum = [2,2,1,1]
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# 输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2
# 
# 
#
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        uprow = []
        lorow = []

        def back(c,up,lo):
            if up < 0 or lo < 0:
                return False

            if c == len(colsum):
                if up == 0 and lo == 0:
                    return True
                return False

            if colsum[c] == 0:
                uprow.append(0)
                lorow.append(0)
                if back(c+1,up,lo):
                    return True
            if colsum[c] == 2:
                uprow.append(1)
                lorow.append(1)
                if back(c+1,up-1,lo-1):
                    return True 
            if colsum[c] == 1:
                uprow.append(1)
                lorow.append(0)
                if back(c+1,up-1,lo):
                    return True
                uprow[-1] = 0
                lorow[-1] = 1
                if back(c+1,up,lo-1):
                    return True
            uprow.pop(-1)
            lorow.pop(-1)
            return False

        def construct(c,up,lo):
            if c == len(colsum):
                return 
            if colsum[c] == 0:
                uprow.append(0)
                lorow.append(0)
                construct(c+1,up,lo)
            if colsum[c] == 2:
                uprow.append(1)
                lorow.append(1)
                construct(c+1,up-1,lo-1)
            if colsum[c] == 1:
                if up >= lo:
                    uprow.append(1)
                    lorow.append(0)
                    construct(c+1,up-1,lo)
                else:
                    uprow.append(0)
                    lorow.append(1)
                    construct(c+1,up,lo-1)

        if sum(colsum) != upper+lower:
            return []
        if upper < colsum.count(2) or lower < colsum.count(2):
            return []
        construct(0,upper,lower)
        return [uprow,lorow]
