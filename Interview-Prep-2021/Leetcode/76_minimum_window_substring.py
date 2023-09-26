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
        # - c = s[l]
        # - window[c] -= 1
        # - If 'c in countT' and 'window[c] < countT[c]', do the following:
        #   - have -= 1
        # - Increment 'l' by +1.

        # - This is outside the while() loop in the body of minWindow itself.
        # - Do 'l,r = res'.
        # - Return 's[l:r+1]' if 'resLen != float("infinity")' else ''.

        # TC: O(N)
        # SC: 

        if t == "":
            return ""

        countT,window = {},{}

        for c in t:
            countT[c] = 1+countT.get(c,0)
        
        have,need = 0,len(countT)
        res,resLen = [-1,-1],float("infinity")
        l = 0

        for r in range(len(s)):

            # TRICK: Upate window.
            c = s[r]
            window[c] = 1+window.get(c,0)

            # TRICK: Update the have variable.
            if c in countT and window[c] == countT[c]:
                have += 1

            # TRICK: When the 'have == need' condition is met!
            while have == need:
                # TRICK: Update 'res' and 'resLen'.
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                # TRICK: Make sure you get this part right! 'window[c] -= 1', where 'c = s[l]'.
                # TRICK: Update left portion of the sliding window.
                c = s[l]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                l += 1
            
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
