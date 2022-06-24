# Link: https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        rows, cols = (numRows, numRows+1)

        # This is a trick: generate 3 lists within one outer list!
        arr = [[0]*cols for _ in range(rows)]

        # Initialize the first row and and first value of Pascal's Triangle
        # as 1.
        arr[0][1] = 1

        # Get the first row of the Pascal's Triangle as a list, and then
        # append it to the final list.
        first = []
        final = []

        first.append(arr[0][1])
        final.append(first)

        # Looping through the rest of the rows that's not the first one.
        for i in range(1, rows):

            # Define the list for each row of the Pascal's Triangle that's not
            # the first.
            inner = []

            # Loop through the column's of the array, up to i+1.

            # Row 1: Columns: 1, 2.
            # Row 2: Columns: 1, 2, 3
            # Row 3: Columns: 1, 2, 3, 4
            # Row 4: Columns: 1, 2, 3, 4, 5

            # Esentially this is the number elements in each row of the
            # Pascal's Triangle.
            for j in range(1, i+2):
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
                inner.append(arr[i][j])

            # Append the row (inner list) to the final list once complete.
            final.append(inner)

        # Return the final list.
        return final
            
foo = Solution();
print(foo.generate(5));
