# LINK: https://leetcode.com/problems/subsets/

class Solution(object):
    # TC: O(N*2^N)
    # SC: O(N*2^N)

    def subsets(self, nums):
        res = []
        cur = []

        def backtrack(start):
            res.append(cur[:])

            for i in range(start, len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    backtrack(i+1)
                    cur.pop()

        backtrack(0)
        return res
