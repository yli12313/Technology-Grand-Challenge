# Link: https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        # Define the resulting list
        result = []

        # Kick off backtracking and recursion
        self.backtracking(xrange(1, n+1), k, 0, [], result)

        # Return the result
        return result
        
        
    def backtracking(self, nums, k, index, holder, result):

        # Define the base case: the index is 0 and we are ready to 
        # append the currently growing list to the resulting list.
        # Return from this level and back track to an upper level
        # because we found a part of the answer.
        if k == 0:
            result.append(holder)
            return

        # Go through all the numbers in 1...n+1 and use recursion to
        # get all the groups of numbers of size k for each number in 
        # nums, but we don't iterate with the values! We iterate with
        # the index of the numbers!
        for i in range(index, len(nums)):
            self.backtracking(nums, k-1, i+1, holder+[nums[i]], result)
