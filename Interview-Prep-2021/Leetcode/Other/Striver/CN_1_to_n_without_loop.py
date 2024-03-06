# LINK: https://www.codingninjas.com/studio/problems/print-1-to-n_628290?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# TRICKS:
# - You should do the 1) recursive step first in the auxiliary function before 2) appending the value to the container.
# - This saves you an 'answer.reverse()' operation!

# TC: O(N)
# SC: O(N)

from typing import List

def recursive(container, n):
    if n <= 0:
        return
    
    recursive(container,n-1)
    container.append(n)

def printNos(x: int) -> List[int]: 
    answer = []

    recursive(answer, x)

    return answer
