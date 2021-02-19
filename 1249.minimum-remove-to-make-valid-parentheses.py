#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lp = []
        rp = []
        result = list(s)
        for i, c in enumerate(s):
            if c == "(":
                lp.append(i)
            elif c == ")":
                if len(lp) > 0:
                    lp.pop()
                else:
                    rp.append(i)
        lp += rp
        for i in lp:
            result[i] = ""
        return "".join(result)


# @lc code=end
