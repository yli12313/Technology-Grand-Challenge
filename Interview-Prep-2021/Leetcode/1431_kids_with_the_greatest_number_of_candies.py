# LINK: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
  def kidsWithCandies(self, candies, extraCandies):
    # Topic: Array

    # TC: O(N)
    # SC: O(N)

    """
    # Approach 1 (My solution I designed and it worked!):
    # You want to add the extra candies to each kid's candies and see if that's
    # the max candies in the whole array. 

    # How to find the max in the array fast? Use max().


    # Define answer array.
    answer = []

    # Go through the list of candies.
    for i in range(len(candies)):
      # Calculate how many candies the current kid has with extras.
      kid_with_extras = candies[i]+extraCandies

      # Updating the candies array with the extra candies for the current kid.
      candies[i] = candies[i] + extraCandies

      # Finding the max number of candies in the whole array.
      max_candies = max(candies)

      # If the max candies in the whole array is equal to what the current kid has
      # add 'True'. Else add 'False'.
      if kid_with_extras == max_candies:
        answer.append(True)
      else:
      	answer.append(False)
      
      # Subtract the extra candies from the current kid.
      candies[i] = candies[i] - extraCandies

    # Return answer
    return answer
    """

    ####

    # Approach 2 (This is the ChatGPT solution with simpler code):
    # Find the max in the candies array. Loop through all the candies
    # and see if it's greater than or equal to the max (true) or if it's
    # less than the max (false).

    max_candies = max(candies)
    answer = []

    for candy in candies:
      kid_with_extras = candy+extraCandies

      if kid_with_extras >= max_candies:
      	answer.append(True)
      else:
      	answer.append(False)

    return answer

foo = Solution();
print(foo.kidsWithCandies([2,3,5,1,3], 3));
