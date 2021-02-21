#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        else:
            temp = Y
            counter = 0
            while X != temp:
                counter += 1
                if temp & 1 == 0 and temp > X:
                    temp >>= 1
                else:
                    temp += 1
            return counter


# @lc code=end
