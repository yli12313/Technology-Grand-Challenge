# LINK: https://leetcode.com/problems/product-of-array-except-self/

from functools import reduce
# from operator import mul

class Solution(object):
    def productExceptSelf(self, nums):
        answer = []

        if len(nums) < 2:
        	return nums

        for i in range(0, len(nums)):

        	# Delete value
        	popped = nums.pop(i)

        	# Get product
        	prod = reduce(mul, nums)

        	# Insert to new list
        	answer.append(prod)

        	# re-insert value
        	nums.insert(i, popped)

        return answer;

foo = Solution();
print(foo.productExceptSelf([1,2,3,4]));