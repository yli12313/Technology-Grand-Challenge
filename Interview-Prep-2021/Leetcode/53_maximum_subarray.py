# LINK: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        # Constraints:
        # - 1 <= nums.length <= 10^5
        # - -10^4 <= nums[i] <= 10^4

        # Topic: Array.
        # This is correct! This is an Array, Divide and Conquer, and Dynamic Programming problem.

        # Approach 1: Kadane's Algorithm from three years ago.

        """
        # TC: O(N)
        # SC: O(1)

        cur = nums[0]
        best = nums[0]

        # Make sure that you starting looping starting from the 1st index.
        for n in nums[1:]:
            cur = max(n, n+cur)
            best = max(best, cur)
        
        return best
        """

        # Approach 1: Kadane's Algorithm from Neetcode.

        # TC: O(N)
        # SC: O(1)

        # NOTE: I don't fully understand how the algorithm works exactly,
        # but this video helps a lot (https://www.youtube.com/shorts/Az8S1ZGpV_M).
        # Let me keep trying! 

        best = nums[0]
        # Make sure to set cur to 0.
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            
            cur += n
            best = max(best, cur)
        
        return best