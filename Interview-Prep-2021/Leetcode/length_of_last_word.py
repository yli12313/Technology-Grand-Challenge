class Solution(object):
  def lengthOfLastWord(self, s):
    if s == ' ':
      return 0

    s = s.strip()
    l = s.split(" ")  	

    return len(l[len(l)-1])

foo = Solution();
print(foo.lengthOfLastWord(" "));