#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        for i in s:
            if i == "." or i == "":
                continue
            elif i == "..":
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        return "/" + "/".join(stack)


# @lc code=end