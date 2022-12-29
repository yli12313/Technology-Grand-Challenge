# LINK: https://leetcode.com/problems/binary-search/

# NOTE: I'm about to finish the mini-series of SQL problems, and they are fantastic!
# I was contemplating whether I should continue with the SQL lessons, but decided that 
# I should go back to Python and also keep those Python skills sharp. I've decided to
# do the mini-series on binary search algorithms, because I've never been very strong w.r.t.
# to binary search. I'm going to take it show by starting with 'Binary Search I'.

# The notes that I should remember for the problem below is the following:
# 1) The '//' operator means Floor Division. For example, if you do (left + right) // 2 where left 
#    and right are the first and last indexes of a 0-indexed array:
#        - Then if the array has an EVEN number of elements, it will return the index of the array 
#          element that is the LAST element in the first half of elements.
#        - Then if the array has an ODD number of elements, it will return the index of the array 
#          element that is the median element.
# 2) This problem is NOT a recursion problem! It is a two-pointer problem where the first pointer
#    is the index of the first array element and the second pointer is the idex of the last array 
#    element.
# 3) The logic that makes the code work is the two following pieces of code:
#        - 'left <= right'.
#        - '(left + right) // 2'.

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            search_point = (left + right) // 2

            if (target == nums[search_point]):
                return search_point
            
            if (target > nums[search_point]):
                left = search_point+1
            elif (target < nums[search_point]):
                right = search_point-1
                
        return -1