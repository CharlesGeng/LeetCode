#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        for w in d:
            i = 0
            flag = True
            for c in w:
                if c in s[i:]:
                    i += s[i:].index(c) + 1
                else:
                    flag = False
                    break
            if flag and (len(w) > len(res) or (len(res) == len(w) and w[0] < res[0])):
                res = w
        return res


# @lc code=end
