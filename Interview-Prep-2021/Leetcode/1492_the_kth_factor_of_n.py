# LINK: https://leetcode.com/problems/the-kth-factor-of-n/

from math import *

class Solution(object):
  def kthFactor(self, n, k):
    # Solution 1:

    # Smart approach (Kacy):
    # 1) Loop just before ceil of square root.
    # 2) Loop down from floor of square while dividing to get complement, decrement k.
    # 3) Whenever k == 0, return the factor.

    # This is an absolutely genius solution!

    # TC: O(sqrt(N))
    # SC: O(1)

    # Set the counter
    counter = k

    # Grab the square root of n's floor and ceiling
    sqrt_root_floor = int(floor(sqrt(n)))
    sqrt_root_ceil = int(ceil(sqrt(n)))

    # Loop through to the square root ceiling, but not including it. 
    # If you've found the the kth factor, then return it.
    for i in range(1, sqrt_root_ceil):
      if (n%i == 0):
        counter -= 1

        if counter == 0:
          return i 
    
    # Loop through the complement of the factors that you just went through 
    # above. If you've found the kth factor, then return it.
    for i in range(sqrt_root_floor, 0, -1):
      if (n%i == 0):
        counter -= 1

        if counter == 0:
          return n/i

    # Return the default answer.
    return -1

    #######
    #######
    #######

    # Solution 2:
    # Given an integer n=12, how do you get a list of it's factors:
    # [1,2,3,4,6,12]

    # Brute-Force Approach:
    # 1) Loop through all the integers from 1-to-n. Use the variable i for iteration.
    # 2) If the number i such that n % i == 0, then we found a factor. 
    # 3) Subtract the number k by 1.
    # 4) If k == 0, return the number i.
    # 5) Return -1 by default.

    # TC: O(N)
    # SC: O(1)

    '''
    counter = k

    for i in range(1, n+1):
      if n%i == 0:
        counter -= 1

        if counter == 0:
          return i

    return -1
    '''

foo = Solution();
print(foo.kthFactor(12,3));
