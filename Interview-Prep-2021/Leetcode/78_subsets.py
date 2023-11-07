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
        # - Define a 'res' list that will hold all the subsets; define a 'cur' list that will hold the current subset.
        # - We will be utilizing a inner function has a helper (backtrack).
        # - The backtracking starts with index 0.
        # - Inside the backtrack function:
        #   - Append the a copy of cur to res (base case).
        #   - Loop from start..len(nums).
        #   - If nums[i] is not in the cur list, then append it.
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
