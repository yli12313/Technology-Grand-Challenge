# LINK: https://leetcode.com/problems/faulty-keyboard/

class Solution(object):
    def finalString(self, s):
        # Constraints
        # - 1 <= s.length <= 100
        # - s consists of lowercase English letters.
        # - s[0] != 'i'

        # Topic: Array.
        # This is a String, Simulation problem.

        # Approach 1:
        # - Loop through the array.
        # - If you encounter i where the index of i is greater than 1, then you reverse the new string.
        # - Else add the character to the new string. 
        # - Return the new string.

        # TC: O(N)
        # SC: O(N)

        answer = ""

        for j in range(len(s)):
            c = s[j]

            if c != 'i':
                answer += c
            elif c == 'i':
                # TRICK: To reverse a string in python, use '[::-1].
                answer = answer[::-1]
        
        return answer
