#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minPrice:
                profit += prices[i] - minPrice
            minPrice = prices[i]
        return profit


# @lc code=end
