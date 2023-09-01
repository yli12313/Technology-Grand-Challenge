class Solution(object):
    def maxSum(self, nums):
        # Constraints
        # - 2 <= nums.length <= 100
        # - 1 <= nums[i] <= 10^4

        # Topic: Array.
        # This is an array and hash table problem.

        # Approach 1:
        # - Wouldn't you just do:
        # [51,71,17,24,42] -> [6,8,8,6,6]
        # - Then you would need to extract the maximum number that has 
        # frequency of 2?
        # {8:2, 6:3}
        # - This is just not the right approach; it's ok to look at the
        # answers in this case.

        # (HINT): Find the largest and second largest element with maximum
        # digits equal to x where 1<=x<=9.
        
        # - Ah! You have to find the MAXIMUM SUM of a PAIR OF NUMBERS where
        # the MAXIMUM DIGIT in both numbers are EQUAL. Else return -1.
        # - (Full Algorithm): Define a function that will calculate the max
        # digit in any number.
        # - Define 'ans'
        # - Define double for() loops that will loop through the array 'nums'.
        # - Call max digit function on numbers: 'nums[i]' and 'nums[j]'.
        # - If the two numbers have the same max digit, calcuate the sum and
        # update 'ans'.

        # TC: O(N^2)
        # SC: O(1)
        
        n=len(nums)
        # TRICK: You should set the ans to -1.
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

    def findMax(self, n):
        max_digit = 0
        
        while n > 0:
            # REMINDER: 'n%10' will get you the digit that is right-most.
            # REMINDER: 'n/10' will cut the digit that is right-most.

            r=n%10
            max_digit = max(max_digit, r)
            # TRICK: you have to do 'math.floor(n/10)'.
            n=math.floor(n/10)
        
        return max_digit
