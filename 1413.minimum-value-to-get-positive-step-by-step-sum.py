#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#


# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # ***************************************************
        # ############ My Solution ################
        # startValue = 1
        # sum = 0
        # for i in nums:
        #     sum += i
        #     if startValue + sum < 1:
        #         startValue = -sum + 1
        # return startValue
        # ***************************************************
        return 1 - min(accumulate(nums, initial=0))


# @lc code=end
