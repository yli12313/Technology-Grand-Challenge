# LINK: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

# NOTE: This was a pretty challenging problem for me. I almost had the right solution and
# it was this piece of logic 'arr2[mid] > arr1_element' that I could not figure out. If you 
# checked that the difference of 'arr1_element' and 'arr2[mid]' was NOT less than or equal to
# the distance, then you have to figure out which side of the binary search to update the edges.
# This walways seems to give me trouble, the conditions that you check to update the conditions
# in binary search.

# For this problem, you are comparing the element in 'arr2' with the element in 'arr1'.
# - If element2 > element1, then move left and update the right edge to: mid-1. We want to: [Make the difference less by moving left].
# - If element2 < element1, then move right and update the left edge to: mid+1. We want to: [Make the difference more by moving right].

# This is a very confusing problem that I'm not sure I still fully understand yet, but all I know is 
# that the two biggest takeaways from the problem is:
# 1) This logic is important: 'arr2[mid] > arr1_element'
# 2) Be really careful with if-statement logic with regard to binary search. You can solve most
# binary search problems with an: if-elif-else block.

class Solution(object):
  def findTheDistanceValue(self, arr1, arr2, d):
    if len(arr1)==0 or len(arr2)==0:
      return -1

    arr1=sorted(arr1)
    arr2=sorted(arr2)

    count=0

    for arr1_element in arr1:
      left=0
      right=len(arr2)-1

      while left<=right:
        mid=(left+right)//2

        if abs(arr1_element-arr2[mid])<=d:
  	      count+=1
  	      break
        elif arr2[mid] > arr1_element:
  	      right=mid-1
        else:
  	      left=mid+1

    return len(arr1)-count

foo = Solution();
print(foo.findTheDistanceValue([-3,10,2,8,0,10], [-9,-1,-4,-9,-8], 9));

###################################################
## Tracing the code for a use case; answer is: 2 ##
###################################################

# arr1: [-3,0,2,8,10,10]
# arr2: [-9,-9,-8,-4,-1]
# d: 9

# count=0; count=1; count=2; count=3

# arr1_element=-3; left=0;right=4; mid=(0+4)//2 => 2
# abs(-3-arr2[2]) => abs(-3-(-8)) => 5 <= 9 [O]

# arr1_element=0; left=0;right=4; mid=(0+4)//2 => 2
# abs(0-arr2[2]) => abs(0-(-8)) => 8 <= 9 [O]

# arr1_element=2; left=0;right=4; mid=(0+4)//2 => 2
# abs(2-arr2[2]) => abs(2-(-8)) => 10 > 9 [X]
# arr2[2] > 2 => -8 > 2 [X]
# left=2+1; left=3;right=4; mid=(3+4)//2 => 3
# abs(2-arr2[3]) => abs(2-(-4)) => 6 <= 9 [O]

# ...

#################################################
## Tracing a use case for why the answer is: 2 ##
#################################################

# arr1: [-3,0,2,8,10,10]
# arr2: [-9,-9,-8,-4,-1]
# d: 9

# -3: X
# |-3-(-9)|=6 <= 9

# 0: X
# |0-(-9)|=9 <= 9

# 2: X
# |2-(-9)|=11 > 9
# |2-(-9)|=11 > 9
# |2-(-8)|=10 > 9
# |2-(-4)|=6 <= 9

# 8: X
# |8-(-9)|=17 > 9
# |8-(-9)|=17 > 9
# |8-(-8)|=16 > 9
# |8-(-4)|=12 > 9
# |8-(-1)|=9 <= 9

# 10: O
# |10-(-9)|=19 > 9
# |10-(-9)|=19 > 9
# |10-(-8)|=18 > 9
# |10-(-4)|=14 > 9
# |10-(-1)|=11 > 9

# 10: O
# |10-(-9)|=19 > 9
# |10-(-9)|=19 > 9
# |10-(-8)|=18 > 9
# |10-(-4)|=14 > 9
# |10-(-1)|=11 > 9

