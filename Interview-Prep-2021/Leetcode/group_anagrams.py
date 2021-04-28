class Solution(object):
  def groupAnagrams(self, strs):
    holder = {}

    if len(strs) == 0:
      return [[""]]

    if len(strs) == 1:
      return [[strs[0]]]

    for x in strs:
      y = "".join(sorted(x))

      if y in holder.keys():
      	holder[y].append(x)
      else:
      	holder[y] = [x]

    return list(holder.values())

foo = Solution();
print(foo.groupAnagrams(["eat","tea","tan","ate","nat","bat"]));