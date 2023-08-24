# LINK: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
  def twoSum(self, numbers, target):
    # Constraints
    # - 1 <= index_1 <= index_2 < numbers.length
    # Numbers is sorted in ascending order.

    # Topics: Hash table.
    # Wrong. This is an array, two pointers, and binary search 
    # problem.

    # Approach 1 (Using a new dictionary):
    # - Create a dictionary d.
    # - Loop through the array.
    # - Create a temporary variable that is 'target-n', where 
    # 'n = numbers[i]'.
    # - If this number is in the dictionary, then return 
    # '[d[temp]+1, i+1]'. 
    # - Add to dictionary: 'd[n] = i'.
    # - Return '[]' by default.

    # TC: O(N)
    # SC: O(1)
    
    """
    d = {}

    for i in range(len(numbers)):
      n = numbers[i]
      temp = target-n

      if temp in d:
        return [d[temp]+1, i+1]
            
      d[n] = i
        
    return []
    """

    # Approach 2 (Using two pointers):
    
    # NOTE: I had to take a look at the answers. This is actually a very easy 
    # It's not a binary search, but actually just a two pointers problem! Two pointers problems
    # are very similar to binary search problems. I was not thinking about the problem
    # the right way at all! Lessons learned from this problem:

    # - Binary search is very similar to two pointers; two pointers is an excellent way to 
    #   solve problems such as two sums, where one pointer is set at the beginning and the
    #   other pointer is set at the end of the array. You increase the left pointer and decrease 
    #   the right pointer until the 'two_sums' add up to the target.

    # - When 'two_sums<target', you update the left pointer so that 'left=left+1', thus increasing the
    #   sum. When 'two_sums>target', you know that you over-shot the target. Therefore, you decrease
    #   the right pointer to make the sum less by doing 'right=right-1'.

    # I think this is my biggest problem with LC: I don't have the intuition yet to know when
    # to apply a specific algorithm to a specific problem right away. I was not even thinking about 
    # two pointers when I first started trying to solve this problem. Therefore, the key to getting 
    # better at LC is to keep practicing and keep taking notes! Then, you'll start recognizing patterns
    # like you did with binary search. 

    """
    left=0
    right=len(numbers)-1

    while left<right:
      two_sums=numbers[left]+numbers[right]

      if two_sums==target:
      	return [left+1,right+1]
      elif two_sums<target:
        left=left+1
      else:
      	right=right-1
    """
    
    # Approach 2.5 (Using two pointers with more optimized code):
    # - Set the left as the first element; right as the last element.
    # - Loop through numbers with the condition 'l<r'.
    # - Caculate the two sum as 'two_sums = numbers[l]+numbers[r]'.
    # - If two sum is less than the target, increase the two sum by
    # incrementing the left pointer 'l += 1'.
    # - Otherwise the two sum is greater than the target, so decrease
    # the two sum by decrementing the right pointer 'r -= 1'.

    # TC: O(N)
    # SC: O(1)

    n = len(numbers)-1
    l, r = 0, n

    while l<r:
      two_sum = numbers[l]+numbers[r]

      if two_sum == target:
        return [l+1,r+1]
      elif two_sum < target:
        l += 1
      else:
        r -= 1
        
    return []
    
foo = Solution();
print(foo.twoSum([2,7,11,15],9));
