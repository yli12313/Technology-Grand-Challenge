
# Link: https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums):
        # Initialize the maximum current perimeter as 0.
        maxPerim = 0

        # Sort the nums array in descending order i.e. [2,2,1]
        numsSorted = sorted(nums, reverse=True)
        
        # Loop through the array per every triplet of numbers.
        for i in range(len(nums)-2):
            # Extract the largest side and calculate the sum of the next two largest sides.
            largestSide = numsSorted[i]
            twoSides = numsSorted[i+1] + numsSorted[i+2]
        
            # if the two sides are greater than the largest side, we have a triangle!
            # Compare the parimeter of the new triangle with the max triangle perimemter 
            # encountered; if it's bigger, then we have have a new max triangle perimeter.
            if twoSides > largestSide:
                tempPerim = largestSide + twoSides
                maxPerim = max(tempPerim, maxPerim)
        
        # Return the answer.
        return maxPerim

foo = Solution();
print(foo.largestPerimeter([2,1,2]));
