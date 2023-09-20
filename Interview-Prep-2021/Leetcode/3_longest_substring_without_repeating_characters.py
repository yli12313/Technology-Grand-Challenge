# LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
  def lengthOfLongestSubstring(self, s):

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
      
      # TRICK: If a new character is found starting at index 0, add it to the dictionary.
      # Increase the second pointer and calculate the length of the  current longest
      # substring.
      if s[j] not in dic.keys():
        dic[s[j]] = 1
        j += 1
        distance = len(dic)
        max_substring = max(distance, max_substring)

      # TRICK: If we found a duplicate character, pop() the exiting character that's 1/2 of
      # the duplicate and increase the first pointer. The colde will go back to the while()
      # loop and add the ducplicate value found in the next iteration of the while() loop.
      # The duplicate found is special because it could be part of the longest substring 
      # for another substring that beyond the first substring. Increase the first pointer.
      else:
        dic.pop(s[i])
        i += 1
    
    # TRICK: Return the length of the maximum longest substring.
    return max_substring

foo = Solution();
print(foo.lengthOfLongestSubstring("pwwkew"));
