#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Reverse string
        sn = s[::-1]
        l = len(sn)
        maxSub = ""
        for i in range(l):
            #
            if l - i < len(maxSub):
                break
            sub = sn[i]
            for j in range(i + 1, l):
                if sub + sn[j] in s:
                    sub += sn[j]
                else:
                    break
            if len(sub) > len(maxSub) and sub == sub[::-1]:
                maxSub = sub
            # print(sub)
        return maxSub


# @lc code=end
