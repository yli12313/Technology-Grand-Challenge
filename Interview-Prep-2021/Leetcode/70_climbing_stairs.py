# LINK: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        # Constraints
        # - 1 <= n <= 45

        # Topic: Dynamic Programming
        # This could also be a Math, Dynamic Programming, or Memoization problem.

        # Approach 1 (dynamic programming):
        # - Define a results array that will host the answer.
        # - Treat the n == 1 case ans n >= 2 case.
        # - Loop from 2..n.
        # - Update the results array.
        # - Return the right most element in the results array.

        # TC: O(N)
        # SC: O(N)

        """
        res = [0]*n
        if n == 1:
            res[0] = 1
        elif n >= 2:
            res[0] = 1
            res[1] = 2
        
        for i in range(2,n):
            res[i] = res[i-1]+res[i-2]
        
        return res[n-1]
        """

        # Approach 2: (iterative):
        # - Treat the n == 1 case.
        # - Define first and second and set them to 1,2.
        # - Loop from 3..n+1.
        # - Create a variable third that's first+second.
        # - Update first; update second.
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
