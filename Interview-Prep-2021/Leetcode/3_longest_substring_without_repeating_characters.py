# LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    # Constraints
    # - 0 <= s.length <= 5 * 10^4
    # - s consists of English letters, digits, symbols and spaces.

    # Topic: Two Pointers (Tortoise and Hare)
    # This is a Hash Table, String, or Sliding Window problem.

    # Approach 1:
    # - Define an ans variable, left and right pointers, and a dictionary
    # to hold the current substring.
    # - Loop while the right pointer is less than the length of string 's'.
    # - If the character encountered is NOT in the dictionary:
    #   - Add the current character to the dictionary.
    #   - Calculate the max substring w/o repeating characters, and update
    #   the value if we've found a new max.
    #   - Increase the right pointer.
    # - Else, Pop the value from the dictionary using the left pointer. In-
    # crease the left pointer.
    # - Return the answer.

    # TC: O(N): Both pointers traverse the string once.
    # SC: O(min(N,M))
    #   - N is the length of the input string 's'.
    #   - M is the number of unique characters in the string.
    
    # TRICK: Set the two pointers, the dictionary to keep track of the longest substring, and 
    # the curren maximum substring length.
    i = 0
    j = 0
    dic = {}
    max_substring = 0

    # TRICK: While the second pointer is still in play, keep looping.
    while j < len(s):
      c = s[j]
      
      # TRICK: If a new character is found starting at index 0, add it to the dictionary.
      # Increase the second pointer and calculate the length of the  current longest
      # substring.
      if c not in dic.keys():
        dic[c] = 1
        j += 1
        distance = len(dic)
        max_substring = max(distance, max_substring)

      # TRICK: If we found a duplicate character, pop() the exiting character that's 1/2 of
      # the duplicate and increase the first pointer. The colde will go back to the while()
      # loop and add the ducplicate value found in the next iteration of the while() loop.
      # The duplicate found is special because it could be part of the longest substring 
      # for another substring that beyond the first substring. Increase the first pointer.
      else:
        c = s[i]
        dic.pop(c)
        i += 1
    
    # TRICK: Return the length of the maximum longest substring.
    return max_substring

foo = Solution();
print(foo.lengthOfLongestSubstring("pwwkew"));
