class Solution(object):
    def longestConsecutive(self, nums):
        # Constraints
        # 0 <= nums.length <= 10^5
        # -10^9 <= nums[i] <= 10^9

        # Topic: Hash table and then sorting.
        # This is an array and hash table problem.

        # Approach 1:
        # - Define a hash table with lists.
        #   Example: 1:[2,3,4], 0:[1,2,3,4,5,6,7,8]
        # - Define an answer and set it to 0 and return the answer.
        # - Doesn't work because this is an unsorted nums list that 
        # you are given.

        # NOTE: Always write out the non-optimal solution!

        # Approach 2:
        # - Start by turning nums into a set to eliminate duplicate values.
        # Duplicate values really slow down solving this problem.
        # - Loop through nums.
        # - For every number in nums, check if (n-1) is NOT in the array.
        # - This mean that we found a starting point.
        # - Create a variable that will serve as the counter for the new streak.
        # - Calculate the streak.
        # Compare the streak to the previous longest one and return the max.
        # - Return the answer.

        # This part was also tricky. Start by creating a set to remove duplicate
        # values in nums.
        nums_set = set(nums)
        best = 0

        for n in nums:
            if (n-1) not in nums_set:
                streak = 0

                # This part was tricky for you. Just start calculating the 
                # streak with a while() loop!
                while n in nums_set:
                    n += 1
                    streak += 1

                """ Neetcode approach:
                streak = 1

                # I would have never come up with this method, but doing
                # 'n+streak' over 'n+1' makes it so that you don't have to
                # do n += 1 inside the while() loop!
                while (n+streak) in nums_set:
                    streak += 1
                """
                
                best = max(best, streak)
        
        return best
