# LINK: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        # Constraints:
        # - 3 <= nums.length <= 3000
        # -10^5 <= nums[i] <= 10^5

        # Topic: Array
        # This is an Array, Two Pointers, Sorting problem.

        # Approach 1:
        # - [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2] (Sorted)
        # (Naive Approach)
        # - Generate all triplet pairs of indicies.
        #   - How would you do this?
        # - Check if the values add up to 0 and if the set of triplet values have not been seen 
        # before.

        # Approach 2 (Neetcode):
        # - You need both a for() loop and within that a two pointer problem.
        # - Define a for() loop that loops through nums.

        n = len(nums)-1
        # Define and return results.
        result = []
        # TRICK: Key point! Have to sort the 'nums' list.
        nums.sort()

        # TRICK: for() loop problem with a two pointers problem within it.
        for i in range(n):
            # Check that if you keep hitting duplicate values, then you have to 'continue' onto
            # the next value.
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            a = nums[i]
            # Two pointers are always set at 'i+1' and 'n' where 'n=len(nums)-1'.
            l,r = i+1, n

            while l<r:
                three_sum = a + nums[l] + nums[r]

                if three_sum == 0:
                    # TRICK: Append the result.
                    result.append([a, nums[l], nums[r]])

                    # TRICK: Update and increase the l pointer.
                    l += 1

                    # TRICK: While 'l<r' and you've found duplicate values i.e. 'nums[l] == nums[l-1]',
                    # increase the l pointer.
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif three_sum < 0:
                    l+=1
                else:
                    r-=1
        
        return result

