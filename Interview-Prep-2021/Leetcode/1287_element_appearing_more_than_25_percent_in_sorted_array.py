# Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution(object):
  def findSpecialInteger(self, arr):
    # If the the array is empty, then return None.
    if not arr:
      return None
    
    # Define a dictionary.
    dictionary = {}

    # Using the dictionary, create counts of all the values found in: arr.
    for val in arr:
      if val in dictionary.keys():
        dictionary[val] += 1
      else:
        dictionary[val] = 1
    
    # Return the key with the highest count, which is the element that appears more than 25%.
    return max(dictionary, key=dictionary.get)

foo = Solution();
print(foo.findSpecialInteger([1,1]));
