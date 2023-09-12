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

        # Approach 2 (Found on YouTube):
        # - Define two lists (l1 and l2) and define the length of 's1' (n) and 
        # 's2' (m).
        # - If the length of 's1' is greater than the length of 's2', return False.
        # - Define the sliding window pointers left (l), right (r) and set them both to 0.
        # - Using a while() loop, loop while the right pointer is less than n.
        # - Update lists and increase pointer.
        # - Decrease pointer to point to the end of the sliding window.
        # - Using a while() loop, loop while the right pointer is less than m.
        # - If l1 equals l2, return True.
        # - Increment the right pointer. 
        # - If l1 does not equal l2, update the second dictionary with the right pointer (+1).
        # - Update the second dictionary with the left pointer (-1); this is outside the if
        # statement.
        # - Increment the left pointer.
        # - Return False; this is outside the while() loop.

        # TC: O(26*N)
        # SC: O(1); the lists used have a fixed size of 26. The amount of memory used by the 
        # algorithm is constant, regardless of the input size.

        # NOTE: (DICTIONAIRES) When you compare two dictionaries in Python using '==', it 
        # checks if the key-value pairs of the two dictionaires are equal. 
        
        # TRICK: Making this lists is what makes the problem easier. You need
        # to write more code if you do not work with lists.
        l1,l2 = [0]*26,[0]*26
        n,m = len(s1),len(s2)
        l,r = 0,0

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
            if r != m:
                l2[ord(s2[r])-ord('a')] += 1
            l2[ord(s2[l])-ord('a')] -= 1
            # TRICK: Make sure that you increment the left pointer.
            l += 1
        
        return False
