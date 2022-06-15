# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
  def findKthLargest(self, nums, k):
    if nums is None:
      return None
    if k > len(nums):
      return None
        
    nums = sorted(nums)
    
    return nums[len(nums)-k]
