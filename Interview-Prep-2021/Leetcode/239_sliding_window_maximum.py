# Link: https://leetcode.com/problems/sliding-window-maximum/

class Solution(object):
    def maxSlidingWindow(self, nums, k):
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
