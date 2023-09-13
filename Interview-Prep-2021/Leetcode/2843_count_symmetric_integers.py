# LINK: https://leetcode.com/problems/count-symmetric-integers/

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        # Constraints
        # - 1 <= low <= high <= 10^4

        # Topic: Math, Enumeration

        # Approach 1:
        # - We know that we are given '[low,high]', so the range that we are looking over for
        # the symmetric integers is inclusive of low,high.
        # - Define count to hold the answer.
        # - Loop through the given range.
        # - Convert the number into string.
        # - If the string is of odd length, it can't be a symmetric integer.
        # - If it's even, check if the sum of the digits in the first half equals the sum of 
        # the digits in the  second half of the string.
        # - If so, increment count.
        # - Return count.

        # TC: O(N*M)
        #   - N is the number of integers we are iterating over
        #   - M is the number of digits in the longest integer.
        # SC: O(1)

        count = 0

        n = high+1
        for i in range(low,n):
            n_string = str(i)
            m = len(n_string)
            if m%2 != 0:
                continue
            else:
                o = int(m/2)
                if self.get_sum(n_string[:o]) == self.get_sum(n_string[o:]):
                    count += 1

        return count
    
    def get_sum(self, n):
        ans = 0
        for d in n:
            d = int(d)
            ans += d
        
        return ans
