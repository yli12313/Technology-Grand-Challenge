# LINK: https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        # Topic: Array
        # Wrong. This is apparently a hash table, string, and sorting problem.

        # Approach 1:
        # - Add each element to a dictionary and increase the counter if it's a new character. 
        # Do it for string one.
        # - Do the samething for the second string and subtract the counter every time it
        # encounters a new character. 
        # - If the counter is after subtraction is 0, delete the element from the hash table.
        # - return if hash table == 0.

        # NOTE: Your code is too complicated! Need to look for a simple solution instead. 
        # Go to the solutions here!

        # holder = {}

        # for c in s:
        #     if c not in holder.keys():
        #         holder[s] = 1
        #     else:
        #         holder[s] += 1
            
        # for c in t:
        #     if c not in holder.keys():
        #         continue
        #     else:
        #         holder[s] -= 1

        #         if holder[s] == 0:
        #             del holder[s]

        # return len(holder) == 0

        # Approach 2:
        # - First check if the two strings have the same length. If they don't then return False.
        # - Define two dictionaries that will record the frequency of all the characters.
        # - Check if the two dictionaries are the same!

        # NOTE: This is a genius solution! Just brilliant.

        # TC: O(N)
        # SC: O(2*N)

        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            count_s[char_s] = 1 + count_s.get(char_s, 0)
            count_t[char_t] = 1 + count_t.get(char_t, 0)
        
        return count_s == count_t
