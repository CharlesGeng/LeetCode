#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ls1 = list(s1)
        ls2 = list(s2)
        counter = []
        for i in range(len(ls1)):
            if ls1[i] != ls2[i]:
                counter.append(i)
            if len(counter) > 2:
                break
        if len(counter) == 0 or (
            len(counter) == 2
            and ls1[counter[0]] == ls2[counter[1]]
            and ls2[counter[0]] == ls1[counter[1]]
        ):
            return True
        else:
            return False


# @lc code=end
