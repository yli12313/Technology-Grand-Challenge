# LINK: https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        # Topic: Hash tables.
        # Correct! This can be solved in many ways: Arrays, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue),
        # Bucket Sort, Counting, Quickselect.

        # Approach 1:
        # - Add the num->count as a key-value pair into a hash table.
        # - Sort the hash table by the values.
        # - Return the top k values from the hash table. 
        # Can you solve this without sorting?

        # Approach 2:
        # - We are doing a Bucket Sort approach where you first create a hash table of the
        # counts of each number. 
        # - Then create another list frequency where the index is the count (genius)! The 
        # value per index is a list with all the values with that specific count.
        # - Then go through the frequency list in descending order. Append to a results list
        # the values in frequency (which is a list of lists). You may append multiple from
        # one list to the answer.
        # - If the results list is equal to k, return the results lists.

        # TC: O(N)
        # SC: O(N)

        count = {}
        # You have to add an extra entry in the frequency list because a number could occur
        # zero times.
        freq = [[] for i in range(len(nums)+1)]

        # Add to the count. The count is structured: number -> count.
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Loop through the count and add to the frequency list. We want to structure freq: 
        # freq[c] -> number.
        for n,c in count.items():
            freq[c].append(n)

        # Declaring the resulting answer list.
        res = []

        ## At this point, you are only working with the freq list of lists! ##
        ## Still working with nums! After you construct freq, you only work with freq! ##
        
        # This is looping from the max number of counts possible down to 1 and not including 0!
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
