# LINK: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        # Constraints
        # - 1 <= s.length <= 10^5
        # - s consists of only uppercase English letters.
        # - 0 <= k <= s.length

        # Topic: Sliding Window
        # This is a Hash Table, String, or Sliding Window problem.
        # TRICK: In this problem, the Hash Table was a list of size 26 that maps to the 
        # uppercase English character set! This DID NOT use a dictionary as a Hash Table!

        # Approach 1 (Documenting YouTube code):
        # - Define variable to store the length of s.  
        # - Define list of size 26 to store the variable counts.
        # - Set left and right pointers to the first character.
        # - Define longest: consecutive count of the same character.
        # - Define ans: longest substring with the same consecutive 
        # character after substitution.

        # - Do a for loop that goes from right to the end of the string 's'.
        # - Increase the count of the character in the list of size 26.
        # - Update maxCount if we've found a new value.
        # - Update left side of the sliding window.
        #   - Do a while() loop with the logic: 'right-left-maxCount+1 > k'.
        #   - Decrement the count of the character that the left pointer points 
        #     to.
        #   - Increment the left pointer.
        # - Update the answer using the max function and the logic 'right-left+1'.
        # - Return the answer.

        # Approach 2 (My own try):
        # - Define left pointer and set them at 0.
        # - Define a counts list that will count the frequencies of each character
        # encountered.
        # - Define a variable that will keep track of the consecutive count of the same
        # character.
        # - Define an ans variable and return it.
        # - Loop using a for() loop from right = 0 to the end of the string 's'.
        # - Update the count of the characters encountered in the list of size 26.
        # - Update the variable that keeps track of the consecutive count of the same character.
        # - See if we can perform an operation to change one of the characters.
        # - If so, update the count of the left pointer by '-1' in the list of size 26.
        # - Increase the left pointer.
        # - Update the ans and see if we have a new answer.
        # - Return the ans variable.

        # TC: O(N)
        # SC: O(1)

        n = len(s)
        # TRICK: This is a list of size 26 populated by all 0s!
        # TRICK: Don't forget to define this please. This should be defined right away.
        counts = [0]*26
        l = 0
        longest = 0
        ans = 0

        # TRICK: Because we are using a for() loop, we do NOT need to increment r
        # itself.
        for r in range(0,n):
            c = s[r]
            counts[ord(c)-ord('A')] += 1
            longest = max(longest, counts[ord(c)-ord('A')])

            # TRICK: This is calculating the number of characters we have to change in the 
            # sliding window. We are checking if this is greater than 'k'.
            # TRICK: We need to '+1' for the new character that we added to the sliding window
            # in every iteration of the for() loop.
            while r-l-longest+1 > k:
                # TRICK: When the condition 'r-l-longest+1 > k' is met, it's time to update
                # the left side of the sliding window.
                c1 = s[l]
                counts[ord(c1)-ord('A')] -= 1
                l += 1

            # TRICK: It's 'r-l+1'!
            ans = max(ans, r-l+1)

        return ans
