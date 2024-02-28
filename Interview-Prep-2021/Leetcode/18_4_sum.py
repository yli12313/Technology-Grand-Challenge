# LINK: https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        # Constraints
        # - 1 <= nums.length <= 200
        # - -10^9 <= nums[i] <= 10^9
        # - -10^9 <= target <= 10^9

        # Topic: Array
        # This is an Array, Two Pointers, Sorting problem.

        # Approach 1 (Copilot):
        # - Just see the comments.

        # TC: O(N^3), because there's three nested loops (implemented through recursion).
        # SC: O(N), because the space required for the recursion stack in the worst case is N.
        # Another way of saying it is that: 'the depth of the recursion is at most N'.

        # Make sure to sort the 'nums' list first!
        nums.sort()
        results = []
        
        # Calling an auxiliary function where you are passing in:
        #   - 'nums' list
        #   - 'target' to hit
        #   - '4'
        #   - Empty list '[]' to hold a result
        #   - 'results' list that holds all the answers
        self.findNsum(nums, target, 4, [], results)
        
        return results

    # TRICK: Have to pass the number of elements to consider for sum 'N' into this function!
    def findNsum(self, nums, target, N, result, results):
        n = len(nums)
        
        # If length of 'nums' is less than N (number of elements to consider for sum), return.
        # If N is less than 2, return.
        if n < N or N < 2: 
            return None

        # solve 2-sum in an if() statement.
        if N == 2:
            l, r = 0, len(nums)-1

            # TRICK: Define the while() loop after you define 'l' and 'r'.
            while l < r:
                temp = nums[l] + nums[r]
                
                # Case 1: Left and right hit target.
                if temp == target:
                    
                    # Operations performed:
                    #   1) Update results.
                    #   2) Update left pointer.
                    #   3) Update left pointer again if the same value is encountered.
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    # TRICK: The first part of the condition is 'while l<r'.
                    while l<r and nums[l-1] == nums[l]:
                        l += 1

                # Case 2: Left and right is less than target.
                elif temp < target:
                    l += 1

                # Case 3: Left and right is greater than target.
                else:
                    r -= 1
        else:
            # TRICK: We need to find N numbers that add up to the target. 
            # So we only need to consider up to the 'len(nums)-N+1'th element.
            # Remember, the for() loop is the first thing right after else!
            for i in range(n-N+1):
                # TRICK: If target is less than the smallest possible sum (current number times N),
                # or greater than the largest possible sum (which is the last number times N),
                # you can break early because you can't find N numbers that sum to target.
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                # TRICK: Use this line to avoid duplicates.
                # The line is: 'i == 0 or i > 0 and nums[i-1] != nums[i]'.
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    # Call the recursive function with the current number; operations performed:
                    #   1) Update nums array to the next value.
                    #   2) Decrease 'target' by 'nums[i]'.
                    #   3) 'N-1', because we've chosen one number.
                    #   4) 'result + [nums[i]]', because we're updating result.
                    #   5) No change made to 'result'.
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        
        # Return by default.
        return None
