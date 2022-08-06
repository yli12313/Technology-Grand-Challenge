# Link: https://leetcode.com/problems/longest-happy-string/

# Import the libraries that are needed.
# Note: When you need a heap, always use: from heapq import *
# to make the notation a little easier to use.
from heapq import *

class Solution(object):
  def longestDiverseString(self, a, b, c):
    # Define the resulting happy string.
    result = ""

    # Define a list to use as the max-heap.
    max_heap = []

    # Python by default comes with a min-heap. But if you negate
    # the values, it becomes a max-heap.

    # The heappush() syntax is as follows with the heap
    # often being of list type: heappush(heap, value)
    for count, value in [(-a, "a"), (-b, "b"), (-c, "c")]:
      if count:
        heappush(max_heap, (count, value))

    # Keep going while the max-heap is not empty.
    while max_heap:

      # Pop the count and the largest value from the max-heap. 
      # The syntax for the popping values from the heap is:
      # heappop(heap)
      cur, cur_val = heappop(max_heap)
      
      # If there is no more count for this particular value, then
      # continue onto the next one.
      if cur == 0:
        continue 

      # Check that the current happy string is at least of size 2
      # and that the popped character is not equal to the two previous
      # characters in the happy strong.

      # To check the back of a string or list, use the NEGATIVE indexing notation!
      if len(result) > 1 and result[-1] == result[-2] == cur_val:
        
        # The heap should only have non-zero values. If the heap is empty,
        # then stop all operations. This stops the triple case: 'ccc'. Let's say
        # you have 'cc' and you encounter another 'c'. If there's no other values
        # in the max-heap, then the only thing you can make is 'ccc', which is NOT
        # a happy string. Therefore you break and return the string as is without
        # any further modifications!
        if not max_heap:
          break

        # Get the second most popular value.
        cur2, cur_val2 = heappop(max_heap)
        
        # Increase the count of the second most popular value; since it's negative,
        # it's really subtracting the count by 1. Add the value to the result. Push the 
        # count and the value back onto the stack.
        if cur2 < 0:
          cur2 += 1
          result += cur_val2
          heappush(max_heap, (cur2, cur_val2))

        # Increase the count (which is subtracting the count by 1 when the number is
        # negative. Add the largest value from the max-heap to the result.
      elif cur < 0:
          cur += 1
          result += cur_val
      
      # Push the updated count and unchanged value to the max-heap.
      heappush(max_heap, (cur, cur_val))

    # Return the result.
    return result

foo = Solution();
print(foo.longestDiverseString(0, 0, 7));
