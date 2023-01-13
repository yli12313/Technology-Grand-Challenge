# LINK: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

# NOTE: I don't know why I struggled with this problem so much. I tried many different wrong approaches.
# I didn'treally understand the problem or what it was asking. I didn't realize that the problem wants you
# to think in terms of 'i', which ranges between 0-1000. That's the answer space! From the answer space, you
# want to find the number of elements in 'nums' greater than or equal to i, for example 'elem>=i' and keep a
# count. Because the answer is unique, you just need to find the i that's equal to the count, for example
# 'count==i'.

# I guess one big key takeaway is to always look at the constraints before starting a problem! The constraints
# are very important. Had I looked at the contraints for this problem first, I would have not been as confused
# with the nature of the problem.

# An FYI: the sorted() function always sorts in ascending order (i.e. the values increase and become larger).

class Solution(object):
  def specialArray(self, nums):
    for i in range(0, 1001):
      count=0

      for elem in nums:
        if elem>=i:
          count+=1
      
      if count==i:
        return i

    return -1

foo = Solution();
print(foo.specialArray([3,9,7,8,3,8,6,6]));
