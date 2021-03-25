#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = len(nums) + 1
        res = []
        for i in range(1, n):
            if i not in s:
                res.append(i)
        return res


# @lc code=end
