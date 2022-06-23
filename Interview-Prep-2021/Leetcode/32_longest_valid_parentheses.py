# Link: https://leetcode.com/problems/longest-valid-parentheses/

# This is a monotonically increasing stack! The index's are always increasing :)

class Solution(object):
  def longestValidParentheses(self, s):
    # 1) Define a stack.
    # 2) Defind the longest valid parentheses as 0.
    # 3) Append a -1 to the stack.
    stk = []
    mx = 0
    stk.append(-1)

    # Loop through the string.
    for i in range(len(s)):
      # if you encounter a '(', then append the index of the '(' to the stack.
      if s[i] == '(':
        stk.append(i)
      else:
  
        # Else pop the index from the top of the stack.
        stk.pop()
        
        # If the monotonic increasing stack is empty, append the index of the new
        # ')' value as a bookmark. 
        if (len(stk)==0):
          stk.append(i)
        else:
          # If you encounter ')' and the stack is not empty, then calculate the length
          # and compare it to max. If it's bigger than max, then update the max value.
          length = i-stk[len(stk)-1]
          mx = max(mx, length)
    
    # Return max.
    return mx

foo = Solution();
print(foo.longestValidParentheses(""));
