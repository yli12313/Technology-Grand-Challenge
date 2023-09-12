# LINK: https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        # Constraints:
        # - 1 <= s1.length, s2.length <= 10^4
        # - s1 and s2 consist of lowercase English letters.

        # Topic: String.
        # This is a Hash Table, Two Pointers, String, or Sliding Window problem.

        # Approach 1 (My approach):
        # - Get the length of s1 and s2.
        # - Loop through from 0..m-n+1 (non-inclusive of m-n+1), basically these are all the
        # indices in s2 where s1 could be a substring of s2.
        # - Check if 'sorted(list(s1)) == sorted(list(s2[i:i+n]))'. If so, return True.
        # - Return False.

        # TC: Pretty terrible due to sorting operations.
        # SC: Pretty terrible due to sorting operations.

        """
        n = len(s1)
        m = len(s2)
        s1_updated = sorted(s1)

        for i in range(m-n+1):
            if s1_updated == sorted(s2[i:i+n]):
                return True

        return False
        """

        # Approach 1:
        # - Define two lists that are of length 26 (l1, l2) and populated with 0s.
        # - Define variables to hold the length of s1 (n) and s2 (m).
        # - Define pointers l,r that are both set to 0.
        # - If n > m, return False.
        # - Define a while() loop that loops from r<n.
        # - Update the character frequencies for l1 and l2.
        # - Increase the r pointer.
        # - Outside the while() loop, decrease the r pointer.
        # - While r<m, go into another while() loop.
        # - If l1 and l2 are equal, the return true.
        # - Increment the right pointer.
        # - If r is not equal to m, then update the list l2 using the right pointer to increment 
        # the frequency of the character encountered.
        # - Update the list l2 using the left pointer to decrement the frequency of the left-most 
        # character in the sliding window.
        # - Increment the left pointer by 1.
        # - Return False. 

        # TC: O(26*N)
        # SC: O(1); the lists used have a fixed size of 26. The amount of memory used by the 
        # algorithm is constant, regardless of the input size.

        # NOTE: 
        # - (DICTIONAIRES) When you compare two dictionaries in Python using '==', it 
        # checks if the key-value pairs of the two dictionaires are equal. 
        # - (ANAGRAMS): When you have anagrams, think hash tables and frequency tables!
        
        # TRICK: Making this lists is what makes the problem easier. You need
        # to write more code if you do not work with lists.
        l1,l2 = [0]*26,[0]*26
        n,m = len(s1),len(s2)
        l,r = 0,0

        # TRICK: Don't forget this check!
        if n>m:
            return False

        while r<n:
            l1[ord(s1[r])-ord('a')] += 1
            l2[ord(s2[r])-ord('a')] += 1
            r += 1
        r -= 1

        while r<m:
            if l1 == l2:
                return True
            # TRICK: Make sure to update the right pointer.
            r += 1
            # TRICK: Make sure this condition is correct: 'r != m'.
            # TRICK: (Writing this again) Make sure this condition is correct: 'r != m'.
            if r != m:
                # TRICK: Addition operation on l2 using 'r'.
                l2[ord(s2[r])-ord('a')] += 1
            # TRICK: Subtraction operation on l2 using 'l'.
            l2[ord(s2[l])-ord('a')] -= 1
            # TRICK: Make sure that you increment the left pointer.
            l += 1
        
        return False
