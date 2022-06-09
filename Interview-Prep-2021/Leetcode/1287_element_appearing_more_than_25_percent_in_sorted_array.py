class Solution(object):
  def findSpecialInteger(self, arr):
    if not arr:
      return None

    dictionary = {}

    for val in arr:
      if val in dictionary.keys():
        dictionary[val] += 1
      else:
        dictionary[val] = 1
    
    return max(dictionary, key=dictionary.get)

foo = Solution();
print(foo.findSpecialInteger([1,1]));