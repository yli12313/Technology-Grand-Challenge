## Breadth-First Search (BFS) ##
# This resource is good: https://favtutor.com/blogs/breadth-first-search-python

""" ## BFS pseudocode ##

create a queue Q
mark v as visited and put v into Q
while Q is non-empty
  remove the head u of Q
  mark and enqueue all (unvisited neighbors) of u
"""

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m=queue.pop(0)
    print(m, end=" ")

    for neighbor in graph[m]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)

## Executing the code. ##
bfs(visited, graph, 'A')