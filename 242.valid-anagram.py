#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for c in s:
            if c not in m.keys():
                m[c] = 1
            else:
                m[c] += 1

        for i, c in enumerate(t):
            if c not in m.keys() or m[c] < 1:
                return False
            else:
                m[c] -= 1

        return True


# @lc code=end
