# LINK: https://leetcode.com/problems/count-symmetric-integers/

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        # Constraints
        # - 1 <= low <= high <= 10^4

        # Topic: Math, Enumeration

        # Approach 1:
        # - We know that we are given '[low,high]', so the range that we are looking over for
        # the symmetric integers is inclusive of low,high.
        # - Define list to hold the answers.
        # - Loop through the give range.
        # - Convert the number into string.
        # - If the string is of odd length, it can't be a symmetric integer.
        # - If it's even, check if the first half's sum equals the second half's sum of the 
        # string.
        # - If so, add the digit to the answer list.
        # - Return the length of the answer.

        # TC: O(N)
        # SC: ?

        ans = []

        n = high+1
        for i in range(low,n):
            n_string = str(i)
            m = len(n_string)
            if m%2 != 0:
                continue
            else:
                o = int(m/2)
                if self.get_sum(n_string[:o]) == self.get_sum(n_string[o:]):
                    ans.append(i)

        return len(ans)
    
    def get_sum(self, n):
        ans = 0
        for d in n:
            d = int(d)
            ans += d
        
        return ans
