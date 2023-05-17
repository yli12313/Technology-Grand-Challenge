class Solution(object):
  def search(self, nums, target):
    # Approach 1:
    # Do a binary search
    # - If the mid > nums[len(nums)-1], then the first pointer is mid + 1
    # - Else, the second pointer mid - 1

    # i=0
    # j=len(nums)-1

    # while i<=j:
    #   mid=(i+j)//2

    #   if mid > nums[len(nums)-1]:
    #     i=mid+1
    #   else:
    #     j=mid-1
  
    # pivot=i
    # print(pivot)
    
    # m=0
    # n=len(nums)-1
    # while m<=n:
    #   mid=(m+n)//2
      
      
    #   # print(nums[mid])
    #   if nums[mid] == target:
    #     return mid

    #   if pivot != 0:
    #     mid = (mid+pivot)%len(nums)


    #   if mid < target:
    #     m=mid+1
    #   else:
    #     n=mid-1

    # return -1

    # WRONG APPROACH: No use in wasting time when you have the WRONG APPROACH!

    # Approach 2:
    # Do a binary search like normal, calculating the midpoint.
    # If the midpoint equals the target, return the midpoint.
    # Check if the value of the first pointer is less than or equal to the value of the midpoint. KEY POINT!!
    # (Inside): Check if the target is less than or equal to the value of the midpoint and greater than or equal to the value of the first pointer.
    # If so, then the end is: midpoint - 1.
    # Else, the start is: the midpoint + 1.
    # Do the opposite for the right side of the array.
    # Return -1.

    i=0
    j=len(nums)-1

    while i<=j:
      mid=(i+j)//2

      if nums[mid] == target:
        return mid

      if nums[i] <= nums[mid]:
        if nums[i] <= target and target <= nums[mid]:
          j=mid-1
        else:
          i=mid+1
      else:
        if nums[mid] <= target and target <= nums[j]:
          i=mid+1
        else:
          j=mid-1

    return -1

foo = Solution();
print(foo.search([4,5,6,7,0,1,2], target = 0));


