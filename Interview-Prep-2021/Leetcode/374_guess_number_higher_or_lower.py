# LINK: https://leetcode.com/problems/guess-number-higher-or-lower/

# NOTE: I had the right idea overall, but once again I tried to implement recursion when I 
# should NOT have even thought about recursion! Don't use recursion when it comes to binary
# search; use two pointers where one pointer is the first element and the other pointer is
# the last element. The first instinct with binary search should NOT BE recursion.

# The logic is the follow: You start off by guessing the midpoint value.
# - If the midpoint value is GREATER THAN the picked number (i.e. NEGATIVE (-) guess value), then 'right=mid-1'.
# - If the midpoint value is LESS THAN the picked number (i.e. POSITIVE (+) guess value), then 'left=mid+1'.

# I got confused with what the negative and positive numbers from the guess() function mean. That's
# what caused me a lot of confusion until I watched like a YouTube video. But it's ok, I'm learning you know?

class Solution(object):
  def guessNumber(self, n):
    left = 1
    right = n

    while left <= right:
        mid = (right+left) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result < 0:
            right=mid-1
        elif result > 0:
            left=mid+1

    return -1
        