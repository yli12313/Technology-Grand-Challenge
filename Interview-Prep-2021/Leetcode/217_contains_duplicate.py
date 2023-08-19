# LINK: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        # Topic: Array
        # Missed that this was a hash table problem!

        # Approach 1:
        # - Create a hash table.
        # - The key -> value pair will be: value -> count.
        # - If the value doesn't exist, add it to the hash table and increase count to 1.
        # - Else, return true.
        # By default return false.

        # NOTE: Not smart! Don't need to make the problem more complicated than it needs to be.

        # storage = {}

        # for num in nums:
        #     num_string = str(nums)

        #     if num_string not in storage.keys():
        #         storage[num_string] = 1
        #     else:
        #         return True
              
        # return False

        # Approach 2:
        # Solve the problem by utilizing a set and not a hashmap!

        # TC: O(N)
        # SC: O(N)

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
