# LINK: https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
def fibonacci(n):
    if n < 1:
        return None

    if n == 1:
        return 1
    
    if n == 2: 
        return 1

    dp = [0]*n
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n-1]

n = int(input())
print(fibonacci(n))
