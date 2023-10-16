# LINK: https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        # Constraints
        # - 1 <= nums.length <= 6
        # - -10 <= nums[i] <= 10
        # - All the integers of nums are unique.

        # Topic: Backtracking
        # This is an Array or Backtracking problem.

        # Approach 1:
        # - Milestone #1: Set up the skeleton of the problem.
        # - Define a result list res that will hold the answers.
        # - Define and call the backtrack method with parameters: res, [], and nums.
        # - Return res.

        # TC: O(N!); TC is determined by the number of permutations which is N!.
        # SC: O(N); SC is determined by the depth of the recursion stack which is
        # at most N.

        res = []
        self.backtrack(res, [], nums)
        return res
    
    def backtrack(self,result,container,nums):
        # - Milestone #2: Define an auxiliary method backtrack that will perform
        # the backtracking.
        # - Check that the length of the container is equal to the length of nums.
        # - If so, append a copy of the container to the result.
        # - Define a for() loop that goes from 0..len(nums).
        # - Within the for() loop, check to see if the current value indexed by i is in the 
        # container. If so, continue.
        # - Append the value in nums indexed by i to the container.
        # - Call the backtrack() method.
        # - Pop() the rightmost element from the container so that the recursive calls to 
        # backtrack() can find all the other permutation.

        if len(container) == len(nums):
            result.append(container[:])
            return
            
        for i in range(len(nums)):
            v = nums[i]

            if v in container:
                continue
                
            container.append(v)
            self.backtrack(result,container,nums)
            container.pop()
