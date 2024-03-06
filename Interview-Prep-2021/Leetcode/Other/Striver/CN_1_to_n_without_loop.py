# LINK: https://www.codingninjas.com/studio/problems/print-1-to-n_628290?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from typing import List

def recursive(container, n):
    if n <= 0:
        return
    
    container.append(n)

    recursive(container,n-1)

def printNos(x: int) -> List[int]: 
    answer = []

    recursive(answer, x)
    answer.reverse()

    return answer
