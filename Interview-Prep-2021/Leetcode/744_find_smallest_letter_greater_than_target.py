# LINK: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# NOTE: This binary search is different than the other ones that I've seen because
# you don't need to find the 'target'; you just need to find the value that's the
# the smallest-large value w.r.t. the 'target'. If all the values are smaller than the
# 'target', then you should just return the first element in [letters]. 

# An interesting thing w.r.t. this problem:
# - ['e','e','e','e,'e','t','t']

# In this situation, it's not clear which side (left or right) you should move when you do
# the binary search. The logic that solves this is: 'letters[mid]<=target'. Move right when you
# see an element that's less than or equal to the 'target'.

class Solution(object):
  def nextGreatestLetter(self, letters, target):
    left=0
    right=len(letters)-1
    target_index=-1

    while left<=right:
      mid=(left+right)//2

      if letters[mid] <= target:
        left=mid+1
      else:
        target_index=mid
        right=mid-1

    return letters[0] if target_index==-1 else letters[target_index]

foo = Solution();
print(foo.nextGreatestLetter(["x","x","y","y"], "z"));