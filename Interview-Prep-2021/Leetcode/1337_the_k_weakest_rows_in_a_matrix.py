import heapq

class Solution(object):
  def kWeakestRows(self, mat, k):
  	# (Problem solving approach 1):
    # Go through every entry of the matrix, which is a list.
    # Count the number of 1s (soldiers), and store it in a dictionary: {row X : solder_count Y}.
    # Sort by the [soldier_count].
    # But then how will you take care of the situation where: 
    #   - If you have two rows that are the exact same i, j, the weaker row is row i.

    # Problem solving approach 1 --> Wrong intuition.

    # (Problem solving approach 2):
    # Use min heap instead

    # Problem solving approach 2 --> RIGHT INTUITION.

    ## How to use a min heap ##
    """
    import heapq

    heap = []
    heapq.heapify(heap)
	
	heapq.heappush(heap, [soldier_count, i]) # Be careful what goes first! That's what the heap is sorting on.
	heapq.heappop(heap)
    """

    heap = []
    answer = []

    heapq.heapify(heap)

    i = 0
    for row in mat:
      soldier_count = len(filter(lambda x : x == 1, row))
      heapq.heappush(heap, [soldier_count, i])
      
      i += 1

    for i in range(k):
      a_row = heapq.heappop(heap)
      answer.append(a_row[1])

    return answer

mat = [
	[1,1,0,0,0],
	[1,1,1,1,0],
	[1,0,0,0,0],
	[1,1,0,0,0],
	[1,1,1,1,1]
]

k = 3

foo = Solution();
print(foo.kWeakestRows(mat, k));