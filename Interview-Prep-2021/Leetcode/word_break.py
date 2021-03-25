class Solution(object):
  def wordBreak(self, s, wordDict):
    ## Dynamic Programming ##

    wordDict = set(wordDict)
    dp = [False]*(len(s)+1)
    dp[0] = True

    for i in range(1, len(s)+1):
    	for j in range(i):
    		if dp[j] and s[j:i] in wordDict:
    			dp[i]=True
    			break 

    return dp[len(s)]

    ## Breadth-First-Search ##

    ##########################
    
    ## Did not investigate further ##

    # word_set = set(wordDict)
    # q = deque()
    # visited = set()

    # q.append(0)
    # while q:
    #   start = q.popleft()
    #   if start in visited:
    #     continue
    #   for end in range(start + 1, len(s) + 1):
    #     if s[start:end] in word_set:
    #       q.append(end)
    #       if end == len(s):
    #         return True
    #     visited.add(start)
    # return False

foo = Solution();
print(foo.wordBreak("applepenapple", ["apple","pen"]));