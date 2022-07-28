# Link: https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        # When there is only one house, return the money from the house.
        if len(nums) == 1:
          return nums[0]

        # Define a 1-d array that will serve as the dp array.
        dp = [0]*len(nums) 
                
        # Define the first element in the dp array as the money in the first house.
        dp[0] = nums[0]

        # Define the second element in the dp array as the money in either the first or second house.
        dp[1] = max(nums[0], nums[1])

        # Starting from the third house, use dynamic programming to solve the answer. 
        for i in range(2, len(nums)):  
          
          # There's two cases:
          # 1) Get rob the current house, which means you've robbed the house that was two houses down.
          # 2) You don't rob the current house, which means you've robbed the previous house.   
          dp[i] = max(nums[i] + dp[i-2], dp[i-1])


        # Return the money that was stolen from all the houses on the street.
        return dp[len(dp)-1]

foo = Solution();
print(foo.rob([2,7,9,3,1]));
