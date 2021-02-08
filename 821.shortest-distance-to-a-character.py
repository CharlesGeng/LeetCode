#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        occ = []

        # Get index of c
        for i, t in enumerate(s):
            if c == t:
                occ.append(i)

        # Generate Results
        for i in range(len(s)):
            min = len(s)
            for j in occ:
                if abs(i - j) < min:
                    min = abs(i - j)
                if i < j:
                    break
            answer.append(min)
        return answer


# @lc code=end
