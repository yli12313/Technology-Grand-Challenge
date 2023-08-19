# LINK: https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN/solutions

# NOTE: 
# - When you want to chop off a digit from a number, you divide by 10.
# - When you want to retain the digit that would be chopped off, you modulo by 10.

def solution(year):
    # Approach 1:
    last_two = year % 100
    century = year / 100

    if last_two >= 1 and last_two <= 99:
        return century + 1
    
    return century
