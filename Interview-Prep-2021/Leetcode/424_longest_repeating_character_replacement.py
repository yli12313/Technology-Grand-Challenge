# LINK: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        # Constraints
        # - 1 <= s.length <= 10^5
        # - s consists of only uppercase English letters.
        # - 0 <= k <= s.length

        # Topic: Sliding Window

        # Approach 1:
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

        # TC: O(N)
        # SC: O(1)

        n = len(s)
        counts = [0]*26
        l = 0
        longest = 0
        ans = 0

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
            
            ans = max(ans, r-l+1)

        return ans
