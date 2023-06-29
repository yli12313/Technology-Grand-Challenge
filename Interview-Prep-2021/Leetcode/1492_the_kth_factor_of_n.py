# LINK: https://leetcode.com/problems/the-kth-factor-of-n/

class Solution(object):
  def kthFactor(self, n, k):
    # Given an integer n=12, how do ou get a list of it's factors:
    # [1,2,3,4,6,12]

    # Brute-Force Approach:
    # 1) Loop through all the integers from 1-to-n. Use the variable i for iteration.
    # 2) If the number i such that n % i == 0, then we found a factor. 
    # 3) Subtract the number k by 1.
    # 4) If k == 0, return the number i.
    # 5) Return -1 by default.

    # TC: O(N)
    # SC: O(1)

    counter = k

    for i in range(1, n+1):
      if n%i == 0:
        counter -= 1

        if counter == 0:
          return i

    return -1

foo = Solution();
print(foo.kthFactor(12,3));