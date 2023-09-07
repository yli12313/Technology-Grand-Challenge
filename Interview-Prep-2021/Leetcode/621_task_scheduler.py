# LINK: https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
# TRICK: If you want to use heaps, 'import heapq'.
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        # Constraints
        # - 1 <= task.length <= 10^4
        # - tasks[i] is upper-case English letter.
        # - The integer n is in the range[0, 100].

        # Topic: Dynamic Programming
        # This is an Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting problem.

        # Approach 1 (Wrong approach with bad intuition):
        # - Tried to derive a math formula, but this task requires advanced data structures.
        # - Using heaps and queues is the better way.

        # Approach 2 (NeetCode):
        # - Define a max heap that will hold the count of all the tasks, grouped by task types.
        # - Define a time variable that will serve as the answer.
        # - Define a priority queue that will hold: [count, time].
        # - While the maxHeap and the priority queue are not empty, do the following:
        # - 1) Update the maxHeap and see if any tasks are executed. If so, move the task into the
        # priority queue.
        # - 2) Update the priority queue when a task as reached the end of it's cool down period, and if
        # there are still tasks of the same type, move the task counts back to the maxHeap. 
        # - Return the time, which is the answer.

        # Working with the MaxHeap is O(log(N)) -> O(log(26)).
        # TC: O(N*M)
        # SC: O(N): The max heap and queue can store at most 'N' values.

        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        # TRICK: The syntax is always: 'heapq.heapify(collection)'.
        heapq.heapify(max_heap)

        time = 0
        queue = deque()

        # TRICK: Let the while() loop run 'while max_heap or queue:'.
        # TRICK: It's 'max_heap' or 'queue'!
        while max_heap or queue:
            time += 1

            if max_heap:
                # TRICK: The syntax here is '1+heapq.heappop(max_heap)'.
                cnt = 1+heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time+n])
            
            if queue and queue[0][1] == time:
                # TRICK: The operation on the queue is: 'queue.popleft()'.
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time

foo = Solution();
print(foo.leastInterval(["A","A","A","B","B","B"], 2));
