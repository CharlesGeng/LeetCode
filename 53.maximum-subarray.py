#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        maxCurrent = nums[0]
        for i in range(1, len(nums)):
            maxCurrent = maxCurrent + nums[i] if maxCurrent > 0 else nums[i]
            maxVal = max(maxCurrent, maxVal)
        return maxVal


# @lc code=end
