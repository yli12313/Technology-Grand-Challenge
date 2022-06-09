# Great video: https://www.youtube.com/watch?v=SfNlyzNEKyg&t=350s

class Solution(object):
  def nextGreaterElements(self, nums):
    stx = []
    output = [-1 for i in range(len(nums))]
    extended = nums * 2
    N = len(nums)

    for i in range(len(extended)):
      while len(stx) > 0 and stx[-1][0] < extended[i]:
        val, pos = stx.pop()
        output[pos] = extended[i]
      if i < N:
        stx.append((extended[i], i))

    return output

foo = Solution();
print(foo.nextGreaterElements([1,2,1]));