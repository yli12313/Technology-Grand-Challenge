# LINK: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# NOTE: This one was actually pretty tricky if you don't do the naive approach and you use binary
# search instead. There were many tricks to the problem in my opinion.

# - The first is that for each row in the 2-D array, the elements of the row were ordered in 'non-increasing' order
#   (i.e. the elements got smaller as you traversed the array).
# - Therefore when you encountered a non-negative value through binary search 'nums[mid]>=0', you had to move the left 
#   pointer by 'left=mid+1'.
# - When you find encounter a negative value through binary search, you can assume that number and all the numbers
#   to the right of it are negative, hence the logic 'answer+=right-mid+1'. Note there's a trick here: I originally
#   thought that you just set 'answer' to: 'answer=right-mid+1'. But this only works the first time when the right pointer
#   HAS NOT moved! The right pointer is always moving, so you have to set 'answer' as a running count/total. The correct
#   logic here is:
#     * 'answer+=right-mid+1'
#     * 'right=mid-1'

class Solution(object):
  def countNegatives(self, grid):
    answer=0

    for row in grid:
      left=0
      right=len(row)-1

      while left<=right:
        mid=(left+right)//2

        if row[mid]>=0:
          left=mid+1
        else:
          answer+=right-mid+1
          right=mid-1

    return answer

foo = Solution();
print(foo.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]));

# NOTE2: This is of course the brute-force and naive solution. But we want to explore the
# binary search solution instead!

# class Solution(object):
#   def countNegatives(self, grid):
#     answer=0

#     for i in range(len(grid)):
#       for j in range(len(grid[0])):
#         if grid[i][j] < 0:
#           answer+=1

#     return answer
