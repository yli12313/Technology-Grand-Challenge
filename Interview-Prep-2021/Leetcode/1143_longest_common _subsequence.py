# Link: https://leetcode.com/problems/longest-common-subsequence/

# Note: This solution works with only Python3.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Trick to speed up massive amounts of recursive calls with memoization.
        @lru_cache(None)
        
        def auxiliary(text1, text2):
            # Return 0 if both text 1 and 2 are empty.
            if not text1 or not text2:
                return 0
            
            # If the first character of each string is equal to each other, we found a match (+1) and recurse on each string starting from the
            # second character.
            if text1[0] == text2[0]:
                return 1+auxiliary(text1[1:], text2[1:])
            # Recurse on each string and see which recursion call gives the max substring.
            else:
                return max(auxiliary(text1[1:], text2), auxiliary(text1, text2[1:]))
        
        # Return the answer.
        return auxiliary(text1, text2)
