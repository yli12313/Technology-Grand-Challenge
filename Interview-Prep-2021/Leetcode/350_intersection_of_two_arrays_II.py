class Solution(object):
  def intersect(self, nums1, nums2):
    # Approach 1:
    # First you sort the arrays:
    #   - [4,9,5] --> [4,5,9]
    #   - [9,4,9,8,4] --> [4,4,8,9,9]   
    # Find the smaller of the two arrays.
    # Loop through the smaller array checking if the value is in the larger array.
    # If so, keep the value.
    # If not, delete the value.
    # return the smaller array.

    # Completely wrong approach! Don't mess with an algorithm that tries to detect
    # the bigger/smaller array. Just a bad idea. # Use a dictionary instead.

    # Approach 2:
    # Make a dictionary of the first array:
    #   - {1:1, 2:1}
    # Go through second array and every time you see a new number, check if it's in
    # the dictionaries keys and if it's value is > 0. If so, subtract the value by
    # 1 and add the value to the answer array.
    #   - value --> 1; {1:0, 2:1}; answer = [1]
    #   - value --> 1; {1:0, 2:1}; RETURN answer = [1]

    holder = {}
    answer = []

    for number in nums1:
      if number in holder.keys():
        holder[number] += 1
      else:
        holder[number] = 1

    for number in nums2:
      if number in holder.keys() and holder[number] > 0:
        holder[number] -= 1
        answer.append(number)

    return answer
      
foo = Solution();
print(foo.intersect([1,2], [1,1]));
