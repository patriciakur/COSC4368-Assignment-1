import random
from collections import deque
import math

# Graph Class
class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

    def get_neighbors(self, node):
        return self.edges[node]

    def get_edge_weight(self, from_node, to_node):
        return self.weights.get((from_node, to_node))
    
    def get_graph(self):
        return self.weights
    
# A* Search Algorithm
def aSearch(graph, start, goal):
    heuristicChart = {}
    for node in graph.edges:
        heuristicChart[node] = euclidean_heuristic(node, goal)
    
    openList = [(start, heuristicChart[start], [(0,0)], 0)]
    closedList = []
    current = (start, heuristicChart[start], [(0,0)], 0)
    while current[0] != goal:
        current = min(openList, key= lambda openList: openList[1])
        openList.remove(current)
        closedList.append(current[0])
        for neighbor in graph.get_neighbors(current[0]):
            if neighbor not in closedList:
                openList.append((neighbor, current[1] + graph.get_edge_weight(current[0], neighbor) + heuristicChart[neighbor], current[2] + [neighbor], current[3] + graph.get_edge_weight(current[0], neighbor)))
    
    print("Optimal Path to Customer's Home:", current[2])
    print("Total Travel Time along the Path:", current[3], "minutes") 
    travelTimes.append(current[3])
    return

def euclidean_heuristic(node, goal):
    return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)


travelTimes = []

# Create the graphs for task 2
example=Graph()
example.add_edge((0,0), (0,1), 2)
example.add_edge((0,0), (1,0), 4)
example.add_edge((0,1), (0,2), 3)
example.add_edge((0,1), (1,1), 3)
example.add_edge((0,2), (1,2), 7)
example.add_edge((1,0), (1,1), 1)
example.add_edge((1,0), (2,0), 3)
example.add_edge((2,0), (2,1), 4)
example.add_edge((1,1), (2,1), 4)
example.add_edge((1,2), (2,2), 1)
example.add_edge((2,1), (2,2), 5)
example.add_edge((2,2), (2,3), 3)

graphA=Graph()
aEdges = [((0,0), (0,1)), ((0,0), (1,0)), ((0,1), (0,2)), ((0,1), (1,1)), ((0,2), (1,2)),
         ((1,0), (1,1)), ((1,0), (2,0)), ((2,0), (2,1)), ((1,1), (2,1)), ((1,2), (2,2)),
         ((2,1), (2,2)), ((2,2), (2,3))]
for u, v in aEdges:
    weight = random.randint(1, 10)
    graphA.add_edge(u, v, weight)
    
graphB=Graph()
bEdges = [((0,0), (0,1)), ((0,0), (1,0)), ((0,1), (0,2)), ((0,1), (1,1)), ((0,2), (1,2)),
         ((1,0), (1,1)), ((1,0), (2,0)), ((2,0), (2,1)), ((1,1), (2,1)), ((1,2), (2,2)),
         ((2,1), (2,2)), ((2,2), (2,3))]
for u, v in bEdges:
    weight = random.randint(1, 10)
    graphB.add_edge(u, v, weight)


# Run the A* Search algorithm
print("Example Graph:", example.get_graph())
print("---")
print("A* Search Algorithm on Example Graph")
aSearch(example, (0,0), (2,3))
print("-----------------")
print("Test Graph A:", graphA.get_graph())
print("---")
print("A* Search Algorithm on Test Graph A")
aSearch(graphA, (0,0), (2,3))
print("-----------------")
print("Test Graph B:", graphB.get_graph())
print("---")
print("A* Search Algorithm on Test Graph B")
aSearch(graphB, (0,0), (2,3))
print("-----------------")
print("Comparison of the three graphs:")
maxTravelTimePath = travelTimes.index(max(travelTimes))
minTravelTimePath = travelTimes.index(min(travelTimes))
print("The minimum travel time is:", min(travelTimes), "minutes through the", ("Example Graph path." if (minTravelTimePath == 0) else "Test Graph A path." if (minTravelTimePath == 1) else "Test Graph B path."))
print("The maximum travel time is:", max(travelTimes), "minutes through the", ("Example Graph path." if (maxTravelTimePath == 0) else "Test Graph A path." if (maxTravelTimePath == 1) else "Test Graph B path."))
print("The average travel time between the 3 graphs is: ", sum(travelTimes)/len(travelTimes), " minutes")
