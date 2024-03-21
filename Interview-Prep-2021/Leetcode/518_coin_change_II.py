# LINK: https://leetcode.com/problems/coin-change-ii/

class Solution(object):
    def change(self, amount, coins):
        # Constraints:
        # - 1 <= coins.length <= 300
        # - 1 <= coins[i] <= 5000
        # - All the values of coins are unique.
        # - 0 <= amount <= 5000

        # Topic: Dynamic Programming
        # This is an Array or Dynamic Programming problem.

        # Approach 1:
        # - Initialize a list of size 'amount+1' with every element set to 0.
        # Stores the number of combinations for each amount from 0 to amount.
        # - Set dp[0] = 1 (because there's one way to make amount 0, choose no 
        # coins!).
        # - For each coin 'c' in 'coins', iterate over 'dp' from c to amount.
        # - For each 'i', increment 'dp[i]' by 'dp[i-c]'. What does this mean?
        # For each coin, we are adding the number of ways we can make up the amount
        # 'i - c' to the number of ways we can make up the amount 'i'. This effectively
        # counts all combinations that include the current coin. 
        # - Return 'dp[amount]'.

        # TC: O(N*M), where N is the amount and M is the number of different coins.
        # SC: O(N), where N is the amount.

        dp = [0]*(amount+1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]

        return dp[amount]
