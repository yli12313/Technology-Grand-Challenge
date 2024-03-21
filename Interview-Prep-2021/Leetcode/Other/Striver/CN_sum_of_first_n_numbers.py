# LINK: https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# TRICKS:
# - Pretty tricky problem where you can't solve it in Python using recursion! I learned that Python has no 
# concept of different integer types like 'long long' unlike other languages. Therefore, if you can't solve a 
# problem using recursion because the numbers are too big, try a different approach.
# - The sum of of all numbers from 1..n is: n(n+1)/2.
# - The key lesson here is to: Solve the problem! Just because a problem is categorized as a certain type
# of problem (i.e. recursion) does not mean you have to use that technique to solve the problem!

# TC: O(1)
# TC: O(1)

from typing import List

# Approach 1 (recursion; passes 49/50 of the tests):
# def sumFirstN(n: int) -> int:
#     if n <= 0:
#         return 0
#     else:
#         return n + sumFirstN(n-1)

# Approach 2 (uses a mathematical formula; passed 50/50 of the tests):
def sumFirstN(n: int) -> int:
    # TRICK: '//2' is divide and retain the integral result, where the remainder is discarded!
    return n*(n+1)//2
