# LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        # Constraints
        # - 1 <= prices.length <= 10^5
        # - 0 <= prices[i] <= 10^4

        # Topic: Two Pointer (Tortoise and Hare)
        # This is also an Array or Dynamic Programming problem.

        # Approach 1:
        # - Define a variable that will serve as the max profit variable. Return this variable 
        # at the end.
        # - Define l,r pointers that are 0,1.
        # - Loop through the prices list while r < len(prices).
        # - If we found that yesterday's prices is less than today's price, see if we need to 
        # update the max profit.
        # - Else, set l equal to r.
        # - Return the answer.

        # TC: O(N)
        # SC: O(1)

        max_profit = 0
        l,r = 0,1
        n = len(prices)
        
        while r < n:
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r
            
            r += 1
        
        return max_profit
