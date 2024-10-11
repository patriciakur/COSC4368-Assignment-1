from collections import deque

# Graph Class
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def get_graph(self):
        return self.graph

# BFS Approach
def bfs(graph, start,goal):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        (vertex, path) = queue.popleft()
        
        if vertex == goal:
            return path

        for child in graph.get(vertex, []):
            if child not in visited:
                visited.add(child)
                queue.append((child, path + [child]))
    return None

# DFS Approach
def dfs(graph, start, goal):
    visited = set()
    visited.add(start)
    
    return getChildren(graph, start, [start], visited, goal)

def getChildren(graph, parent, currentPath, visited, goal):
    children = graph.get(parent, [])
    if children:
        for child in children:
            if child not in visited:
                visited.add(child)
                if child == goal:
                    return currentPath + [child]
                result = getChildren(graph, child, currentPath + [child], visited, goal)
                if result is not None:
                    return result
    return None

    
# Generate the graph for task 1
g=Graph()
g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(0, 7)
g.add_edge(0, 3)
g.add_edge(3, 0)
g.add_edge(1, 4)
g.add_edge(7, 4)
g.add_edge(7, 5)
g.add_edge(3, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)


# Run the BFS and DFS algorithms
print("Graph:", g.get_graph())
print("-----------------")

print("BFS Approach")
print("Most Efficient Route to Node 7:", bfs(g.get_graph(), 0, 7))
print("Most Efficient Route to Node 5:", bfs(g.get_graph(), 0, 5))
print("Most Efficient Route to Node 6:", bfs(g.get_graph(), 0, 6))

print("-----------------")
print("DFS Approach")
print("Most Efficient Route to Node 7:", dfs(g.get_graph(), 0, 7))
print("Most Efficient Route to Node 5:", dfs(g.get_graph(), 0, 5))
print("Most Efficient Route to Node 6:", dfs(g.get_graph(), 0, 6))


        