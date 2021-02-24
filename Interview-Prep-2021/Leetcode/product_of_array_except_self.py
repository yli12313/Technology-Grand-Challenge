# LINK: https://leetcode.com/problems/product-of-array-except-self/

## Make sure to use double space and not tab! ##

from functools import reduce
from operator import mul

class Solution(object):
  def productExceptSelf(self, nums):

    # Define left, right lists
    left=[0]*len(nums)
    left[0]=1
    right = [0]*len(nums)
    right[len(nums)-1]=1

    total=0

    # Compute left array
    # Compute right array
    for i in range(1, len(nums)):
      left[i]=left[i-1]*nums[i-1]
      right[len(nums)-i-1]=right[len(nums)-i]*nums[len(nums)-i]

    # Compute final answer
    for i in range(len(left)):
      left[i]=left[i]*right[i]

    return left

foo = Solution();
print(foo.productExceptSelf([1,2,3,4]));