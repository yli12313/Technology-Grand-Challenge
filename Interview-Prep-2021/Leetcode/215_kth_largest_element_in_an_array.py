# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Solution 1
class Solution(object):
  def findKthLargest(self, nums, k):
    if nums is None:
      return None
    if k > len(nums):
      return None
        
    nums = sorted(nums)
    
    return nums[len(nums)-k]
  
  # Solution 2
  def findKthLargest_Solution2(self, nums, k):
    number = len(nums) - k
    
    # Heapify gives you a min heap!
    heapify(nums)

    for i in range(number):
      heappop(nums)
        
    return heappop(nums)
