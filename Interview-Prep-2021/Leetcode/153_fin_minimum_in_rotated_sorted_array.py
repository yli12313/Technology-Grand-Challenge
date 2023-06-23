# LINK: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
  def findMin(self, nums):

  	# Set the starting pointers.
    start = 0

    # Set the ending pointer.
    end = len(nums) - 1

    # Example:
    # [4,5,6,7,0,1,2]

    # start = 0; end = 6
    
    # 0 < 6 TRUE
    # mid = 3
    # nums[3] < nums[6] => 7 < 2 FALSE
    # start = 4

    # start = 4; end = 6
    # mid = 5
    # nums[5] < nums[6] => 1 < 2 TRUE
    # end = 5

    # start = 4; end = 5
    # mid = 4
    # nums[4] < nums[5] => 0 < 1 TRUE
    # end = 4

    # start = 4; end = 4
    # mid = 4
    # nums[4] < nums[4] => 0 < 0 FALSE

    # return nums[4] => 0

    while start < end:
      mid = (start + end) // 2

      # Compare the number at the mid with the number at the end.
      if nums[mid] < nums[end]:
      	# Trick: The end gets updated to the mid.
        end = mid
      else:
      	# Trick: The start gets updated to the mid + 1.
      	start = mid + 1

    # Trick: return nums[start].
    return nums[start]

foo = Solution();
print(foo.findMin([4,5,6,7,0,1,2]));