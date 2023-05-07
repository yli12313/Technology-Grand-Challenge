class Solution(object):
  def checkIfExist(self, arr):
    # Approach 1 (Trying it out):
    # [10,2,5,3] --> [2,3,5,10] # Sort the array
    # Then you loop through the array and add to a dictionary the following:
    #   - { 2*value : i }, where i is the index of the array

    # Then you loop through the array again:
    #   - arr[j] is in the holder.keys() {Meaning 2*arr[j] exists in the array}
    #   - Check that j is NOT EQUAL TO holder[arr[j]] {Meaning j is NOT EQUAL TO i}
    #   - Return True

    # You return True by default.

    # KEY POINT: Didn't know that you needed to solve this problem with two
    # for() loops and not just one for() loop!

    holder = {}
    arr = sorted(arr) # Default of sorted() is: ASCENDING order

    for i in range(len(arr)):
      double = 2*arr[i]
      if double in arr:
        holder[double] = i
    
    for j in range(len(arr)):
      if arr[j] in holder.keys():
        if j != holder[arr[j]]:
          return True
        
    return False

foo = Solution();
print(foo.checkIfExist([3,1,7,11]));