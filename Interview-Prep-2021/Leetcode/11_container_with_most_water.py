#LINK: https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        # Constraints:
        # - n == height.length
        # - 2 <= n <= 10^5
        # - 0 <= height[i] <= 10^4

        # Topic: Two Pointers
        # This is an Array, Two Pointers, and Greedy Algorithm problem.

        # Approach 1:
        # - Define an 'ans' variable.
        # - Define l,r pointers such that 'l = 0' and 'r = len(height)-1'.
        # - Loop through 'height' with the condition 'while l<r:'.
        # - Check if 'height[l] < height[r]'.
        # - If so, then do a caculation: 'ans = max(ans, (r-l)*height[l])'.
        # Increase left pointer.
        # - Else, 'ans = max(ans, (r-l)*height[r])'. Increase right pointer.
        # - Return 'ans'.

        # NOTE: Eliminate "uhmm" as you are going through the problem!

        # TC: O(N)
        # SC: O(1)

        # TRICK: Always ask right after the approach, do I need to define 
        # a return 'ans'! Almost always, it's yes!
        ans = -1
        l,r = 0, len(height)-1

        while l<r:
            if height[l]<height[r]:
                ans = max(ans, (r-l)*height[l])
                # TRICK: Make sure that you increase the left pointer.
                l += 1
            else:
                ans = max(ans, (r-l)*height[r])
                # TRICK: Make sure that you decrease the right pointer.
                r -= 1
        
        return ans
