#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        edgeInt = int("80000000", 16)
        s = s.strip()
        result = 0
        index = 0
        positive = True
        if len(s) > 0:
            if s[index] in ["+", "-"]:
                positive = True if s[index] == "+" else False
                index = index + 1

            for c in s[index:]:
                if str.isdigit(c):
                    result = result * 10 + int(c)
                else:
                    break
            if positive and result >= edgeInt:
                result = edgeInt - 1
            if not positive and result > edgeInt:
                result = edgeInt
        return result if positive else -result

        # @lc code=end
