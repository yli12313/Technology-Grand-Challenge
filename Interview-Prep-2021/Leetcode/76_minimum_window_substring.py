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
        # SC: O(S+T); S is the length of the input string 's', and T is the length of the input string 't'.

        if t == "":
            return ""

        countT,window = {},{}

        # TRICK: Make sure you get this syntax correct: the key here is 'c'! Defining and populating countT
        # is the first thing that you must do! We are populating 't' here!
        for c in t:
            countT[c] = 1+countT.get(c,0)

        # TRICK: Define 'have','need' as '0','len(countT)'. 'have' should be 0 and 'need' should have
        # a value right away!
        have,need = 0,len(countT)
        res,resLen = [-1,-1],float("infinity")
        l = 0

        for r in range(len(s)):

            # TRICK: Upate window.
            c = s[r]
            # TRICK: Make show when you update window, you get the syntax correct!
            window[c] = 1+window.get(c,0)

            # TRICK: Update the have variable. Both if statements update the have variable!
            # TRICK: Check that c is in CountT; then check that window[c] == countT[c].
            if c in countT and window[c] == countT[c]:
                have += 1

            # TRICK: When the 'have == need' condition is met! Make sure this is a while() loop!
            # TRICK: Make sure this is a while() loop! (x2)
            while have == need:
                # TRICK: 1) Update 'res' and 'resLen'.
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                    
                # TRICK: 2-Part 1) Make sure you get this part right! 'window[c] -= 1', where 'c = s[l]'.
                # TRICK: 2-Part 2) Update left portion of the sliding window. Decrement the character
                c = s[l]
                window[c] -= 1

                # TRICK: 3) Update have and left pointer.
                if c in countT and window[c] < countT[c]:
                    have -= 1
                l += 1
            
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

        # Approach 1 (From YouTube):
        # - If t is an empty string, then return the empty string.
        # - Define two dictionaires countT and Window.
        # - Populate the countT dictionary.
        # - Define variables have and need.
        # - define variables res, resLen.
        # - Define a left pointer.
        # - Unpack l,r from res.
        # - Return the answer with the correct ternary statement.

        # - Define a for() loop that goes up to len(s).
        # - Add new values to the window. 
        # - Check to see if the character that we just added to the window 
        # is one that we want. If so, update have.
        # - Do a while loop when have == need.
        # - Update res and resLen.
        # - Update the left side of the sliding window and subtract the character 
        # that the left pointer points to.
        # - Do another check to see if we need to update have.
        # - Increment the left pointer.

        # TC: O(N)
        # SC: O(S+T); S is the length of the input string 's', and T is the length of the input string 't'.

        """
        if t == "":
            return ""
        
        countT,window = {},{}

        for c in t:
            countT[c] = 1+countT.get(c,0)
        
        have,need = 0,len(countT)
        res,resLen = [-1,-1],float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                c = s[l]
                window[c] -= 1

                if c in countT and window[c] < countT[c]:
                    have -= 1
                
                l += 1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        """
