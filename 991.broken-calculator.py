#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        counter = 0
        while X < Y:
            counter += 1
            if Y & 1 == 0:
                Y >>= 1
            else:
                Y += 1
        return counter + X - Y


# @lc code=end
