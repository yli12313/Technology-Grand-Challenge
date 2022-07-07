#Link: https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        # Get the length of the temperatures array.
        N = len(temperatures)

        # Define the monotonic stack.
        stack = []

        # Define the answer array that is of length N.
        answer = [0]*(N)
        
        # Loop through the temperature array.
        for i in range(N):
            # Get the current temperature if as the loop goes through the 
            # temperatures array.
            current = temperatures[i]

            # While the stack is NOT empty and the temperature that corresponds
            # to the index at the top of the stack is less than the current 
            # temperature (i.e. we encountered a bigger temperature), do a three
            # part process. 1) Pop from the top of the stack, 2) calculate the 
            # distance from the current temperature to the previous lower temperature
            # in terms of days, and 3) store the answer. 
            while stack and temperatures[stack[-1]] < current:
                prevTemp = stack.pop()
                answer[prevTemp] = i-prevTemp

            # Keep appending the index if the temperatures are less than the current
            # temperature. 
            stack.append(i)

        # Return the answer.
        return answer;       

foo = Solution();
print(foo.dailyTemperatures([30,60,90]));
