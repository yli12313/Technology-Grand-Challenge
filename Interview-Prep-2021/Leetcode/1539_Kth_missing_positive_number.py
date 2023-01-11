# LINK: https://leetcode.com/problems/kth-missing-positive-number/

# THOUGHTS: This was not a hard problem at all, but I did not think about the problem
# the right way. I did not realize that to get the 'k-th' missing value, you have to iterate
# through the array and add all elements that are '<=k' to 'k' to get the answer. What I
# learned from this problem is that:

# 1) When you don't have the right approach in the beginning after trying to generate a solution, 
# it's better to look at the answers and or seek a second opinion. I thought about constructing
# the missing values array, but that was totally not the right approach.

# 2) The key is to solve the problem! Some problems maybe labeled as a certain topic, but you can
# solve the problem using a totally different approach. I tried using binary search to this
# problem when really it wasn't a binary search problem. It was more of an array iteration problem
# with a small trick to it. Next time, I will be more open-minded!

class Solution(object):
  def findKthPositive(self, arr, k):
    for element in arr:
      if element<=k:
        k+=1
      else:
        break

    return k

foo = Solution();
print(foo.findKthPositive([1,2,3,4], 2));