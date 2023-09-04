class Solution(object):
    def findMax(self, n):
        # TRICK: Define 'ans' right here.
        ans = -1
        
        while n > 0:
            # REMINDER: 'n%10' will get you the digit that is right-most.
            # REMINDER: 'n/10' will cut the digit that is right-most.
            r=n%10
            # TRICK: Make sure you are doing 'max(ans,r)' right here and NOT
            # 'max(ans,n)'.
            ans = max(ans,r)
            # TRICK: You have to do 'math.floor(n/10)'.
            n=math.floor(n/10)
        
        return ans
    
    def maxSum(self, nums):
        # Constraints:
        # - 2 <= nums.length <= 100
        # - 1 <= nums[i] <= 10^4

        # Topic: Array.
        # This is an Array and Hash Table problem.

        # Approach 1:
        # - Define a findMax() method in the class 'Solution' that will find 
        # the maximum digit in any number.
        # - Define an answer variable.
        # - Do double for() loops that will iterate through the numbers n in nums.
        # - Call our findMax() method on nums[i] and nums[j].
        # - If the two numbers have equal max digits, then calculate the sum of
        # the two numbers.
        # - Update the answer as the max of the previous answer and the new sum.
        # - Return the answer.

        # TC: O(N^2)
        # SC: O(1)
        
        # TRICK: You should define 'n' set the 'ans' to -1.
        n=len(nums)
        ans = -1

        for i in range(n):
            for j in range(i+1,n):
                n1=self.findMax(nums[i])
                n2=self.findMax(nums[j])

                if n1==n2:
                    # TRICK: You have to do: 'sum=nums[i]+nums[j]'.
                    sum=nums[i]+nums[j]
                    ans=max(ans, sum)
        
        return -1 if ans == -1 else ans
