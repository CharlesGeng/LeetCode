#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 0:
        #     return False
        # n &= n - 1
        # return n == 0
        return n > 0 and not (n & (n - 1))


# @lc code=end
