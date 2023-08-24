def solution(a):
    
    # Approach 1:
    # - TRICK: You have to construct the array B first. This is NOT a two-pointer problem!
    # - Step 1: Construct array B.
    # - Step 2. Loop through B and see if all the elements of the array are increasing.

    n = len(a)
    count = n-1
    
    b = [0]*n

    # Make sure to debug with pdb if you can! Test it on Code Signal tomorrow
    # if you can.
    # import pdb; pdb.set_trace()

    for i in range(n):
        
        if i == 0:
            b[i] = a[i]
        # This was tricky. Set a count variable as the last element and
        # make sure to decrement it each time you find an odd number!
        elif i%2 != 0:
            b[i] = a[count]
            count -= 1
        elif i%2 == 0:
            b[i] = a[i//2]

    # Specify the range exactly right here! the cutoff is len(b)-1.
    # You want to stop 1 BEFORE the last element! The logic is:
    # 'len(b)-1'.
    for i in range(0, len(b)-1):
        # Tricky: Don't forget to include an equals than sign! The
        # array b has to be in ASCENDING ORDER!
        if b[i] >= b[i+1]:
            return False
    
    return True
     
# a = [1,3,5,6,4,2] --> True
# a = [1,4,5,6,3] --> False
answer = solution([1,3,5,6,4,2])
print(answer)