#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # total rows
        m = len(matrix)
        # total columns
        n = len(matrix[0])

        i, j = 0, 0

        while i < m and j < n:
            if target > matrix[i][j]:
                i += 1
                j += 1
            elif target == matrix[i][j]:
                return True
            else:
                break
        l = j
        while l < n:
            for k in range(i):
                if target == matrix[k][l]:
                    return True
            l += 1

        l = i
        while l < m:
            for k in range(j):
                if i < m and target == matrix[l][k]:
                    return True
            l += 1
        return False


# @lc code=end
