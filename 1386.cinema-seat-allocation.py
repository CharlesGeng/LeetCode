#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#

# @lc code=start
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        result = 2 * n
        fp2 = 0b01111111100
        fp11 = 0b00011110000
        fp12 = 0b01111000000
        fp13 = 0b00000111100
        rlh = {}

        for item in reservedSeats:
            if item[0] in rlh.keys():
                rlh[item[0]] += 1 << item[1]
            else:
                rlh[item[0]] = 1 << item[1]
        for k in rlh.keys():
            if rlh[k] & fp2 == 0:
                continue
            elif rlh[k] & fp11 == 0 or rlh[k] & fp12 == 0 or rlh[k] & fp13 == 0:
                result -= 1
            else:
                result -= 2

        return result


# @lc code=end
