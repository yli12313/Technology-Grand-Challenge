# LINK: https://leetcode.com/problems/faulty-keyboard/

class Solution(object):
    def finalString(self, s):
        # Constraints
        # - 1 <= s.length <= 100
        # - s consists of lowercase English letters.
        # - s[0] != 'i'

        # Topic: Array.
        # This is a String, Simulation problem.

         Approach 1:
        # - Loop through the characters of the string s.
        # - For each character c in s, if it's not equal to the character 'i', then add it to a return
        # string.
        # - If it is the character 'i', then reverse the return string, but don't add 'i' to the return
        # string.
        # - Return the answer.

        # TC: O(N)
        # SC: O(N)

        # TRICK: 'answer' has to be a string and not a list! Define this return string first.
        answer = ""

        for c in s:
            if c != 'i':
                answer += c
            elif c == 'i':
                # TRICK: To reverse a string in python, use '[::-1].
                answer = answer[::-1]
        
        return answer
