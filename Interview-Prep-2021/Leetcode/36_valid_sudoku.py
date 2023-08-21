# LINK: https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        # Topic: 2-D Array.
        # You are correct in that this is an Array, Hash Table and Matrix problem.

        # Approach 1:
        # - The brute-force approach would be to... I honestly don't even know how to do this problem
        # with the brute-force method. 

        # Approach 2: 
        # - Neetcode approach. It's a very simple algorithm! I'm going to watch the video again and type 
        # - and document the code. Just really have to understand how the (r//3, c//3) tricks works!

        # NOTE: The (r//3, c//3) trick is very simple. Right now in a normal sudoku board, the rows/columns 
        # range is the following: 0,1,2,3,4,5,6,7,8.

        # After doing (r//3, c//3), the rows/columns
        # is now the following: 0,1,2.

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        n = len(board)

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r]) or \
                   (board[r][c] in cols[c]) or \
                   (board[r][c] in square[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        
        return True