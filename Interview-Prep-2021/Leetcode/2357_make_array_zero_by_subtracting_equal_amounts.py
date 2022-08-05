# Link: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution(object):
  def minimumOperations(self, nums):
    # Get the length of the nums integer array.
    n = len(nums)

    # Create an artificial array that shows the array when all the
    # subtraction operations are completed. 
    final = [0]*n

    # Create a variable that will count the subtraction operations.
    count = 0

    # Keep looping while there are still subtraction operations.
    while nums != final:
      # Find the minimum value in the array that's greater than 0 using the filter()
      # method: filter(function, sequence)
      minimum = min(filter(lambda x: x > 0, nums))

      # Loop through the values in the array and subtract the minimum from all values > 0.
      for i in range(n):
        if nums[i] > 0:
          nums[i] = nums[i] - minimum

      # Increase the count by +1.
      count += 1

    # Return the count.
    return count
  
foo = Solution();
print(foo.minimumOperations([0]));
