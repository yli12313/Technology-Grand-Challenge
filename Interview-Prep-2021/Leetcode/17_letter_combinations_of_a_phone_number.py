# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Make sure to use double space and not tab! ##

class Solution(object):
  def letterCombinations(self, digits):
    # create answer list
    answer = []

    # Check that the length is 0; return it if so
    if (len(digits)==0):
      return answer

    # Append an empty string to start off the sequence
    answer.append("")

    # Create map of numbers to letters
    digitsMap = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # Loop through digits
    for i in range(len(digits)):
      # Extract each individual digit
      digit = digits[i]

      # While the first string in the answer is equal to index of the digit, pop
      # string from answer list; link the length of the answer to the index of digits.
      # Genius!
      while len(answer[0]) == i:
        current = answer.pop(0)

        # Append the letters from the new digit
        for letter in digitsMap[int(digit)]:
          answer.append(current+letter)

    return answer

foo = Solution();
print(foo.letterCombinations("2"));