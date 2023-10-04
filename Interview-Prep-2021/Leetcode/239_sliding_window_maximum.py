# Link: https://leetcode.com/problems/sliding-window-maximum/

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # Constraints
        # - 1 <= nums.length <= 10^5
        # - -10^4 <= nums[i] <= 10^4
        # - 1 <= k <= nums.length

        # Topic: Sliding Window
        # This is an Array, Queue, Sliding Window, Heap (Priority Queue), or 
        # Monotonic Queue problem.

        # Approach 1:
        # - Set 'n' to be the length of 'nums'.
        # - Set result as a list populated by 0s that is of length '(n-k+1)'.
        # - Define a deque as a list that will hold indices. However, the 
        # indices link to values in the nums array. And moreover, the deque
        # encodes a monotonically decreasing queue. You want to keep the maximum
        # value's index in the current sliding window as the first element in the
        # deque.
        # - Define a 'limit' variable and set it to 'k-1'. We do this because
        # lists in Python are 0-based.
        
        # - First for() loop:
        # - Loop using variable i from 0..limit.
        # - Get the value of 'nums[i]'.
        # - while 'deque' and 'nums[deque[-1]]' is less then the value calculated
        # in the previous step, pop from the deque.
        # - Append i to the deque.

        # - Second for() loop:
        # - Loop using variable i from limit..n.
        # - Implement the same code as above.
        # - Calculate 'next', which is the next index in result that you have to 
        # populate with an answer (i.e. our current sliding window as a max value
        # that we found). The condition is 'next = i-limit'.
        #   - 'next' is also the edge of the sliding window on the left side.
        # - For all the indices that are less than next, do a while() loop to remove
        # them in the front using 'deque.pop(0).
        # - Populate 'result[next]' with 'nums[deque[0]]'.

        # TC: O(N)
        # SC: O(K), where K is the size of the sliding window.
        
        n = len(nums)
        result = [0] * (n-k+1)

        deque = []

        limit = k-1
        for i in range (0, limit):
            val = nums[i]
            while not len(deque) == 0 and nums[deque[-1]] < val:
                deque.pop()
            deque.append(i)

        for i in range(limit, n):
            val = nums[i]
            while deque and nums[deque[-1]] < val:
                deque.pop()
            deque.append(i)

            next = i-limit
            while deque[0] < next:
                deque.pop(0)

            result[next] = nums[deque[0]]

        return result
            
foo = Solution();
print(foo.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3));
