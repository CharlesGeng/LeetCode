#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pl = list(pattern)
        sl = s.split()
        if len(pl) != len(sl):
            return False

        myDic = {}
        for i in range(len(pl)):
            if pl[i] not in myDic.keys() and sl[i] not in myDic.values():
                myDic[pl[i]] = sl[i]
            elif pl[i] in myDic.keys() and myDic[pl[i]] != sl[i]:
                return False
            elif pl[i] not in myDic.keys() and sl[i] in myDic.values():
                return False
            else:
                continue
        return True


# @lc code=end
