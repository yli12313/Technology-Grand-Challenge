# LINK: https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        # Topic: Hash Tables.
        # This is correct! It is an array, hash table, string, and sorting problem.

        # Approach 1:
        # - Create a second array and sort each array. 
        # - Loop through each s in strs.
        
        # NOTE: You are correct in some of the intuition, but this is not the full thing. 

        # Approach 2:
        # - Define a hash table where the key->value pair is defined as: 
        # sorted_word->[list of words], where the list of words are all anagrams of each other.
        # - Return the values of the hash table as a list.

        # TC: O(M*N*log(N)) where M is the number of words in the list and N is the max word length.
        # SC: O(M*N) where M is the number of words in the list and N is the average word length.

        # anagram = {}

        # for word in strs:
        #     word_sorted = ''.join(sorted(word))

        #     if word_sorted in anagram.keys():
        #         anagram[word_sorted].append(word)
        #     else:
        #         anagram[word_sorted] = [word]
        
        # return list(anagram.values())

        # Approach 3:
        # - Create a hash table and use a defaultdict of type list.
        # - Loop through the words; loop through the characters in each specific word.
        # - Create a count list that once you convert it to a tuple, will serve as the key in the dictionary!
        # - Use ord() function and subtract from ord('a') to find the index of which element you should increase by one.
        # - Using the tuple of the count list as the key, add the value as the string.
        # - Return the dictionary's values.

        # TC: O(M*N) where M is the number of words in the list and N is the average word length.
        # SC: O(M*N) where M is the number of words in the list and N is the average word length.

        anagram = defaultdict(list)

        for word in strs:
            count = [0]*26

            for c in word:
                count[ord(c)-ord('a')] += 1

            anagram[tuple(count)].append(word)
        
        return anagram.values()
