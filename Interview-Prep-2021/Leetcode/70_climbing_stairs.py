# LINK: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        # Constraints
        # - 1 <= n <= 45

        # Topic: Dynamic Programming
        # This is a Math, Dynamic Programming or Memoization problem.

        # Approach 1 (iterative):
        # - Treat the n == 1 case.
        # - Define first and second as 1 and 2.
        # - Loop from 3..n+1.
        # - Update third, first and second. 
        # - Return second.

        # TC: O(N)
        # SC: O(1)

        if n == 1:
            return 1
        
        first = 1
        second = 2
        
        for i in range(3,n+1):
            third = first+second
            first = second
            second = third
        
        return second

        # Approach 1 (dynamic programming):
        # - Define an array that will store previously computed values
        # of size n. 
        # - If n == 1, update the first value in the results array.
        # - Else if n == 2, update the first and the second value in the
        # results array.
        # - Loop from 3..n+1.
        # - Update the results array.
        # - Return the right most value in the results array.

        res = [0]*n
        if n == 1:
            res[0] = 1
        elif n == 2:
            res[0] = 1
            res[1] = 2
        
        for i in range(3,n+1):
            res[i] = res[i-1]+res[i-2]

        return res[n-1]

foo = Solution();
print(foo.climbStairs(3))
