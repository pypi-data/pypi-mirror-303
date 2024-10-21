
ai =""" 
////////////////////////////////////////////////////////////////////////////////////////////////////////MINMAX
import math

def minimax(depth, node_index, is_max, scores, h):
    if depth == h:  # Check if leaf node
        return scores[node_index]
    
    if is_max:  # Maximizer's turn
        return max(minimax(depth + 1, node_index * 2, False, scores, h),
                   minimax(depth + 1, node_index * 2 + 1, False, scores, h))
    else:  # Minimizer's turn
        return min(minimax(depth + 1, node_index * 2, True, scores, h),
                   minimax(depth + 1, node_index * 2 + 1, True, scores, h))

def log2_custom(n):
    return 0 if n == 1 else 1 + log2_custom(n // 2)

n = int(input("Enter the number of scores (must be a power of 2): "))
scores = [int(input("Enter score {}: ".format(i + 1))) for i in range(n)]

h = log2_custom(n)  # Calculate tree height
res = minimax(0, 0, True, scores, h)  # Find optimal value
print("The optimal value is:", res)

///////////////////////////////////////////////////////////////////////////////////////////////BFS
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()  # To keep track of all vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)  # Add both vertices to the vertex set

    def BFS(self, s):
        if s not in self.vertices:
            print(f"Source vertex {s} is not in the graph!")
            return

        # Create a visited dictionary for all vertices
        visited = {vertex: False for vertex in self.vertices}
        queue = []

        # Enqueue the starting vertex and mark it as visited
        queue.append(s)
        visited[s] = True

        while queue:
            val = queue.pop(0)
            print(val, end=" ")

            # Explore neighbors
            for i in self.graph[val]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def getinput(self):
        n = int(input("Enter the number of edges: "))
        for _ in range(n):
            u, v = map(int, input("Enter the vertices between which edges exist separated by space: ").split())
            self.addEdge(u, v)

# Driver code
g = Graph()
g.getinput()

source = int(input("Enter the source vertex for BFS: "))
print(f"\nFollowing is Breadth First Traversal (starting from vertex {source}):")
g.BFS(source)
////////////////////////////////////////////////////////////////////////////////////////////////////////////BEST-FIRST-SEARCH
def greedy_best_first_search(graph, start_node, goal_node, heuristic):
    queue = [(start_node, heuristic[start_node])]
    visited = set()
    
    while queue:
        queue.sort(key=lambda x: x[1])  # Sort by heuristic value
        curr_node, h_value = queue.pop(0)
        
        if curr_node == goal_node:
            print(f"Goal found at: {curr_node}")
            return
        
        visited.add(curr_node)
        
        for neighbor in graph[curr_node]:
            if neighbor not in visited and neighbor not in [n[0] for n in queue]:
                queue.append((neighbor, heuristic[neighbor]))
    
    print("Goal not found")

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(n):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighboring nodes to {node} (separated by spaces): ").split()
        graph[node] = neighbors  # Store as a list of neighbors
    
    return graph

def heuristic_input(graph):
    heuristic = {}
    
    for node in graph:
        val = int(input(f"Enter the heuristic value for node {node}: "))
        heuristic[node] = val
    
    return heuristic

def main():
    graph = input_graph()
    heuristic = heuristic_input(graph)
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    greedy_best_first_search(graph, start_node, goal_node, heuristic)

if __name__ == "__main__":
    main()
//////////////////////////////////////////////////////////////////////////////////////////////////////HILL-CLIMB
def hill_climb(objective_function,solution):
    current_solution=solution
    current_value=objective_function(current_solution)
    print(f"Initial Solution:{current_solution} | Initial Value:{current_value}")
    while True:
        neighbours=generate_neighbours(current_solution)
       
        best_neighbour=None
        best_value=current_value
        for neighbour in neighbours:
            neighbour_value=objective_function(neighbour)
            if neighbour_value>best_value:
                best_value=neighbour_value
                best_neighbour=neighbour
        if best_neighbour is None:
            break
        current_solution=best_neighbour
        current_value=best_value
        
        
    return current_solution,current_value
def generate_neighbours(solution):
    return [solution+1,solution-1]
def objective_function(x):
    return -x**2+10*x+5
initial_solution = int(input('Enter an initial solution (integer): '))
result, value = hill_climb(objective_function, initial_solution)

print(f'Optimal solution: {result}, Objective value: {value}')
    """
    

def ai():
    print(ai)