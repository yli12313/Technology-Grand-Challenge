# LINK: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution(object):
  def maxDistance(self, nums1, nums2):
    # Approach 1:
    # For the arrays: [55,30,5,4,2], [100,20,10,10,5]
    #   With indexes: [ 0, 1,2,3,4], [  0, 1, 2, 3,4]
    # The pairs of indices are:
    # - (0,0), (0,1), (0,2), (0,3), (0,4)
    # - (1,1), (1,2), (1,3), (1,4)
    # - (2,2), (2,3), (2,4)
    # - (3,3), (3,4)
    # - (4,4)

    # Set the current distance to -1
    # Set two for() loops:
    # - The first for() loop will go from 0 --> 4 (inclusive)
    # - The second for() loop will go from:
    # - 4 --> 0 (inclusive, when the first for() loop is 0)
    # - 4 --> 1 (inclusive, when the first for() loop is 1) 
    # Calculate the distance.
    # set the distance to the max of the old and new distance.

    # Approach 1 works! But it is the brute-force solution. Need to optimize.
    """
    distance = 0
    for i in range(len(nums1)):
      for j in range(i, len(nums2)):
        if nums1[i] <= nums2[j]:
          distance = max(j-i, distance)

    return distance
    """

    # Approach 2:
    # The two conditions with regard to this problem are:
    # - We need to have i <= j
    # - We need to have nums1[i] < nums2[j]
    # - If we have these two conditions, then we can calculate j - i

    # Set two pointers
    # i --> starts at the first index of nums1
    # j --> starts at the first index of nums2
    # do a while() loop that iterates over both i and j

    # (Wrong intuition!)
    # If nums1[i] > nums2[j], then increase i
    # If i > j, then increase j
    # Else calculate the answer 

    # (Correct intuition!)
    # If nums1[i] <= nums2[j], then calculate the answer and increase j
    # Else increase i

    i = 0
    j = 0
    max_distance = 0

    while (i < len(nums1) and j < len(nums2)):
      if (nums1[i] <= nums2[j]):
        max_distance = max(max_distance, j - i)
        j += 1
      else:
        i += 1

    return max_distance

foo = Solution();
print(foo.maxDistance([5,4], [3,2]));