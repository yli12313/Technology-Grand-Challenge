# Link: https://leetcode.com/problems/k-closest-points-to-origin/

# Import the libraries that are needed.
import math
import heapq

class Solution(object):
    def kClosest(self, points, k):
        h = []
        answer = []
        
        # 1) Calculate the distance from the origin.
        # 2) Push the distance and the point into a Min-Heap.
        # 3) Pop the k-top entries from the Min-Heap, and extract the coordinates. 
        for point in points:
            # Calculate the distance from (0, 0).
            distance = math.sqrt(((point[0]-0) ** 2 + (point[1] - 0) **2))
            
            # Push the result to the Min-Heap.
            heapq.heappush(h, (distance, point))
        
        # Pop the k-top entries in the heap and then append it to an answer array.
        while k > 0:
            temp = heapq.heappop(h)
            answer.append(temp[1])

            k -= 1
        
        # Return the answer array.
        return answer

foo = Solution();
print(foo.kClosest([[3,3],[5,-1],[-2,4]], 2));
