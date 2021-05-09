# LINK: https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution(object):
  def merge(self, nums1, m, nums2, n):

    ## Alternative Method ##
    # nums1.extend(nums2)
    
    ## List Comprehension ##
    # nums1 = [x for x in nums1 if x != 0]

    ## Filter ##
    # nums1 = list(filter(lambda x: x != 0, nums1))

    for i in range(m, m+n):
      nums1.pop(i)
      nums1.insert(i, nums2.pop(0))
    
    return sorted(nums1)

foo = Solution();

nums1=[0]
m=0
nums2=[1]
n=1
print(foo.merge(nums1,m,nums2,n));