# LINK: https://leetcode.com/problems/search-a-2d-matrix/

# NOTE: One of the MOST IMPORTANT LeetCode problems I've ever solved! The trick to LeetCode
# is to always keep going. If you are frustrated with a problem, don't lose hope and let
# your mind start ruminating with negative self talk! If you try again, and again, and again,
# sooner or later you will solve the problem. The applies to ANY LeetCode problem. 

# I was only able to solve this problem because it resembled Problem 1351 which I solved earlier.
# The easy problems in LeetCode are actually extremely important. You need to master the
# easy problems first to build up the fundamentals and build up confidence before you can tackle
# medium problems. Going straight to medium problems will not help you build the fundamentals and
# might have a negative impact on your confidence, thus leading you to doubting your abilities. Don't
# let this happen!

# This might have been the first LeetCode medium of some significance that I've solved by myself. 
# It's taken a long time, but I'm going to keep going!

# This problem was not hard; it had two parts:
# 1) Extract the right row.
# 2) Do binary search on the extracted row.

class Solution(object):
  def searchMatrix(self, matrix, target):
    row_extracted=[]
    answer=False
  
    ## [Row extraction part] ##
    if len(matrix)==1:
      row_extracted=matrix[0]
    else:
      for row in matrix:
        if target>=row[0] and target<=row[len(row)-1]:
          row_extracted=row
    
    # Checking if the extracted row has only one element, returning
    # true/false in a simple check if so.
    if len(row_extracted)==1:
      return row_extracted[0]==target

    ## [Binary search part] ##
    left=0
    right=len(row_extracted)-1

    while left<=right:
      mid=(left+right)//2

      if row_extracted[mid]==target:
        answer=True
        break
      elif row_extracted[mid]<target:
        left=mid+1
      else:
        right=mid-1

    return answer;

foo = Solution();
print(foo.searchMatrix([[1]],1));
