#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = nums[0]
        for (i, v) in enumerate(nums):
             if v != n:
                 n = v
                 nums[k] = n
                 k = k +1
        return k
             
        
# @lc code=end

