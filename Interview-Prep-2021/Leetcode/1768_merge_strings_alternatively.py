# LINK: https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
  def mergeAlternately(self, word1, word2):
    # Brainstorming the solution:
    # - You have to have an answer string.
    # - If word1 is empty and word2 is not, return word2.
    # - If word1 is not empty and word2 is empty, return word 1.
    # - Set pointer to the first character of each word.
    # - Figure out which word is the longer one.
    # - Write if-statement logic to figure out if there exists a 
    # letter in the smaller word. If so add it. 
    # - If not, add the characters in the longer word.  

    # Brainstormed solution was incorrect. Here's the correct solution:
    # - You have to have an answer string.
    # - You have to have a counter that counts how many sets of adjacent
    # characters are in both word1 and word2.
    # - If there are sets of characters in both word1 and word2, add them
    # to the answer and increase the counter +1.
    # - At this point, either one of the strings is empty or both strings
    # are empty.
    # - Check if one of the strings has characters that are beyond the index 
    # delineated by the counter.
    # - If so, have the answer add those additional characters.
    # - Else return the answer!

    answer = ""
    counter = 0

    for x, y in zip(word1, word2):
      answer += x
      answer += y
      counter += 1

    if len(word1) > counter:
      answer += word1[counter:]
    elif len(word2) > counter:
      answer += word2[counter:]
    
    return answer

foo = Solution();
print(foo.mergeAlternately("ab", "pqrs"));
