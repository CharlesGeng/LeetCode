#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        i = j = 0
        while i < len(pushed):
            if pushed[i] != popped[j]:
                res.append(pushed[i])
            else:
                j += 1
                while j < len(popped) and len(res) > 0:
                    if popped[j] == res[len(res) - 1]:
                        res.pop()
                        j += 1
                    else:
                        break
            i += 1
        return len(res) == 0


# @lc code=end
