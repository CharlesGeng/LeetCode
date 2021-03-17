#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = {}
        counter["L"] = 0
        counter["R"] = 0
        result = 0
        for c in s:
            counter[c] += 1
            if counter["L"] == counter["R"]:
                result += 1
                counter["L"] = 0
                counter["R"] = 0
        return result


# @lc code=end
