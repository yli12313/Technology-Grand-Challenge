# LINK https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
  def trap(self, height):
    # Approach 1:
    # Had to totally look at the answer as this was not going to be a problem that I was able to solve myself.
    # There are two key tricks with respect to this problem that I didn't think about:
    # 1) If there are two or less bars, then you cannot trap any water.
    # 2) Water can only be trapped above bars 1..n-2. Therefore, you want to do a two pointer problem from 1..n-2.
    # 3) If the current bar is greater than the max left bar, update max left. Else, update trapped water. Increase
    # the pointer. Use symmetry to do the same thing for the right side. 
    # 4) You calculate the trapped water above a bar based on the smaller one between the max left bar or max right bar.
    # 4) Return the trappedWater total as the answer.

    #---------
    # TC: O(N)
    # SC: O(1)
    #---------

    # NOTE: I was not going to solve this problem because I had no intuition as to how I should solve it. But
    # You know this is good practice for me!

    n = len(height)
    
    # TRICK: Set the leftMax, rightMax, left (pointer), right (pointer).
    leftMax = height[0]
    rightMax = height[n-1]
    left = 1
    right = n-2

    # TRICK: Set 'trapped_water' variable to 0.
    trapped_water = 0

    # TRICK: Set while() loop to 'left <= right'.
    while left <= right:
      # TRICK: If the smaller bar is on the left side, which defines the water level!
      if leftMax < rightMax:
        # TRICK: If the 'leftMax' bar is smaller than the corrent 'height[left]', update leftMax.
        if leftMax < height[left]:
          leftMax = height[left]
        else:
          # TRICK: Calculate the 'trapped_water'.
          trapped_water += leftMax - height[left]

        # TRICK: Update left pointer.
        left += 1
      else:
        # TRICK: Use the principle of symmetry right here! Check if 'rightMax' is less than 'height[right]'.
        if rightMax < height[right]:
          rightMax = height[right]
        else:
          trapped_water += rightMax - height[right]

        right -= 1
    
    return trapped_water

foo = Solution();
print(foo.trap([0,1,0,2,1,0,1,3,2,1,2,1]));
