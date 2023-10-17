# LINK: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution(object):
    def maximumTripletValue(self, nums):
        # Constraints
        # - 3 <= nums.length <= 100
        # - 1 <= nums[i] <= 106

        # Topic: Array
        # This is an Array problem.

        # Approach 1:
        # - Do tripple for loops.
        #   - The left indices for the for loops are: 0,i+1,j+1.
        #   - The right indices for the for loops are: n-2,n-1,n.
        # - Calculate the result.
        # - Return the result.

        # Approach 1 (YouTube):
        # - This is a triple for loop problem (Setup the skeleton first).
        # - The first for loop goes from 0..n-2.
        # - The second for loop goes from i+1..len(n-1).
        # - The thrid for loop goes from i+2..n.

        # TC: O(N^3)
        # SC: O(1)
        
        n = len(nums)
        res = 0

        # TRICK: Make sure to get the upper boundaries correct: n-2,n-1,n.
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        
        return res
