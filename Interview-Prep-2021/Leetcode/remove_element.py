# LINK: https://leetcode.com/problems/remove-element/

class Solution(object):
  def removeElement(self, nums, val):
    if len(nums) == 1 and val == nums[0]:
    	del nums[0]
    	return 1
    elif len(nums) <= 1:
    	return len(nums)

    i=0
    while i<len(nums):
    	if nums[i]==val:
    		nums.remove(nums[i])
    	else:
    		i+=1

    return len(nums)

foo = Solution();
print(foo.removeElement([0,1,2,2,3,0,4,2], 2));