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

            # This is a monotonically decreasing stack where we store the index values!

            ## Example ##:
            # temperatures: [30, 20, 10, 60]
            # Same result if temperatures was: [60, 50, 40, 70]

            # stack: []
            # answer: [0, 0, 0, 0]

            # -------

            # stack: [0]

            # -------

            # stack: [0, 1]

            # -------

            # stack: [0, 1, 2]

            # -------

            ## Encountered a bigger element! ##

            # 60 - 10 (temperatures) --> 3 - 2 = 1
            # 60 - 20 (temperatures) --> 3 - 1 = 2
            # 60 - 30 (temperatures) --> 3 - 0 = 3

            # answer = [3, 2, 1, 0]
            # stack = [3]

            # -------

            # Return the answer! The loop ends after i = 3.

            while stack and temperatures[stack[-1]] < current:
                prevTemp = stack.pop()
                answer[prevTemp] = i-prevTemp

            # Keep appending the index if the temperatures are less than the current
            # temperature. 
            stack.append(i)

        # Return the answer.
        return answer;       

foo = Solution();
print(foo.dailyTemperatures([60, 50, 40, 70]));
