#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        j = 0
        for i in pushed:
            res.append(i)
            while res and res[-1] == popped[j]:
                res.pop()
                j += 1
        return len(res) == 0


# @lc code=end
