#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sl = s.split()
        return (
            len(pattern) == len(sl)
            and len(set(pattern)) == len(set(sl))
            and len(set(zip(pattern, sl))) == len(set(pattern))
        )
        # and len(set(pattern)) == len(set(sl))


# @lc code=end
