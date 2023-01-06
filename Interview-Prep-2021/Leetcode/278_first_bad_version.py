# LINK: https://leetcode.com/problems/first-bad-version/

# NOTE: Surprisingly, this was the first LeetCode problem that I've solved myself
# without looking at the answers in a long time! When you are confused and frustrated:
# my best advice is to keep going and start doing stuff (anything) to help solve the 
# problem. 

# For this problem specifically, when you need to find the inflection point when the 
# values change from F --> T using binary search:

# [F,F,F,F,T,T,T]

# Set a variable to the inspected value that corresponds to 'mid' when you update the
# right edge ['right=mid-1'].

class Solution(object):
  def firstBadVersion(self, n):
    left=1
    right=n
    answer=-1

    while left<=right:
      mid=(left+right)//2
      current=isBadVersion(mid)

      if not current:
        left=mid+1
      else:
        answer=mid
        right=mid-1
                
    return answer