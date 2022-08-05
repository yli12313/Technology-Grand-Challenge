# Link: https://leetcode.com/problems/sorting-the-sentence/

class Solution(object):
    def sortSentence(self, s):
        # Using a list to hold the string with the words split, including the numbers at the end.
        holder = []

        # Using a second list to hold the sorted word tuples: (index, word).
        holder2 = []
        
        # If the string is empty, return the empty string. 
        if not s:
            return ""

        # Split the string by the " " empty chracter and return a list of words.
        holder = s.split()

        # Loop through the list of words.
        for word in holder:

            # Append the word tuples: (index, word) to a second list.
            holder2.append((word[-1:], word[:-1]))
        
        # Sort the second list for the first index of each tuple element.
        holder2 = sorted(holder2, key = lambda x: x[0])

        # Return the words of the sentence as the answer.
        return ' '.join(map(str, [x[1] for x in holder2])).strip()
    
foo = Solution();
print(foo.sortSentence("is2 sentence4 This1 a3"));
