Problem:
Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

Approach:
Brute Force (Check All Pairs)

Why this works:
Try all possible (buy, sell) pair and update the 'prof' value if it is greater than current 'prof' value

Time Complexity:
O(n²)
Two nested loops check all possible buy–sell pairs.

Space Complexity:
O(1)
  
# ----------------------------------
# Brute-force solution
# ----------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if (prices[j] - prices[i]) > prof:
                    prof = prices[j] - prices[i]
        return prof
