# Link: https://leetcode.com/problems/rotate-image/

import math

class Solution(object):
  def rotateIndex(self, i, j, n):
    # Return the index of the rotated cell for index i, j.
    return j, n-1-i
    
  def rotate(self, matrix):
    # if the matrix is empty, then return none.
    if matrix == None:
      return None
        
    # Get the length of the matrix.
    n = len(matrix)
        
    # Loop through the sub-section of cells of the matrix that 
    # we will use to rotate our matrix (i.e the red box).
    for i in range(int(math.floor(n/2.0))):
      for j in range(int(math.ceil(n/2.0))):
        # Create the temporary list [-1, -1, -1, -1].
        temp = [-1]*4

        # Get the current i, j index.
        cur_i, cur_j = i, j
                
        for k in range(4):
          # Populate the temp list with the the value of the cell.
          # Get the index of the next cell in the set of 4 values.
          # Keep doing it until temp is populated: [X, X, X, X].
          temp[k] = matrix[cur_i][cur_j]

          # Use the rorateIndex() function to get the next set of 
          # index values.
          cur_i, cur_j = self.rotateIndex(cur_i, cur_j, n)
                
        for k in range(4):
          # Use the temp list [X, X, X, X] to do the rotation.
          # logic: (K - 1) % 4

          # 0: (0 - 1) % 4 --> 3
          # 1: (1 - 1) % 4 --> 0
          # 2: (2 - 1) % 4 --> 1
          # 3: (3 - 1) % 4 --> 2

          # Notice how in our example:
          # [1, 3, 9, 7] when rotated is: [7, 1, 3, 9]

          # The INDEX values that can do that is: [3, 0, 1, 2]

          # Populate the matrix with rotated values.
          matrix[cur_i][cur_j] = temp[(k+3) % 4]

          # Use the rorateIndex() function to get the next set of 
          # index values.
          cur_i, cur_j = self.rotateIndex(cur_i, cur_j, n)
