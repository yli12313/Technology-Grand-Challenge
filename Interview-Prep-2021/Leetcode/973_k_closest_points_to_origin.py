# Link: https://leetcode.com/problems/k-closest-points-to-origin/

import math
import heapq

class Solution(object):
    def kClosest(self, points, k):
        h = []
        answer = []

        for point in points:
            distance = math.sqrt(((point[0]-0) ** 2 + (point[1] - 0) **2))

            heapq.heappush(h, (distance, point))

        while k > 0:
            temp = heapq.heappop(h)
            answer.append(temp[1])

            k -= 1

        return answer

foo = Solution();
print(foo.kClosest([[3,3],[5,-1],[-2,4]], 2));
