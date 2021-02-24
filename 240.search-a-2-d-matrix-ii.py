#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix[0]) - 1
        for row in matrix:
            while i and row[i] > target:
                i -= 1
            if row[i] == target:
                return True
        return False


# @lc code=end
