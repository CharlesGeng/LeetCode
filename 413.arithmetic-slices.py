#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        result = 0
        counter = 0
        for i in range(1, len(A) - 1):
            if (A[i + 1] - A[i]) == (A[i] - A[i - 1]):
                counter += 1
            else:
                result += (counter + 1) * counter // 2
                counter = 0
        result += (counter + 1) * counter // 2
        return result


# @lc code=end
