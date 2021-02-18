#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, maxArea = 0, len(height) - 1, 0
        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea


# @lc code=end
