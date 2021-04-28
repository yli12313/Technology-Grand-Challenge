# LINK: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
  def removeDuplicates(self, nums):
    temp = {}

    i = 0
    while i < len(nums):
    	print(i, nums[i])

    	if nums[i] in temp.keys():
    		nums.remove(nums[i])
    	else:
    		temp[nums[i]] = 1
    		i += 1

    return len(nums)

foo = Solution();
print(foo.removeDuplicates([1,1,2]));