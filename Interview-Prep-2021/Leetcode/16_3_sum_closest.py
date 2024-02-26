# LINK: https://leetcode.com/problems/3sum-closest/

class Solution(object):
    def threeSumClosest(self, nums, target):
        # Constraints:
        # - 3 <= nums.length <= 500
        # - -1000 <= nums[i] <= 1000
        # - -10^4 <= target <= 10^4

        # Topic: Array.
        # This is an Array, Two Pointers, Sorting problem.

        # Approach 1 (for() loop + two pointer):
        # SKELETON:
        #   1) Check that the 'nums' list is good.
        #   2) Sort the list. 
        #   3) Calculate the first 'result' and return it.

        # MAIN CODE:
        # - Do a for() loop and define 'l' and 'r' pointers.
        # - Iterate as long as 'l<r'.
        # - Calculate possibly the new result value as 'temp'.
        # - Perform 3 operations:
        #     1) If new result 'temp' equals 'target', then return 'temp'.
        #     2) If new result 'temp' is closer to 'target' than the former 'result', then update 'result'.
        #     3) Update 'l' and 'r' pointers.

        # TC: O(N^2); for() loop is O(N) and two pointers is also O(N).
        # SC: O(log(N)); the space required for sorting is O(log(N)).

        if len(nums) < 3:
            return None

        # TRICK: Don't forget to sort 'nums'! 'nums.sort()' is better syntax than 'nums = sorted(nums)'.
        nums.sort()
        result = nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l < r:
                # TRICK: Calculating 'temp' has to go inside the while() loop!
                temp = nums[i]+nums[l]+nums[r]

                # TRICK: Returning 'temp' here.
                if temp == target:
                    return temp

                # TRICK: Updating 'result' here such that it's equal to 'temp'!
                if abs(temp-target) < abs(result-target):
                    result = temp

                # TRICK: Updating 'l' and 'r' here!
                if temp < target:
                    l += 1
                else:
                    r -= 1

        return result
