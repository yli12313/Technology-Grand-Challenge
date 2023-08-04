# LINK: https://leetcode.com/problems/two-sum/

# Approach 1: I'm reviewing two sums because I forgot about it. I'm using ChatGPT for review.

# NOTE: The key point to note is that if there's two numbers that add up to the target, then
# 'target - number1' should yield a 'number2' that's also in the nums array. Therefore, we calculate 
# the difference and see if the result is in a dictionary that records the items and indexes in nums that 
# we created. If so, return the index of the value number2 such that 'number2' is equivalent to 
# 'target - number1'. The key point is that 'number2' is itself a value of the nums array!

class Solution(object):
  def twoSum(self, nums, target):

    # Create a dictionary to hold all the values of nums encountered.
    num_dict = {}

    # Loop through the nums array by index and by value.
    for i, num in enumerate(nums):
      # Calculate the difference between the target and the current item of nums.
      diff = target - num

      # If the difference is in nums_dict, then return the index of the diff value in nums + the current index.
      if diff in num_dict:
        return [num_dict[diff], i]

      # Record the current nums value and index in the dum_dict dictionary.
      num_dict[num] = i
    
    # Return an empty list if you could not find an answer to the two sums problem. 
    return []

foo = Solution();
print(foo.twoSum([3,2,4], 6));