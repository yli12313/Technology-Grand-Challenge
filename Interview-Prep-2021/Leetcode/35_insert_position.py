# LINK: https://leetcode.com/problems/search-insert-position/

# NOTE: I had the binary search right, but just didn't have the last part
# the return index correct. I should have known that the insertion point of
# the 'target' was going to be 'left'. Let me trace the code with a simple example:

# Example we are tracing has: nums=[1,3]; target=2

# Tracing the logic, we have the following:

# left=0; right=1
# mid=0

# left=1; right=1
# mid=1

# left=1; right=0
# mid=X

# return left => 1

# PUNCHLINE: What I should have realized was that the while() loop stops when
# 'left' > 'right', and that 'left' IS the value that you return as the insertion
# point for 'target'. You don't need to do anything complicated. I was trying to
# do some complicated if-statement logic. Whenever you find yourself trying complicated
# if-statement logic, it's almost always wrong. Better to look at the answers because
# the if-statement logic will work on some test cases, and not on others. Better to 
# solve the problem with better logic and NOT more if-statements! This is something
# that I need to get better at with regard to solving coding problems: simplify my
# coding logic.

class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1

        while left<=right:
       	    import pdb; pdb.set_trace()
            mid=(left+right) // 2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        
        return left

foo = Solution();
print(foo.searchInsert([1,3], 2));

