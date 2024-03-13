# LINK: https://www.codingninjas.com/studio/problems/-print-n-times_8380707?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# TRICK:
# Keep going and keep practicing!

# TC: O(N)
# SC: O(1)

from  typing import *

def printNtimes(n: int) -> List[str]:
    # TRICK: For the base case, you have to return the empty list '[]'
    if n == 0:
        return []
    
    print("Coding Ninjas", end = " ")

    # TRICK: For the recursive step, you have to do 'return printNtimes(n-1)'.
    return printNtimes(n-1)
