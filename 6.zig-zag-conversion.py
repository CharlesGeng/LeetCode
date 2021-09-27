#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        counter = 0
        il = list(range(numRows))
        r = list(range(numRows - 1))
        r.reverse()
        il.extend(r[:-1])
        length = len(il)
        htb = {}
        for c in s:
            k = il[counter]
            if k in htb.keys():
                htb[k] += c
            else:
                htb[k] = c
            counter += 1
            if counter == length:
                counter = 0

        result = ""
        for k in htb.keys():
            result += "".join(htb[k])
        return result


# @lc code=end
