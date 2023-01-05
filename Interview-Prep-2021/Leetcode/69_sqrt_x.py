# LINK: https://leetcode.com/problems/sqrtx/
# LINK2 (Very Good Explanation): https://leetcode.com/problems/sqrtx/solutions/2981409/binary-search-finding-first-true-statement-in-false-true-list-python/?envType=study-plan&id=binary-search-i

# NOTE: This was an interesting problem. Essentially, you are finding the cutoff point (see example):

# Example: [F,F,F,T,T,T,T,T]

# Obviously we want to return the square root directly if the target number 'X' is a perfect square right away.
# where the element changes from '[elem]*[elem] < [X]' to '[elem]*[elem] > [X]'. We want to return the
# cutoff point where this happens, the last element that when you take the square of it, it's still less than
# the target 'X'.

class Solution(object):
  def mySqrt(self, x):
    left=1
    right=x
    sqrt_root=-1

    if x==0: return 0

    while left<=right:
      mid=(left+right)//2

      if mid*mid==x:
      	return mid
      elif mid*mid<x:
      	sqrt_root=mid
      	left=mid+1
      else:
      	right=mid-1

    return sqrt_root

foo = Solution();
print(foo.mySqrt(4));
