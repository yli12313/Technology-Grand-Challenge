class Solution(object):
    def productExceptSelf(self, nums):
        # Topic: Hash table.
        # This is not a hash table problem. This is an array and prefix sum problem.

        # Approach 1:
        # - Have to create an array of the same length as nums to return as the answer.
        # - As you go through the array, delete each entry and save the value.
        # - Calculate the product and append it to the answer.
        # - Re-add the element deleted back into the array.

        # NOTE: Solution works! But it's not optimal and reaches 'Time Limit Exceeded'. 
        # This is where we have to look at the answers for a better solution.

        # answer = []

        # for i in range(len(nums)):
        #     current_value = nums[i]
        #     del nums[i]
        #     found = reduce((lambda x,y: x*y), nums)
        #     answer.append(found)

        #     nums.insert(i, current_value)
        
        # return answer

        # Approach 2:
        # This was the approach that I did two years ago that I don't think is the most optimized
        # solution in terms of time and space complexity.

        # TC: O(N)
        # SC: O(2*N)

        '''
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = 1
        right[n-1] = 1

        for i in range(1,n):
            # To update the left ith value, you have to modify the left i-1 and nums i-1 values.
            left[i] = left[i-1]*nums[i-1]

            # To update the right n-i-1 value where n is the nums length, you have to modify the right 
            # n-i value and the nums n-i value.
            right[n-i-1] = right[n-i]*nums[n-i]
        
        for i in range(n):
            left[i] = left[i]*right[i]
        
        return left
        '''

        # Approach 3:
        # This is the NeetCode approach. Not exactly sure how this algorithm works exactly, but let me
        # try to explain it. 

        # TC: O(N)
        # SC: O(1)

        # Create an answer array that will hold both the prefixes and the post fixes. 
        n = len(nums)
        answer = [1]*n

        # Set the prefix to 1.
        prefix = 1

        # Compute prefix values.
        for i in range(n):
            # Update the answer with the prefix.
            answer[i] = prefix

            # Update the prefix
            prefix *= nums[i]
        
        # Set the postfix to 1.
        postfix = 1

        # Compute postfix values.
        for i in range(n-1, -1, -1):
            # Tricky you have to include an multiplication operation '*' right here!
            # Update the answer with the postfix.
            answer[i] *= postfix

            # Update the postfix.
            postfix *= nums[i]
        
        return answer