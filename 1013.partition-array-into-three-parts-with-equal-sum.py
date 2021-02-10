#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 == 0:
            sub = csub = s // 3
            count = 0
            for v in arr:
                sub -= v
                if sub == 0:
                    sub = csub
                    count += 1
            if count >= 3:
                return True

        return False


# @lc code=end
