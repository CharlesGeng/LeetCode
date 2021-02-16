#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result =[]
        for i, v in enumerate(mat):
            sum = 0
            for j in mat[i]:
                if j > 0:
                    sum += j
                else:
                    continue
            result.append([i, sum])

        n = len(result)
        ni = []
        while True:
            if len(ni) < n:
                for i,v in enumerate(result):
                    minIndex = v[0]
                    min = v[1]
                    curI = i
                    for j, w in enumerate(result):
                        if v != w:
                            if w[1] < min or (w[1] == min and w[0]< minIndex):
                                min = w[1]
                                minIndex = w[0]
                                curI = j
                    ni.append(minIndex)
                    del result[curI]
                    
            else:
                break
        return ni[:k]
        
# @lc code=end

