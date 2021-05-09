class Solution(object):
  def merge(self, nums1, m, nums2, n):
    # List the conditions
    # if one of the list has values and the other does not have any values, return the
    # one that has values

    # if both lists are 0, then return the empty list

    # Algorithm
    # Look through the list with the lesser elements, find where it's bigger than an element 
    # and lesser than or equal to an element and insert it there... then shift and move the
    # other elements down. if it's bigger than all the other elements, then insert it at the
    # end

    



foo = Solution();

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
print(foo.XXX(nums1,m,nums2,n));