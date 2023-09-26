# LINK: https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        # Constraints
        # - m == s.length
        # - n == t.length
        # - 1 <= m,n <= 10^5
        # - s and t consist of uppercase and lowercase English letters.

        # Topic: Sliding Window
        # This is a Hash Table, String, or Sliding Window problem.

        # Approach 1:
        # - If 't' is an empty string, return "".
        # - Define countT and window as two dictionaries.
        # - For all the characters in 't', count the frequencies of the
        # characters and populate countT.
        # - Define have and need; set have to 0 and need to len(countT).
        # - Define res, resLen; set res to [-1,-1] and resLen to 
        # float("infinity").
        # - Set 'l' to 0.
        # - Define a for() loop that goes up to len(s).
        # - Define c = s[r].
        # - Update the window for the character c.
        # - If 'c in countT' and 'window[c] == countT[c]', increment have 
        # by +1.

        # - Define while() loop such that 'have == need'. Everything below is 
        # inside the while() loop.
        # - If '(r-l+1) < resLen', the update res and resLen.
        #   - res = [l,r]
        #   - resLen = r-l+1
        # - Pop from the left of our window. 
        #   - c = s[l]
        #   - window[c] -= 1
        # - If 'c in countT' and 'window[c] < countT[c]', do the following:
        #   - have -= 1
        # - Increment 'l' by +1.

        # - This is outside the while() loop.
        # - Do 'l,r = res'.
        # - Return 's[l:r+1]' if 'resLen != float("infinity")' else ''.


        
