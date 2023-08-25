# LINK: https://leetcode.com/problems/prime-in-diagonal/

class Solution(object):
    def diagonalPrime(self, nums):
        # Constraints:
        # - 1 <= nums.length <= 300
        # - nums.length == nums_i.length
        # - 1 <= nums[i][j] <= 4*10^6

        # Topic: Didn't really take a guess at what the topic was.
        # Ended up looking at the answer and this is an array, math, matric, number theory 
        # problem.

        # Approach 1 (Brute-Force Approach):

        # NOTE: The only trick was that I calculated the checkPrime() function wrong! Other than
        # that, I got most of the logic correct!

        n = len(nums)

        max_diag = 0

        for i in range(n):
            if self.checkPrime(nums[i][i]):
                max_diag = max(max_diag, nums[i][i])
            
            # Missed the TRICK right here! Diagonals can go from 'top-left -> bottom right', 
            # as well as 'top-right -> bottom-left'.
            if self.checkPrime(nums[i][n-i-1]):
                max_diag = max(max_diag, nums[i][n-i-1])
        
        return max_diag
    
    def checkPrime(self, x):
        if x <= 1:
            return False
            
        # The TRICK is that when you check if a number is prime or not, you only need to check
        # the numbers: '2 <= i <= sqrt(x)'. For any i in this range such that 'x % i == 0', then
        # you know that the number is NOT prime! Moreover, you have to caste 'sqrt(x)+1' as an 
        # 'int'.
        for i in range(2, int(sqrt(x)+1)):
            if x%i == 0:
                return False
            
        return True