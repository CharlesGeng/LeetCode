#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        m1 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        m2 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        sl = list(s)
        l = len(s)
        i = 0
        while i < l:
            if i + 1 < l and sl[i] + sl[i + 1] in m1.keys():
                sum += m1[sl[i] + sl[i + 1]]
                i += 1
            else:
                sum += m2[sl[i]]
            i += 1
        return sum


# @lc code=end
