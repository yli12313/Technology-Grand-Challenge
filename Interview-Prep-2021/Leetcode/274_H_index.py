# LINK: https://leetcode.com/problems/h-index/

class Solution(object):
  def hIndex(self, citations):
    # Topic: dynamic programming (my guess is wrong). It's a 
    # sorting/counting sort problem.

    # TC: O(Nlog(N))
    # SC: O(1)

    ####

    # Approach 1:
    # 1) Sort the citations in reverse order with the paper with the highest citation
    # at the start.
    # 2) Set the H-index counter to 0. 
    # 3) Do an enumeration with the index,citation pairs in citations starting at index=1.
    # 4) We know that as long as index <= citation, we have 'index' number of papers with 
    # at least 'citation'. Update and increase the H-index.
    # 5) Else you can break and you know that you found the max H-index.
    # 6) Return the H-index.

    citations.sort(reverse=True)

    h=0
    for i,citation in enumerate(citations, start=1):
    	if citation >= i:
    		h = i
    	else:
    		break

    return h

foo = Solution();
print(foo.hIndex([3,0,6,1,5]));