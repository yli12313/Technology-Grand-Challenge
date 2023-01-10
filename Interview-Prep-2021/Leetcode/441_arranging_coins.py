# LINK: https://leetcode.com/problems/arranging-coins/

# NOTE: I learned a lot solving this problem the first time without looking at someone else's solution!
# Even though this is an easy problem on LeetCode, I still felt it was pretty tricky. I think that for me 
# personally, the key to getting better at algorithms is to start by typing notes and naturally flow into a 
# solution when I see a new problem, and not rely on memory to regurgitate a memorized solution. 

# I made a breakthorough with this problem when three things happened:
# - 1) I realized that I should appy the formula 'n(n+1)/2'.
# - 2) I needed to save the cutoff point and answer in a variable.
# - 3) I needed to treat the case wih 'n=1'. Be careful of edge cases (i.e. the zero case or the one case) and 
#      default return values! 

class Solution(object):
  def arrangeCoins(self, n):
    left=1
    right=n
    answer=1

    while left<=right:
      mid=(left+right)//2

      current_sum=mid*(mid+1)/2

      if current_sum>n:
      	answer=mid-1
      	right=mid-1
      else:
      	left=mid+1

    return answer

foo = Solution();
print(foo.arrangeCoins(1)); 