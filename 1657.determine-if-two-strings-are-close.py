#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hw1, hw2 = Counter(word1), Counter(word2)
        if hw1.keys() == hw2.keys() and sorted(hw1.values()) == sorted(hw2.values()):
            return True

        return False

    # @lc code=end
