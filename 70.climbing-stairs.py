#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = {}

    def climbStairs(self, n: int) -> int:
        if n in self.result.keys():
            return self.result[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.result[n] = steps
        return steps


# @lc code=end
