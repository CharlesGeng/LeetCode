#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = S.lower()
        result = [""]
        for c in S:
            n = len(result)
            C = c.upper() if c.isalpha() else ""
            for i in range(n):
                result[i] += c
            if C != "":
                result = result * 2
                for i in range(n, 2 * n):
                    result[i] = result[i][:-1] + C
        return result


# @lc code=end
