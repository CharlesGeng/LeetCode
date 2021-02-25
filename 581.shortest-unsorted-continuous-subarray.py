#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = nums.copy()
        sortedNums.sort()
        l = -1
        for i in range(len(nums)):
            if sortedNums[i] != nums[i]:
                l = i
                break
        if l == -1:
            return 0

        j = len(nums) - 1
        while j > i:
            if sortedNums[j] != nums[j]:
                break
            else:
                j -= 1
        return j - l + 1


# @lc code=end
