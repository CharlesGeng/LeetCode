#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            if (target - v) in m.keys():
                return [m[target - v], i]
            else:
                m[v] = i


# @lc code=end
