# LINK: https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # array 'a' of 'n' unique non-negative integers
    # find second largest and second smallest element from the array

    # Approach 1 (Non-Optimal Solution):

    # TC: O(N*Log(N)), don't forget that sorting is O(N*Log(N))!
    # SC: O(1)

    # if n <= 1:
    #     return None
    
    # a.sort()
    # return [a[-2], a[1]]

    # Approach 2 (Optimized Solution):
    # - This is the right code, but it only passes 10/11 tests. I think there's something wrong 
    # with the Coding Ninjas platform.

    # TC: O(N)
    # SC: O(1)

    if n < 2:
        return None

    # TRICK: This is how you set multiple variables to have the same value.
    largest = sec_largest = smallest = sec_smallest = 0
    
    if a[0] > a[1]:
        largest = sec_smallest = a[0]
        smallest = sec_largest = a[1]
        
    else:
        smallest = sec_largest = a[0]
        largest = sec_smallest = a[1]
    
    for i in range(2,n):
        cur = a[i]

        if cur > largest:
            sec_largest = largest
            largest = cur
        elif cur > sec_largest:
            sec_largest = cur

    # TRICK: When you have two for() loops, you can use the same variable to interate
    # over them!
    for i in range(2,n):
        cur = a[i]

        if cur < smallest:
            sec_smallest = smallest
            smallest = cur
        elif cur < sec_smallest:
            sec_smallest = cur
    
    return [sec_largest, sec_smallest]
