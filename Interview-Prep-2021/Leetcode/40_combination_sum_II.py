# LINK: https://leetcode.com/problems/combination-sum-ii/

class Solution(object):
    def combinationSum2(self, candidates, target):
        # Constraints:
        # - 1 <= candidates.length <= 100
        # - 1 <= condidates[i] <= 50
        # - 1 <= target <= 30

        # Topic: Hash table.
        # This is an array and backtracking problem instead!

        # Approach 1:
        # - Loop through the array. 
        # - If the number is greater than the target, then skip it.
        # - What is the trick? This problem is similar to two sums.
        # - I don't know the trick; it may be time to look at a ChatGPT answer!

        # Example (Trying to solve a smaller problem instead):
        # [1,2,7], target = 8
        # - All 1 number combinations: [1], [2], [7]
        # - All 2 number combinations: [1,2], [1,7], [2,7]
        # - All 3 number combinations: [1,2,7]

        # Approach 2 (From ChatGPT and Neetcode):
        # - Define an inner function that will do the backtracking. The inputs to this function
        # are (start, target, path) -> (0, target, []).
        # - If target becomes 0, then you append the path to result, which is a variable that
        # you define outside of the backtracking() function. 'return' from the function.
        # - Define a for loop that goes from the start to the length of candidates.
        # - If 'i>start' and 'candidates[i] == candidates[i-1]', you found a duplicate and you
        # continue onto the next value.
        # - If 'candidates[i] > target', you break.
        # - Append candidates[i] -> path.
        # - Call 'backtrack(i+1, target-cadidates[i], path)'
        # - TRICK: This is the cleanup step. After you've explored the path, you need to pop()
        # the last value from the path. This is because you append candidates[i] to the path
        # and then call backtrack. 

        # (Outside the backtrack function):
        # - Sort the candidates.
        # - Define the results.
        # - Call the backtrack function.
        # - Return the results.

        # TC: O(2^N) -> Worst case scenario would explore all possible combinations.
        # SC: O(N)

        def backtrack(start, target, path):
            if target == 0:
                # TRICKY: To make a copy of the list path, you have to slice the list using '[:]'.
                result.append(path[:])
                return
            
            n = len(candidates)
            for i in range(start, n):
                # 1) CHECK 1: Check for duplicates.
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                # 2) CHECK 2: Check if candidates[i] > target.
                if candidates[i] > target:
                    break

                # 3) Append 'candidates[i]' to the path.
                path.append(candidates[i])

                # 4) TRICKY: Call backtrack(), but do it with start -> 'i+1'.
                backtrack(i+1, target-candidates[i], path)

                # 5) Path has to call pop().
                path.pop()

        # 6) TRICKY: Call candidates.sort().
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
