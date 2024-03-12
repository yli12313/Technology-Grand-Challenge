# LINK: https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# TRICK:
# Keep going and keep practicing!

# TC: O(N)
# SC: O(1)

from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    largest = 0

    for x in arr:
        if x > largest:
            largest = x
    
    return largest
