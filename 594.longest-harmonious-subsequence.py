#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        else:
            d = {}
            min = nums[0]
            max = nums[0]
            for i in nums:
                if i < min:
                    min = i
                if max < i:
                    max = i
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            if min == max:
                return 0
            else:
                ml = 0
                for i in d:
                    if i + 1 in d and ml < d[i] + d[i + 1]:
                        ml = d[i] + d[i + 1]
                    if i - 1 in d and ml < d[i] + d[i - 1]:
                        ml = d[i] + d[i - 1]
                return ml


# @lc code=end
