class Solution(object):
  def longestValidParentheses(self, s):
    stk = []
    mx = 0
    stk.append(-1)

    for i in range(len(s)):
      if s[i] == '(':
        stk.append(i)
      else:
        stk.pop()
        if (len(stk)==0):
          stk.append(i)
        else:
          length = i-stk[len(stk)-1]
          mx = max(mx, length)

    return mx

foo = Solution();
print(foo.longestValidParentheses(""));