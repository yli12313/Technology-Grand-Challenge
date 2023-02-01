## This is the graph that's given as part of Problem 2. ##
graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['G', 'H'],
  'E' : ['I'],
  'F' : ['J'],
  'G' : ['K', 'L'],
  'H' : ['M'],
  'I' : [],
  'J' : ['N', 'O'],
  'K' : ['P', 'Q'],
  'L' : [],
  'M' : ['R', 'S'],
  'N' : [],
  'O' : [],
  'P' : [],
  'Q' : ['T'],
  'R' : [],
  'S' : [],
  'T' : ['U', 'V'],
  'U' : [],
  'V' : [],
}

## Depth-First Search (DFS) ##
# This resource is good: https://favtutor.com/blogs/depth-first-search-python

""" The DFS algorithm follows as:
1. We will start by putting any one of the graph's vertex on top of the stack.
2. After that, take the top item off the stack and add it to the visited list of the vertex.
3. Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.
4. Lastly, keep repeating steps 2 and 3 until the stack is empty.
"""

## This is the iterative implementation of DFS. ##
visited=set()
stack=[]

def dfs(visited, graph, node):
  stack.append(node)

  while stack:
    current=stack.pop()
    if current not in visited:
      print(current, end=" ")
      visited.add(current)

      if len(graph[current])==2:
        stack.append(graph[current][1])
        stack.append(graph[current][0])
      elif len(graph[current])==1:
        stack.append(graph[current][0])

## This is the recursive implementation of DFS. ##
# visited=set()

# def dfs(visited, graph, node):
#   if node not in visited:
#     print(node, end=" ")
#     visited.add(node)
#     for neighbor in graph[node]:
#       dfs(visited, graph, neighbor)  

## Executing the code. ##
dfs(visited, graph, 'A')
