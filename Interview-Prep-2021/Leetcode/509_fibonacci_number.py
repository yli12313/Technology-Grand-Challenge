# LINK: https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        # Constraints:
        # - 0 <= n <= 30

        # Topics: Dynamic Programming
        # This is a Math, Dynamic Programming, Recursion, or Memoization problem.

        # Approach 1:
        # - This is a very standard approach. Just be careful of the following edge cases:
        # -   1) 'n < 0'
        # -   2) 'n == 0'
        # -   3) 'n == 1 or n == 2'
        # - Moreover, you need to initialize n-elements in the dp array.
        # - You loop from 2 --> n.
        # - But in the end, you return the value at 'dp[n-1]'. 
        # - Keep going and keep practicing!

        if n < 0:
            return None
        
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n-1]
