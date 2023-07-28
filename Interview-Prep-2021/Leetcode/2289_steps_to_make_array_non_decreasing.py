class Solution(object):
  def totalSteps(self, nums):
    # Approach 1:
    # - When do you know that an arrac is a non-decreading array?
    # - You know it's a non-decreasing array (a.k.a. increasing array) when
    # you set two pointers (one at the beginning and one at the end) and the 
    # elements that the first pointer points to is less than the elements that
    # the second pointer points to.

    # You need a quick way to check if the array is increasing?
    # TOTALLY WRONG APPROACH! Need Dynamic Programming + Monotonic Stack.

    # Approach 2:
    # - See the code documentation.

    n = len(nums)
    answer = 0

    # dp is used to hold steps.
    dp = [0]*n

    # Stack is used to hold indexes of nums.
    stack = []
    
    # Loop through the nums array.
    for i in range(n):

      # Set step to 1.
      step = 1

      # Update step and dp.
      while stack and nums[stack[-1]] <= nums[i]:
        step = max(step, dp[stack.pop()] + 1)
      
      if stack:
        dp[i] = step

      # Update stack.
      stack.append(i)
      
      # update answer.
      answer = max(answer, dp[i])
    
    # Return the answer.
    return answer



foo = Solution();
print(foo.totalSteps([5,3,4,4,7,3,6,11,8,5,11]));