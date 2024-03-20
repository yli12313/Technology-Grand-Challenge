# LINK: https://www.codingninjas.com/studio/problems/n-to-1-without-loop_8357243?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# TRICK:
# Keep practicing and keep going!

# TC: O(N)
# SC: O(N)

from typing import List

def printNos(x: int, result = None) -> List[int]:
    if result == None:
        result = []
    
    if x <= 0:
        return result
    
    result.append(x)
    return printNos(x-1, result)
