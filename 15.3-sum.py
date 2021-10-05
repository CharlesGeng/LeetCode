#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    lv = nums[l]
                    rv = nums[r]
                    while l + 1 < r and lv == nums[l + 1]:
                        l += 1
                    while r - 1 > l and rv == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result


# @lc code=end
