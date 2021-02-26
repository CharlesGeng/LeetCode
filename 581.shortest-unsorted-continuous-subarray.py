#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return (
            0
            if all(is_same)
            else len(nums) - is_same.index(False) - is_same[::-1].index(False)
        )


# @lc code=end
