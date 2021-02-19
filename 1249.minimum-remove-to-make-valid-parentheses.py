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
        result = []
        for i, c in enumerate(s):
            if c == "(":
                lp.append(i)
            elif c == ")":
                if len(lp) > 0:
                    lp.pop(len(lp) - 1)
                else:
                    rp.append(i)
            result.append(c)
        lp += rp
        up = sorted(lp)
        up.reverse()
        for i in up:
            result.pop(i)
        return "".join(result)


# @lc code=end
