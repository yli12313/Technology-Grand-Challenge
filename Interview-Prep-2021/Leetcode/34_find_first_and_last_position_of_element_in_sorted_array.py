# LINK: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# NOTE: This problem I tried the best I could and could not get it. It's smart at this point to look at the answers for
# a solution. I'm too tired right now to find the answers. I'm going to try again when I'm more away.

# This was a crazy problem that I didn't think that I was going to be solve, but I was able to solve it!
# It involved having two binary searches, one to find the left cutoff point and one to find the right cutoff 
# point. I had the algorithm right and the intuition right, but just didn't recognize that you needed two binary
# searches and not just one. This kind of intuition you only get through practice and I'm glad I pushed through to
# solve this problem!

class Solution(object):
  def searchRange(self, nums, target):
    answer=[-1,-1]

    left=0
    right=len(nums)-1
    while left<=right:
      mid=(left+right)//2

      if nums[mid]==target:
        if mid-1>=0 and nums[mid-1]==target:
          answer[0]=mid-1
          right=mid-1
        else:
          answer[0]=mid
          right=mid-1
      elif nums[mid]<target:
        left=mid+1
      else:
        right=mid-1

    left=0
    right=len(nums)-1
    while left<=right:
      mid=(left+right)//2

      if nums[mid]==target:
        if mid+1<len(nums) and nums[mid+1]==target:
          answer[1]=mid+1
          left=mid+1
        else:
          answer[1]=mid
          left=mid+1
      elif nums[mid]<target:
        left=mid+1
      else:
        right=mid-1

    return answer

foo = Solution();
print(foo.searchRange([], 0));

# NOTE: This is the non-binary search algorithm from before. 

# class Solution(object):
#   def searchRange(self, nums, target):
#     for i in range(0, len(nums)):
#       if nums[i] == target and i==0:
#         return [0, 0]
            
#       if nums[i] == target:
#         return [i, i+1]
            
#     return [-1, -1]