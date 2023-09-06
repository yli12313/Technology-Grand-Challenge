# LINK: https://leetcode.com/problems/furthest-point-from-origin/

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        # Constraints
        # - 1 <= moves.length == n <= 50
        # - moves consists only of characters 'L', 'R', and '_'.

        #: Topic: String
        # This is an Array, Counting problem.

        # Approach 1 (It works!):
        # - Go through the string and count the frequency if characters 'L' and 'R':
        # {L:2, R:2: _:3} -> 2-2+3 = 3
        # {L:2, R:1, _:4} -> 2-1+4 = 5
        # - Define ans variable.
        # - Define l, r, and underscore variables.
        # - Go through the array and count the frequency of everything.
        # - Determine the max between l and r.
        # - Apply the formula: max - min + count of _.

        # TC: O(N)
        # SC: O(1)

        """
        ans = 0
        l,r,underscore = 0,0,0

        for m in moves:
            if m == "L":
                l += 1
            elif m == "R":
                r += 1
            else:
                underscore += 1
        
        if l>r:
            ans = l-r+underscore
        elif l<r:
            ans = r-l+underscore
        else:
            ans = underscore

        return ans
        """

        # Approach 2 (Simplifying the approach, but this approach has a far worse
        # time and space complexity):

        """
        count,blank = 0,0

        for m in moves:
            if m == "L":
                count -= 1
            elif m == "R":
                count += 1
            else:
                blank += 1

        return abs(count) + blank
        """

        # Approach 3 (Same as Approach 1, but without an 'ans' variable):
        # {L:2, R:2, _:3} -> 3
        # {L:2, R:1, _:4} -> 2-1+4 -> 5
        # {_:7} -> 7

        # - Define left, right and underscore variables.
        # - Loop through the moves.
        # - For each move m, figure out if it's a left, right, or underscore and update that 
        # variable.
        # - If left < right, then return right - left + underscore.
        # - Else if left > right, left - right + underscore.
        # - Return underscore.

        # TC: O(N)
        # SC: O(1)

        left,right,underscore = 0,0,0

        for m in moves:
            if m == "L":
                left += 1
            elif m == "R":
                right += 1
            else:
                underscore += 1
        
        if left < right:
            return right-left+underscore
        elif left > right:
            return left-right+underscore
        
        return underscore
