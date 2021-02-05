#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        results = []
        for i in range(0, len(words)):
            for j in range(0, len(words)):
                if i != j and words[i] in words[j]:
                    results.append(words[i])
                    break
        return results


# @lc code=end
