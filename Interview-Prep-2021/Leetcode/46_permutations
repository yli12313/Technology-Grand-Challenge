class Solution(object):
    def backtrack(self, container, temp_container, nums):
        if len(temp_container) == len(nums):
            container.append(temp_container[:])
            return
        
        for i in range(len(nums)):
            v = nums[i]

            if v in temp_container:
                continue

            temp_container.append(v)
            self.backtrack(container, temp_container, nums)
            temp_container.pop()
            
    def permute(self, nums):
        # Constraints:
        # - 1 <= nums.length <= 6
        # - -10 <= nums[i] <= 10
        # - All the integers of nums are unique.

        # Topic: Backtracking

        # Approach 1:
        # Auxiliary backtrack() function:
        # - Check to see if the length of the temporary container is equal
        # to the length of nums.
        # - If so, then  append the temporary container to the container. 
        # - Do a for() loop from 0..len(nums) indexed by i.
        # - If the current value indexed by i is in the temporary container,
        # - then continue.
        # - Add the corrent value indexed by i to the temporary container.
        # - Call the backtrack() function recursively.
        # - Pop a value from the temporary container to backtrack and explore 
        # other permutations.

        # Main permute() function:
        # - Set up the skeleton.
        # - Define a res list and return it.
        # - Between the definition and the return statement, call backtrack.
        #   - Parameter1: res variable
        #   - Parameter2: empty list
        #   - Parameter3: nums variable

        # TC: O(N!); TC is determined by the number of permutations which is N!.
        # SC: O(N); SC is determined by the depth of the recursion stack which is
        # at most N.

        res = []
        self.backtrack(res, [], nums)
        return res

foo = Solution()
print(foo.permute([1,2,3]))
