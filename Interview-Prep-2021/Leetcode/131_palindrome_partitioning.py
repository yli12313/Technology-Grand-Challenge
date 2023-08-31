class Solution(object):
    def partition(self, s):
        # Constraints:
        # - 1 <= s.length <= 16
        # - s contains only lowercase English letters.

        # Topic: Hash table?
        # Nope. This is a String, Dynamic Programmiing, Backtracking problem.

        # Approach 1:
        # - TRICKY: The brute-force approach is now you solve this problem with
        # tracking.
        # - I want to use Combination Sum II as a reference to see if I can solve
        # this problem.
        # - I couldn't I had to take a look at Neetcode's solution + use ChatGPT.

        # Approach 2 (Neetcode): 
        # - Define and 'res' and 'part' list.
        # - Define a dfs() function with parameter 'i'.
        # - If 'i >= len(s)', append a copy of 'part' to 'res' and return.
        # - Define a for() loop that uses a new variable 'j' that goes from 'i' -> 'len(s)'.
        # - If string 's' from 'i' -> 'j' is a palidrome (create helper function), then
        # - add 's[i,j+1]' to 'part'. 
        # - Call 'dfs(j+1)'.
        # - Call 'part.pop()'.

        # - Outside the inner dfs() function but within the partition() function, do
        # 'dfs(0)' and return the result. 

        # - Define an isPali() function with the signature: 'isPali(self, s, l, r)'.

        # TC: O(N*(2^N)) -> Worst case is 2^N possible palindrome partitions.
        # SC: O(N*(2^N)) -> Worst case is 2^N possible palindrome partitions.

        res,part = [],[]

        def dfs(i):
            n = len(s)
            if i >= n:
                res.append(part[:])
                return
            
            for j in range(i, n):
                if self.isPalid(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        # TRICK: Have to call 'dfs(0)' and 'return res' outside of 'dfs()', but within 
        # 'partition()'.
        dfs(0)
        return res
        
    def isPalid(self, s, l, r):
        while l<r:
            if s[l]!=s[r]:
                return False
            # TRICK: Have to update the pointers right here.
            l,r = l+1,r-1
        
        return True

        # Approach 2 (ChatGPT):
        # - Define a function 'is_palindrome(s)' checking if 's == s[::-1].
        # - Define backtrack function with 'backtrack(start, path):'.
        # - If start is equal to len(s), then append a copy of 'path' to the 'result' and return.
        # - loop using an end variable from 'start+1' -> 'len(s) + 1'.
        # - If 's[start:end]' is a palindrome, then call backtrack again.
        # - Call 'backtrack(end, path + [s[start:end]])'.
        # - Define result outside the function.
        # - Call backtrack with the right parameters.
        # - Return the result.

        # TC: O(N*(N^2)) -> O(N^3) -> Worst case is you make N^2 number of recursive calls.
        # SC: O(2^N) -> Worst case is 2^N possible palindrome partitions. 
