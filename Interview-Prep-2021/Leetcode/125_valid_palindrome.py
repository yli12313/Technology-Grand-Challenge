# Link: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        
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
