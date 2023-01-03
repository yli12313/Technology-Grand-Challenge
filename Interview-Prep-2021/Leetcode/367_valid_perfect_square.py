# LINK: https://leetcode.com/problems/valid-perfect-square/

# NOTE: I think I finally solved a binary search problem myself without looking
# at the answers! You have to be careful with the if-statement logic and updating
# the left and right boundaries with a binary search problem.

# One pattern that I did notice is that:
# - If it's '>' in the condition, then you update the right boundary.
# - If it's '<' in the condition, then you update the left boundary.

# The right boundary you always shrink [i.e. 'mid-1'].
# The left boundary you always increase [i.e. 'mid+1'].

class Solution(object):
  def isPerfectSquare(self, num):
    left=1
    right=num

    while left<=right:
      mid=(left+right)//2

      perfect_square=mid*mid
      if perfect_square==num:
        return True
      elif perfect_square > num:
        right=mid-1
      elif perfect_square < num:
        left=mid+1

    return False

foo = Solution();
print(foo.isPerfectSquare(16));