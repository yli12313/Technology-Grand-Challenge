# LINK: https://leetcode.com/problems/peak-index-in-a-mountain-array/

# NOTE: This solution works. I'm going to write out two test cases:

#######

# Test Case #1: [0,1,2,3,4,3,1,0]

# left=0; right=7; mid=3
# arr[3]>arr[2] and arr[3]>arr[4] => 3>2 and 3>4 => [X]

# arr[3]<arr[4] => 3<4 => [O]

# left=3+1 => left=4

# left=4; right=7

#######

# Test Case #2: [0,1,4,3,2,1,0]

#left=0; right=6; mid=3

# arr[3]>arr[2] and arr[3]>arr[4] => 3>4 and 3>2 => [X]

# arr[3]<arr[4] => 3<2 => [X]

# arr[3]<arr[2] => 3<4 => [O]

# right=3-1 => right=2

# left=0; right=2

#######

class Solution(object):
  def peakIndexInMountainArray(self, arr):
    left=0
    right=len(arr)-1

    while left<=right:
      mid=(left+right)//2

      if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
        return mid
      elif arr[mid]<arr[mid+1]:
        left=mid+1
      elif arr[mid]<arr[mid-1]:
        right=mid-1

foo = Solution();
print(foo.peakIndexInMountainArray([3,9,8,6,4]));

# NOTE2: You solved this problem using Python built-in functions, but we have to 
# try to solve this problem with binary search. No shortcuts!

# class Solution(object):
#   def peakIndexInMountainArray(self, arr):
#     if len(arr)<3:
#       return -1
            
#     mountain_top=max(arr)
#     return arr.index(mountain_top)