#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {
            "a": min(a, 2 * (b + c + 1)),
            "b": min(b, 2 * (a + c + 1)),
            "c": min(c, 2 * (b + a + 1)),
        }
        rl = sum(d.values())
        result = ""
        for i in range(rl):
            ca = set(["a", "b", "c"])
            if len(result) > 1 and result[-1] == result[-2]:
                ca.remove(result[-1])
            c = max(ca, key=lambda x: d[x])
            result += c
            d[c] -= 1

        return result


# @lc code=end
