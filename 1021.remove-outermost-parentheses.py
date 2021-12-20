#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#


# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        stack = []
        temp = ''
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            temp += c
            if not stack:
                result += temp[1:-1]
                temp = ''
        return result


# @lc code=end
