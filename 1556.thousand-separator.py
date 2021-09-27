#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        t = list(str(n))
        i = len(t)
        while i > 0:
            if i > 3:
                t.insert(i - 3, ".")
            i -= 3
        return "".join(t)


# @lc code=end
