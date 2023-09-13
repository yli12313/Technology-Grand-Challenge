# LINK: https://leetcode.com/problems/count-symmetric-integers/

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        # Constraints
        # - 1 <= low <= high <= 10^4

        # Topic: Math, Enumeration

        # Approach 1:
        # - Define a variable count that will store the answer: the number of symmetric integers found.
        # - Loop through low -> high, inclusive of the endpoint values.
        # - Convert each number in the iteration to a string.
        # - If the string has an odd number of digits, continue.
        # - Else, call a helper function that will calculate the sum of digits on the left and right split 
        # of the string. 
        # - If the sum of the digits on the left and the right split of the string is equal, increase the 
        # variable count (+1).
        # - Return the count. 

        # TC: O(N*M)
        #   - N is the number of integers we are iterating over.
        #   - M is the number of digits in the longest integer.
        # SC: O(1)

        count = 0

        high = high+1
        for i in range(low,high):
            i_string = str(i)
            n = len(i_string)
            
            if n%2 != 0:
                continue
            else:
                # TRICK: When dividing by 2, it's always a good idea to cast to int()!
                m = int(m/2)
                
                if self.get_sum(n_string[:m]) == self.get_sum(n_string[m:]):
                    count += 1

        return count
    
    def get_sum(self, n):
        ans = 0
        for d in n:
            d = int(d)
            ans += d
        
        return ans
