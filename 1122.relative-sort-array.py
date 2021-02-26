#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = {}
        ue = []
        res = []
        for i in arr2:
            m[i] = []
        for i in arr1:
            if i in m.keys():
                m[i].append(i)
            else:
                ue.append(i)
        for i in arr2:
            res.extend(m[i])
        res.extend(sorted(ue))
        return res


# @lc code=end
