# Link: https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        # Define the resulting list
        result = []

        # k is the limit of each list within the larger list.
        limit = k
        
        # Kick off backtracking and recursion
        self.backtracking(range(1, n+1), 0, k, [], result)

        # Return the result
        return result
    
    def backtracking(self, numbers, index, limit, holder, result):

        # Defining the base case: if the limit is 0, we are ready to 
        # append the currently growing list to the resulting list.
        # Return from this level and backtrack to an upper level in 
        # the recursion stack because we found a part of the answer.
        if limit == 0:
            result.append(holder)
            return

        # Go through all the numbers in 1...n+1 (interate by their index, so start 
        # with 0) and use recursion to get all the groups of numbers of size: limit. 
        # But we don't iterate with the values! We iterate with the index of the numbers!
        # Need to track both the numbers and their index (see parameters: numbers, index).
        # The parameter: numbers doesn't change, but the index increases +1 for every 
        # recursive call and the limit -1 for every recursive call.
        for i in range(index, len(numbers)):
            self.backtracking(numbers, i+1, limit-1, holder+[numbers[i]], result)

foo = Solution();
print(foo.combine(4, 2));
