# LINK: https://leetcode.com/problems/sum-of-square-numbers/

from math import *

class Solution(object):
  def isqrt(self, n):
    x = n
    y = (x + 1) // 2
    while y < x:
      x = y
      y = (x + n // x) // 2
    
    return x

  def judgeSquareSum(self, c):
    # Approach 1:
    # - Given c, can you find a^2 + b^2 = c?
    # - Obviously a, b both have to be less than c.

    # Was not going to get it by myself. Might as well look at the answer.

    # Approach 2:
    # - Set this up as a two pointers problem: where the start is 0 and the end is sqrt(c).
    # - Calculate sumOfSquare = a^2+b^2.
    # - If sumOfSquare is equal to c, return True.
    # - If sumOfSquare < c, then the first pointer is increased.
    # - If sumOfSquare > c, then the second pointer is decreased.
    # - Return False.

    i = 0
    j = self.isqrt(c)

    while (i <= j):
      sumOfSquare = pow(i,2) + pow(j,2)
      print(sumOfSquare)
      if sumOfSquare == c:
        return True
      elif sumOfSquare < c:
        i += 1
      else:
        j -= 1

    return False 

foo = Solution();
print(foo.judgeSquareSum(5));