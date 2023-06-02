# LINK: https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution(object):
  def differenceOfDistinctValues(self, grid):
    
    ######################
    ## How to use a Set ##
    ######################

    # Initializing the set: topLeft = set()
    # Adding to the set: topLeft.add(tl)
    # Clearing the set: topLeft.clear()
    
    ######################

    # Defining the sets that will hold the distinct diagonal values towards the:
    # - topLeft
    # - bottomRight
    topLeft = set()
    bottomRight = set()

    # Defining a 2-D array that the same size as the given grid.
    answer = [[0]*len(grid[0]) for i in range(len(grid))]
    
    # Looping through every value in the given grid.
    for i in range(len(grid)):
      for j in range(len(grid[0])):

        # Adding the diagonal values from the topLeft to it's corresponding set.
        m = i
        n = j
        while m > 0 and n > 0:
          m -= 1
          n -= 1
          tl = grid[m][n]
          topLeft.add(tl)
        
        # Adding the diagonal values from the bottomRight to it's corresponding set.
        m = i
        n = j
        while m < len(grid)-1 and n < len(grid[0])-1:
          m += 1
          n += 1
          br = grid[m][n]
          bottomRight.add(br)
        
        # Calculate the answer for the (i, j) coordinate.
        answer[i][j] = abs(len(topLeft) - len(bottomRight))

        # Clear the sets so that the answer can be calculated for subsequent (i, j) coordinates.
        topLeft.clear()
        bottomRight.clear()

    # Return the answer.
    return answer

foo = Solution();
print(foo.differenceOfDistinctValues([[1,2,3],[3,1,5],[3,2,1]]));