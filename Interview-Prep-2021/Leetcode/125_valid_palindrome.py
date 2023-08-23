# LINK: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    
    
    def isPalindrome(self, s):
        # Constraints:
        # - 1 <= s.length <= 2 * 10^5
        # - s consists only of printable ASCII characters.

        # Topic: Two pointers.

        # Approach 1 (June, 2022):
        """
        # If it's an empty string, return True that the string is a palindrome.
        if len(s) == "":
            return True
        
        # Set i to the first index.
        i=0
        
        # Set j to the last index.
        j=len(s)-1
        
        # Set two pointers to the first and last characters in the string.
        p1 = s[i]
        p2 = s[j]
        
        # Loop while the index from the tail > the index from the head.
        while j > i:
            # Check if the first pointer is alphanumeric; if not, move the pointer forward and continue.
            if not p1.isalnum():
                i += 1
                p1 = s[i]
                continue
                
            # Check if the second pointer is alphanumeric; if not, move the pointer backwards and continue.
            if not p2.isalnum():
                j -= 1
                p2 = s[j]
                continue
            
            # Both pointers point to the same character; increase first pointer and decrease the second pointer. Otherwise, return False.
            if p1.lower() == p2.lower():
                i += 1
                p1 = s[i]
                j -= 1
                p2 = s[j]
            else:
                return False
        
        # Return true by default.
        return True
        """

        # Approach 2:
        # - Strip the string of non-alphanumeric characters and convert each character to 
        # lower case.
        # - Set pointer as the index of the first character and pointer as the 
        # index of the last character.
        # - Do a while loop where start < end. See if the characters match each other. If they
        # don't return False. 
        # - Increment the start pointer and decrement the end pointer.
        # - Return True by default.

        # TC: O(N)
        # SC: O(N)

        # NOTE: I had a solution from last June that works, but it's a very convoluted solution.
        # It is a O(N) space complexity solution however. I'm learning a lot from the Neetcode 
        # solutions however.

        # The expression here is (where s is the collection!):
        # (exp for c in s if exp)
        """
        s = "".join(c.lower() for c in s if c.isalnum())

        start = 0
        end = len(s)-1

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
        """

        # Approach 3: Trying the Neetcode solution. This solution is pretty interesting.
        # - Define your own is alphanumeric function.
        # - Define two pointers again.
        # - Use two while() loops to to find only the characters we are looking for.
        # - Compare the values from the two pointers and if they are not equal, return False.
        # - Update pointers.
        # - Return True.

        # TC: O(N)
        # SC: O(1)

        l, r = 0, len(s)-1

        while l<r:
            # When you call a method in a class, you have to use 'self.'
            while l<r and not self.isalnum(s[l]):
                l += 1

            while r>l and not self.isalnum(s[r]):
                r -= 1

            # Right here, you have to call the lower() function! The characters
            # have not been converted to lowercase.
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

    def isalnum(self, c):
        """
        This function only detected if a character is alphanumeric, but does no
        conversion of the actual character!
        """
        return (ord('A') <= ord(c) <= ord('Z')) or \
            (ord('a') <= ord(c) <= ord('z')) or \
            (ord('0') <= ord(c) <= ord('9'))
