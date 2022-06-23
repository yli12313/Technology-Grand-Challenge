# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import *

class Solution(object):
  
  ## Solution 1 ##
  def findKthLargest(self, nums, k):
    # Conditions: if the array is empty or if the the k-value is greater than then array
    # length, return none.
    if nums is None:
      return None
    if k > len(nums):
      return None
    
    # Sort the array in ascending order i.e. [1, 2, 3].
    nums = sorted(nums)
    
    # If the array is sorted in ascending order, to get the kth-largest, you have to subtract from then length of the array.
    # 1st largest: 3-1 = 2. The 2nd in the array above is the value: 3.
    return nums[len(nums)-k]
  
  ## Solution 2 ##
  def findKthLargest_Solution2(self, nums, k):
    
    # Get the index of the kth-largest value.
    number = len(nums) - k
    
    # Heapify gives you a min heap!
    heapify(nums)
    
    # Pop k-times from the heap from the beginning of the heap if it's a min-heap.
    for i in range(number):
      heappop(nums)
        
    # Return the kth-largest value.
    return heappop(nums)
