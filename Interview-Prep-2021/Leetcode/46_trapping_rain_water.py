class Solution(object):
  def trap(self, height):
    # Approach 1:
    # Had to totally look at the answer as this was not going to be a problem that I was able to solve myself.
    # There are two key tricks with respect to this problem that I didn't think about:
    # 1) If there are two or less bars, then you cannot trap any water.
    # 2) Water can only be trapped above bars 1..n-2. Therefore, you want to do a two pointer problem from 1..n-2.
    # 3) If the current bar is greater than the max left bar, update max left. Else, update trapped water. Increase
    # the pointer. Use symmetry to do the same thing for the right side. 
    # 4) Return the trappedWater total as the answer.

    #---------
    # TC: O(N)
    # SC: O(1)
    #---------

    # NOTE: I was not going to solve this problem because I had no intuition as to how I should solve it. But
    # You know this is good practice for me!

    n = len(height)

    if n <= 2:
      return 0

    left = 1
    right = n-2
    leftMax = height[0]
    rightMax = height[n-1]
    trappedWater = 0

    while left <= right:
      if (leftMax < rightMax):
        if height[left] >= leftMax:
          leftMax = height[left]
        else:
          trappedWater += leftMax - height[left]

        left += 1
      else:
        if height[right] > rightMax:
          rightMax = height[right]
        else:
          trappedWater += rightMax - height[right]

        right -= 1

    return trappedWater

foo = Solution();
print(foo.trap([0,1,0,2,1,0,1,3,2,1,2,1]));