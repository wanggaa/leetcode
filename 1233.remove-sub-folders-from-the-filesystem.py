#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 矩形内船只的数目
#
# https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/description/
#
# algorithms
# Medium (46.25%)
# Total Accepted:    5.7K
# Total Submissions: 12.3K
# Testcase Example:  '["/a","/a/b","/c/d","/c/d/e","/c/f"]'
#
# 你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
# 
# 我们这样定义「子文件夹」：
# 
# 
# 如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的子文件夹。
# 
# 
# 文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：
# 
# 
# / 后跟一个或者多个小写英文字母。
# 
# 
# 例如，/leetcode 和 /leetcode/problems 都是有效的路径，而空字符串和 / 不是。
# 
# 
# 
# 示例 1：
# 
# 输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# 输出：["/a","/c/d","/c/f"]
# 解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。
# 
# 
# 示例 2：
# 
# 输入：folder = ["/a","/a/b/c","/a/b/d"]
# 输出：["/a"]
# 解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。
# 
# 
# 示例 3：
# 
# 输入：folder = ["/a/b/c","/a/b/d","/a/b/ca"]
# 输出：["/a/b/c","/a/b/ca","/a/b/d"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= folder.length <= 4 * 10^4
# 2 <= folder[i].length <= 100
# folder[i] 只包含小写字母和 /
# folder[i] 总是以字符 / 起始
# 每个文件夹名都是唯一的
# 
# 
#
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        if '/' in folder:
            return '/'

        fs = [f[1:].split('/') for f in folder]
        def subFolders(fs):
            if [] in fs:
                return [[]]
            d = {}
            for i in range(len(fs)):
                t = fs[i][0]
                if t not in d:
                    d[t] = []
                d[t].append(i)
            ans = []
            for k in d.keys():
                t = [fs[i][1:] for i in d[k]]
                ans += [[k] + v for v in subFolders(t)]
            return ans
        
        answers = ['/'+'/'.join(a) for a in subFolders(fs)]
        return answers
