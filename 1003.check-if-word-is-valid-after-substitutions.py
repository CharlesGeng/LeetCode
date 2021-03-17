#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if "abc" in s:
                s = s.replace("abc", "")
            elif len(s) == 0:
                return True
            else:
                return False


# @lc code=end
