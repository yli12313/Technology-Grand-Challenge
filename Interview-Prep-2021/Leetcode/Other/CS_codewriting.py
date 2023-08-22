def solution(a):
    # Constraints:
    # 1 <= a.length <= 10^3
    # 1 <= a[i] < 100
    
    # Topic: Hash Table.
    
    # Approach 1 (Passed 21/22 Tests):
    # - How to check if a number has one or two digits?
    # - Simple, check if it's between 1 <= x <= 9.
    
    # - Go through each number in 'a' and check if it has one or two
    # digits. 
    #     - If it has one digit, add it to the hash_table where 
    #     k,v -> digit,count. Continue to the next number.
    #     - If it has two digits, first parse the number such that you
    #     separate the first and second digits. 
    # - Sort the 'hash_table.items()' which are tuple values by 'x[1]'.
    # Do it in a way where 'reverse=True'.
    # - Loop through the list of tuples such that if 'count >= max', 
    # update 'max' and append to the 'answer' list.
    # - Return the 'answer'.

    # NOTE: I'm proud my myself for not quitting! I kept trying and I 
    # learned a lot about the Code Signal platform!
    
    """
    answer = []
    hash_table = {}
    max = 0
    
    for n in a:
        if 1 <= n <= 9:
            hash_table[n] = 1 + hash_table.get(n, 0)
            continue
        
        # This will grab the first digit if it's a two digit number.
        first = int(n % 10)
        # This will grab the second digit if it's a two digit number.
        second = int(n / 10)
        
        hash_table[first] = 1 + hash_table.get(first, 0)
        hash_table[second] = 1 + hash_table.get(second, 0)
        
    hash_table = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)

    for tup in hash_table:
        digit = tup[0]
        count = tup[1]

        if count >= max:
            max = count 
            answer.append(digit)
                
    return answer
    """

    # Approach 2:
    # - Much simpler implementation! The key is to join all the numbers 
    # together into a single string.
    
    a = "".join(str(x) for x in a)
    d = {}
    max = 0

    # Create the dictionary of digits and their counts.
    for n in a:
        d[n] = 1 + d.get(n,0)
    
    # Find the max count. Interesting: When you loop through the
    # keys of a dictionary, you just need to put the dictionary's name!
    for i in d:
        if d[i] > max:
            max = d[i]
    
    # 1) Construct the answer list. Do it with the construct:
    # [exp for exp if exp]

    # 2) You are looking to return the keys (where they are strings
    # that you convert to ints) where the frequency (v) is equal to
    # the max!
    l = [int(k) for k,v in d.items() if v == max]

    # Sort and return the answer.
    return sorted(l)

answer = solution([25, 2, 3, 57, 38, 41])
print(answer)
