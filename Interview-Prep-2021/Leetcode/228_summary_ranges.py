# LINK: https://leetcode.com/problems/summary-ranges/

class Solution(object):
  def summaryRanges(self, nums):
    # Topic: Arrays.

    # TC: O(N)
    # SC: O(N)

    # Approach 1:
    # Use the two pointers method to implement the solution.

    # Tricks:
    # 0) If it's an empty nums, return an empty list.
    # 'if not nums:
    #    return []'

    # 1) If you need to compare elements to the one before, start looping at index 1: 
    # 'for i in range(1, len(nums))'.

    # 2) Updating the running pointer: 
    # 'if nums[i] == nums[i-1] + 1:
    #    end = nums[i]'

    # 3) Checking if you need to add '7' or '0->2'.
    # If 'start == end' append '7'.
    # Else append '0->2'.

    if not nums:
      return []

    ranges = []
    start = nums[0]
    end = nums[0]

    for i in range(1, len(nums)):
      if nums[i] == nums[i-1]+1:
        end = nums[i]
      else:
        if start == end:
          ranges.append(str(end))
        else:
          ranges.append(str(start) + "->" + str(end))
        start = end = nums[i]

    if start == end:
      ranges.append(str(end))
    else:
      ranges.append(str(start) + "->" + str(end))

    return ranges
    
foo = Solution();
print(foo.summaryRanges([0,1,2,4,5,7]));
