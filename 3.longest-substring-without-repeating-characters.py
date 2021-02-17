#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        maxSub = 0
        for c in s:
            if c in sub:
                maxSub = max(maxSub, len(sub))
                sub = sub[sub.index(c) + 1 :]
            sub += c
        return max(maxSub, len(sub))


# @lc code=end
