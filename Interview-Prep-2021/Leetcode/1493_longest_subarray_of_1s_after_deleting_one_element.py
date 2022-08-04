# Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution(object):
  def longestSubarray(self, nums):
    # Define the previous and the current span (i.e. the number of 1's encountered before and after 0).
    previous_span = 0
    current_span = 0

    # Define the length of the nums array that is the argument.
    n = len(nums)

    # Store the best result answer.
    best_result = 0

    # Start at index 0.
    start = 0

    # Loop through the nums array from start and end at n.
    while start < n:  

      # If you encounter a 0: you have to 1) calculate the best result, 2) set the previous_span as the current_span,
      # and 3) set the current_span as 0.
      if nums[start] == 0:
        best_result = max(best_result, previous_span + current_span)
        previous_span = current_span
        current_span = 0

      # If you encounter a 1: you have 1) increase the current_span by +1 and 2) calculate the best result. You calculate
      # the result AFTER you increase current_span +1 just in case 1 is the last value as in: [1, 1, 0, 1].
      elif nums[start] == 1:
        current_span += 1
        best_result = max(best_result, previous_span + current_span)
      
      # Increase the index to loop to the next element.
      start += 1

    # Account for the case that the array is all 1's. If the array is all 1's, then return
    # the best result - 1.
    if best_result == len(nums):
      return best_result - 1

    # Return the best result answer. 
    return best_result 
        
foo = Solution();
print(foo.longestSubarray([1,1,0,1]));
