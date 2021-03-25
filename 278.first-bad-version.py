#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        l = 1
        r = n
        while r > l + 1:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        return r


# @lc code=end
