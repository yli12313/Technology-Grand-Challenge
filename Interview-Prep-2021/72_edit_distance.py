# Link: https://leetcode.com/problems/edit-distance/

class Solution(object):
    def minDistance(self, word1, word2):
        # To set up the dp array, the characters of word1 will represent the rows and
        # the characters of word2 will represent the columns.

        # Get the rows and columns, including an extra row or column for the empty string!
        rows = len(word1)+1
        columns = len(word2)+1

        # Generating a 2-D array in Python: [[0] * X for _ in range(Y)]
        dp = [[0] * columns for _ in range(rows)]

        # What you can learn: to optimize the algorithm, it's important which word you put as the row and which word
        # you put as the column of the dp array. Selecting one word vs. the other will help optimize the algorithm.

        # For the first row, initialize the dp array. Ironically, you have to use columns to traverse the first row.
        # Use Case: you have "" for word1 and and a non-empty string for word 2.
        for i in range(columns):
          dp[0][i] = i

        # For the first column, initialize the dp array. Ironically, you have to use rows to traverse the first column.
        # Use case: yo have a non-empty string for word1 and "" for word 2.
        for j in range(rows):
          dp[j][0] = j

        # What can you learn: use the principle of Symmetry.

        # Loop through the dp array to fill it out starting at 1 for the rows and columns (which represents the first character)
        # of each word.
        for i in range(1, rows):
          for j in range(1, columns):
            # Have to look back 1 character for both words in order to make edit distance comparisions UP TO word1[i-1] and word2[j-1]
            # in order to calculate the edit distance of word1[i] and word2[j].
            c1 = word1[i-1]
            c2 = word2[j-1]

            # If the edit distance up to the previous character in both words is the same, keep the same edit distance for the
            # new characters encountered at word1[i] and word2[j].
            if c1 == c2:
              dp[i][j] = dp[i-1][j-1]
            else:
              # Calculate the edit distance of: 1+ the minimum of the replace and addition operations. You don't care about the
              # delete operation because an addition in one word IS a deletion on the other word.
              dp[i][j] = 1+min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j]))

        # Return the answer.
        return dp[rows-1][columns-1]

foo = Solution();
print(foo.minDistance("horse", "ros"));
