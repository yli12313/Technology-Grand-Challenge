# LINK: https://leetcode.com/problems/subsets/

class Solution(object):

    def subsets(self, nums):
        # Constraints: 
        # - 1 <= nums.length <= 10.
        # - -10 <= nums[i] <= 10.
        # - All the numbers of nums are unique.

        # Topic: Backtracking
        # This is an Array, Backtracking, or Bit Manipulation problem.

        # Approach 1:
        # - Define a 'res' and 'cur' list that will hold the results and the current subset being processed.
        # Return res as part of the code skeleton.
        # - We are going to utilize a helper function 'backtrack'. We call this function starting with index 0.
        # - Inside the backtrack() function:
        #   - Append the a copy of cur to res.
        #   - Loop from start..len(nums), with index i.
        #   - If the current value with index i is not in cur, then append it.
        #   - Call backtrack with i+1.
        #   - Call the pop() function to remove the last value in this path, so that you can use backtracking to explore 
        #   other paths that may result in a valid subset.

        # TC: O(N*2^N)
        # SC: O(N*2^N)

        res = []
        cur = []

        def backtrack(start):
            res.append(cur[:])

            # TRICK: The loop goes from start..len(nums).
            for i in range(start, len(nums)):
                # TRICK: Check the following -> 'if nums[i] not in cur:'.
                if nums[i] not in cur:
                    cur.append(nums[i])
                    backtrack(i+1)
                    cur.pop()

        backtrack(0)
        return res
