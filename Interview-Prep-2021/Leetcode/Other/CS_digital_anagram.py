def solution(a):
    
    # Approach 1:
    # - Define an answer variable and set it as 0. Return the answer.
    # - Define a dictionary.
    # - 1) Convert the numbers to strings, 2) sort the strings (resulting
    # in a list), and 3) join the list back into a string. 
    # - Then put the string into the dictionary (key), while counting the 
    # frequency (value).
    # - Loop through the values and apply the formula: K*(K-1)/2
    # - Return the answer.

    # NOTE: Not a hard problem at all! Just need some more practice. 

    answer = 0
    d = {}

    for n in a:
        n = "".join(sorted(str(n)))
        d[n] = 1 + d.get(n, 0)
    
    for count in d.values():
        nCr = count*(count-1) / 2
        answer += int(nCr)

    return answer
    
answer = solution([25, 35, 872, 228, 53, 278, 872])
print(answer)