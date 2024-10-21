







class CodeLibraryText:
    
    input= """" 

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// K - Mean

Enter the number of data points: 9
Enter the coordinates for each data point:
Point 1 (space-separated): 2
Point 2 (space-separated): 4
Point 3 (space-separated): 10
Point 4 (space-separated): 12
Point 5 (space-separated): 3
Point 6 (space-separated): 20
Point 7 (space-separated): 30
Point 8 (space-separated): 11
Point 9 (space-separated): 25

Enter the number of clusters: 2
Enter the coordinates for each initial centroid:
Centroid 1 (space-separated): 3
Centroid 2 (space-separated): 11

Results:
Cluster 1: [array([2.]), array([4.]), array([10.]), array([12.]), array([3.]), array([11.])]
Cluster 2: [array([20.]), array([30.]), array([25.])]
Final centroids:
Centroid 1: [7.]
Centroid 2: [25.]

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Page Rank
Enter the number of data points: 9
Enter the coordinates for each data point:
Point 1 (space-separated): 2
Point 2 (space-separated): 4
Point 3 (space-separated): 10
Point 4 (space-separated): 12
Point 5 (space-separated): 3
Point 6 (space-separated): 20
Point 7 (space-separated): 30
Point 8 (space-separated): 11
Point 9 (space-separated): 25

Enter the number of clusters: 2
Enter the coordinates for each initial centroid:
Centroid 1 (space-separated): 3
Centroid 2 (space-separated): 11

Results:
Cluster 1: [array([2.]), array([4.]), array([10.]), array([12.]), array([3.]), array([11.])]
Cluster 2: [array([20.]), array([30.]), array([25.])]
Final centroids:
Centroid 1: [7.]
Centroid 2: [25.]


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// FP - TREE

Enter the number of transactions: 5
Enter items in transaction 1 (space-separated): M O N K E Y
Enter items in transaction 2 (space-separated): D O N K E Y
Enter items in transaction 3 (space-separated): M A K E
Enter items in transaction 4 (space-separated): M U C K Y
Enter items in transaction 5 (space-separated): C O O K I E
Enter the minimum support count: 3
Enter the minimum confidence (as a decimal, e.g., 0.6 for 60%): 0.8

FP-Tree after inserting T1:

Final FP-Tree Structure:
K:5
   E:4
      M:1
      O:3
         M:1
         Y:1
      O:1
         Y:1
   M:1
      Y:1

Conditional Pattern Bases:
E: [(['K'], 4)]
K: []
M: [(['K', 'E', 'O'], 1), (['K'], 1)]
O: [(['K', 'E'], 3), (['K', 'E', 'O'], 1)]
Y: [(['K', 'E', 'O', 'M'], 1), (['K', 'M'], 1)]


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Apriori


Enter items for transaction 5 (separate items by space): I1 I3
Enter items for transaction 6 (separate items by space): I2 I3
Enter items for transaction 7 (separate items by space): I1 I3
Enter items for transaction 8 (separate items by space): I1 I2 I3 I5
Enter items for transaction 9 (separate items by space): I1 I2 I3
Enter the minimum support count (e.g., 2 for at least 2 transactions): 2
Enter the minimum confidence (e.g., 0.6 for 60%): 0.7

Frequent 1-itemsets:
{'I2'}: 7 transactions
{'I5'}: 2 transactions
{'I3'}: 6 transactions
{'I4'}: 2 transactions
{'I1'}: 6 transactions

Frequent 2-itemsets:
{'I2', 'I1'}: 4 transactions
{'I1', 'I3'}: 4 transactions
{'I2', 'I4'}: 2 transactions
{'I2', 'I5'}: 2 transactions
{'I1', 'I5'}: 2 transactions
{'I2', 'I3'}: 4 transactions

Frequent 3-itemsets:
{'I2', 'I1', 'I5'}: 2 transactions
{'I2', 'I3', 'I1'}: 2 transactions



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ID3

Enter the number of attributes: 3
Enter name of attribute 1: age
Enter name of attribute 2: comp
Enter name of attribute 3: type
Enter the name of the target attribute: profit
Enter the number of rows in the dataset: 10
Enter 10 rows of data, with values separated by spaces:
old yes soft down
old no soft down
old no hard down
mid yes soft down
mid yes hard down
mid no hard up
mid no soft up
new yes soft up
new no hard up
new no soft up

Decision Tree:
age :
  new:
    profit: up
  mid:
    type:
      no:
        profit: up
      yes:
        profit: down
  old:
    profit: down




/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// naive bayes


Enter the number of columns (including the class column): 2
Enter name for column 1: color
Enter name for column 2: class
Enter the number of rows: 3
Enter value for color in row 1: Red
Enter value for class in row 1: Fruit
Enter value for color in row 2: Green
Enter value for class in row 2: Vegetable
Enter value for color in row 3: Red
Enter value for class in row 3: Fruit

Dataset:
   color      class
0    Red      Fruit
1  Green  Vegetable
2    Red      Fruit

Enter the name of the class column: class
Enter value for color in the new instance: Red

Probabilities:
P(Fruit | X) = 0.6666666666666666
P(Vegetable | X) = 0.0

The predicted class is: Fruit

    """

    fptree = """ 
class FPNode:
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.next = None


class FPTree:
    def __init__(self, transactions, min_support):
        self.min_support = min_support
        self.header_table = {}
        self.root = FPNode(None, 0, None)
        self.transactions = transactions
        self.frequent_items = self._get_frequent_items()
        self._build_tree()


    def _get_frequent_items(self):
        item_count = {}
        for transaction in self.transactions:
            for item in transaction:
                item_count[item] = item_count.get(item, 0) + 1
        return {k: v for k, v in item_count.items() if v >= self.min_support}


    def _build_tree(self):
        for i, transaction in enumerate(self.transactions, 1):
            sorted_items = sorted(
                [item for item in transaction if item in self.frequent_items],
                key=lambda x: (-self.frequent_items[x], x)
            )
            if sorted_items:
                self._insert_tree(sorted_items, self.root)
            print(f"\nFP-Tree after inserting T{i}:")
            self._print_tree(self.root)


    def _insert_tree(self, items, node):
        if items:
            item = items[0]
            if item in node.children:
                node.children[item].count += 1
            else:
                new_node = FPNode(item, 1, node)
                node.children[item] = new_node
                if item not in self.header_table:
                    self.header_table[item] = new_node
                else:
                    current = self.header_table[item]
                    while current.next:
                        current = current.next
                    current.next = new_node
            self._insert_tree(items[1:], node.children[item])


    def _print_tree(self, node, indent=""):
        if node.item:
            print(f"{indent}{node.item}:{node.count}")
        for child in sorted(node.children.values(), key=lambda x: x.item):
            self._print_tree(child, indent + " ")


def get_conditional_pattern_base(node):
    patterns = []
    while node:
        path = []
        support = node.count
        current = node.parent
        while current.parent:
            path.append(current.item)
            current = current.parent
        if path:
            patterns.append((list(reversed(path)), support))
        node = node.next
    return patterns


# Function to get user input for transactions, min_support, and min_confidence
def get_user_input():
    num_transactions = int(input("Enter the number of transactions: "))
    transactions = []
   
    for i in range(num_transactions):
        transaction = input(f"Enter items in transaction {i+1} (space-separated): ").split()
        transactions.append(transaction)
   
    min_support = int(input("Enter the minimum support count: "))
    min_confidence = float(input("Enter the minimum confidence (as a decimal, e.g., 0.6 for 60%): "))
   
    return transactions, min_support, min_confidence


if __name__ == "__main__":
    # Get user input
    transactions, min_support, min_confidence = get_user_input()


    # Create FP-Tree
    fp_tree = FPTree(transactions, min_support)
    print("\nFinal FP-Tree Structure:")
    fp_tree._print_tree(fp_tree.root)


    print("\nConditional Pattern Bases:")
    for item in sorted(fp_tree.header_table.keys()):
        patterns = get_conditional_pattern_base(fp_tree.header_table[item])
        print(f"{item}: {patterns}")


    # For now, min_confidence is just taken as input and not yet used in the FP-Tree.
    """

    apriori = """ 
from itertools import combinations


# Helper function to calculate support count for an itemset
def calculate_support_count(itemset, transactions):
    count = sum(1 for transaction in transactions if itemset.issubset(transaction))
    return count


# Generate all candidate itemsets of a specific length
def generate_candidates(frequent_itemsets, length):
    candidates = set()
    for itemset1 in frequent_itemsets:
        for itemset2 in frequent_itemsets:
            union_itemset = itemset1 | itemset2  # Union of two itemsets
            if len(union_itemset) == length:  # Only keep itemsets of the desired length
                candidates.add(frozenset(union_itemset))
    return candidates


# Apriori algorithm implementation with support count
def apriori(transactions, min_support_count):
    # Step 1: Convert transactions to list of sets
    transactions = [set(transaction) for transaction in transactions]


    # Step 2: Generate frequent 1-itemsets
    itemsets = set()
    for transaction in transactions:
        for item in transaction:
            itemsets.add(frozenset([item]))


    # Step 3: Prune infrequent itemsets based on support count
    frequent_itemsets = []
    for itemset in itemsets:
        support_count = calculate_support_count(itemset, transactions)
        if support_count >= min_support_count:
            frequent_itemsets.append((itemset, support_count))


    # Print frequent 1-itemsets
    print("Frequent 1-itemsets:")
    for itemset, support_count in frequent_itemsets:
        print(f"{set(itemset)}: {support_count} transactions")


    # Step 4: Generate higher-order itemsets (2-itemsets, 3-itemsets, etc.)
    k = 2
    while frequent_itemsets:
        candidates = generate_candidates([itemset for itemset, _ in frequent_itemsets], k)
        frequent_itemsets = []
        for candidate in candidates:
            support_count = calculate_support_count(candidate, transactions)
            if support_count >= min_support_count:
                frequent_itemsets.append((candidate, support_count))


        # Print frequent k-itemsets
        if frequent_itemsets:
            print(f"\nFrequent {k}-itemsets:")
            for itemset, support_count in frequent_itemsets:
                print(f"{set(itemset)}: {support_count} transactions")


        k += 1


# Main function to take user input
def get_user_input():
    # Input for number of transactions
    num_transactions = int(input("Enter the number of transactions: "))


    # Input for each transaction (items separated by space)
    transactions = []
    for i in range(num_transactions):
        transaction = input(f"Enter items for transaction {i+1} (separate items by space): ").split()
        transactions.append(transaction)


    # Input for minimum support count
    min_support_count = int(input("Enter the minimum support count (e.g., 2 for at least 2 transactions): "))


    # Input for minimum confidence (though it’s not used in the current apriori implementation)
    min_confidence = float(input("Enter the minimum confidence (e.g., 0.6 for 60%): "))


    return transactions, min_support_count, min_confidence


# Get user input
transactions, min_support_count, min_confidence = get_user_input()


# Run the Apriori algorithm
apriori(transactions, min_support_count)
    """
    
    pagerank= """ 
def page_rank(graph,max_iterations,damping_factor=0.85):
    num_pages=len(graph)
    pr={page:1/num_pages for page in graph}
    for _ in range(max_iterations):
        new_pr={}
        for page in graph:
            incoming_pr=sum(pr[i]/len(graph[i]) for i in graph if page in graph[i])
            new_pr[page]=(1-damping_factor)*damping_factor+incoming_pr
        pr=new_pr
    for page,rank in pr.items():
        print(f"{page}:{rank}")
    return pr

def get_graph_input():
    graph={}
    while True:
        page=input("Enter the page:")
        if not page:
            break
        links=input(f"Enter the links associated with {page}:").split(',')
        graph[page]=[link.strip() for link in links if link.strip()]
    return graph
print("Enter the graph structure:")
graph=get_graph_input()
iter=int(input("Iterations:"))
result=page_rank(graph,iter)
for page,rank in result.items():
    print(f"{page}:{rank}")
    """

    kmeans = """ 
import random
import statistics

def distance(x, centroid):
    return abs(x - centroid)

arr = []
n = int(input("Enter the number of elements in the Array: "))
print("Enter the Elements:\n")
for i in range(n):
    num = int(input(f"Element {i + 1}: "))
    arr.append(num)

k = int(input("Enter the number of clusters (k): "))

# Step 1: Initialize k random centroids
centroids = random.sample(arr, k)
print("Initial centroids:", centroids)

# Step 2: Iterative processṁ
iteration = 0
while True:
    iteration += 1
    print(f"\nIteration {iteration}")

    # Create empty clusters
    clusters = {i: [] for i in range(k)}

    # Step 3: Assign each point to the nearest centroid
    for x in arr:
        distances = [distance(x, centroid) for centroid in centroids]
        nearest_centroid = distances.index(min(distances))  # Find closest centroid
        clusters[nearest_centroid].append(x)

    # Step 4: Update centroids (calculate the mean of each cluster)
    new_centroids = []
    for i in range(k):
        if clusters[i]:  # If cluster is not empty
            new_centroids.append(statistics.mean(clusters[i]))
        else:  # If cluster is empty, keep the old centroid
            new_centroids.append(centroids[i])

    print("Clusters:", clusters)
    print("Updated centroids:", new_centroids)

    # Check for convergence (if centroids don't change, break)
    if new_centroids == centroids:
        break

    # Update centroids for the next iteration
    centroids = new_centroids

# Final output
print("\nFinal clusters:", clusters)
print("Final centroids:", centroids)
    """
    
    id3 = """
import math
from collections import Counter


class Node:
    def __init__(self, attribute=None, value=None, results=None, branches=None):
        self.attribute = attribute
        self.value = value
        self.results = results
        self.branches = branches or {}


def entropy(data):
    counts = Counter(row[-1] for row in data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values() if count > 0)


def information_gain(data, attribute_index):
    base_entropy = entropy(data)
    weighted_entropy = 0
    for value in set(row[attribute_index] for row in data):
        subset = [row for row in data if row[attribute_index] == value]
        weighted_entropy += len(subset) / len(data) * entropy(subset)
    return base_entropy - weighted_entropy


def id3(data, attributes):
    if len(set(row[-1] for row in data)) == 1:
        return Node(results=data[0][-1])
   
    if not attributes:
        return Node(results=Counter(row[-1] for row in data).most_common(1)[0][0])
   
    best_attribute_index = max(range(len(attributes)), key=lambda i: information_gain(data, i))
    best_attribute = attributes[best_attribute_index]
   
    tree = Node(attribute=best_attribute)
    remaining_attributes = attributes[:best_attribute_index] + attributes[best_attribute_index+1:]
   
    for value in set(row[best_attribute_index] for row in data):
        subset = [row for row in data if row[best_attribute_index] == value]
        subtree = id3(subset, remaining_attributes)
        tree.branches[value] = subtree
   
    return tree


def print_tree(node, indent=""):
    if node.results is not None:
        print(f"{indent}{target_attribute}: {node.results}")
    else:
        print(f"{indent}{node.attribute}:")
        for value, branch in node.branches.items():
            print(f"{indent}  {value}:")
            print_tree(branch, indent + "    ")


def classify(tree, instance):
    if tree.results is not None:
        return tree.results
    value = instance[tree.attribute]
    if value not in tree.branches:
        return None
    return classify(tree.branches[value], instance)


# Get user input for dataset structure
num_attributes = int(input("Enter the number of attributes: "))
attributes = [input(f"Enter name of attribute {i+1}: ") for i in range(num_attributes)]
target_attribute = input("Enter the name of the target attribute: ")
attributes.append(target_attribute)


num_rows = int(input("Enter the number of rows in the dataset: "))


# Get user input for dataset
print(f"Enter {num_rows} rows of data, with values separated by spaces:")
data = []
for _ in range(num_rows):
    row = input().strip().split()
    if len(row) != len(attributes):
        print(f"Error: Expected {len(attributes)} values, but got {len(row)}. Please try again.")
        row = input().strip().split()
    data.append(row)


# Build the decision tree
tree = id3(data, attributes[:-1])


# Print the decision tree
print("\nDecision Tree:")
print_tree(tree)
    """
    
    naivebayes = """
import pandas as pd
from collections import defaultdict


def get_user_input():
    num_columns = int(input("Enter the number of columns (including the class column): "))
    column_names = [input(f"Enter name for column {i+1}: ") for i in range(num_columns)]
    num_rows = int(input("Enter the number of rows: "))
   
    data = []
    for i in range(num_rows):
        row = [input(f"Enter value for {col} in row {i+1}: ") for col in column_names]
        data.append(row)
   
    return pd.DataFrame(data, columns=column_names)


def naive_bayes_classify(df, class_column, new_instance):
    class_values = df[class_column].unique()
    probabilities = {}


    for class_value in class_values:
        class_prob = len(df[df[class_column] == class_value]) / len(df)
        conditional_probs = 1


        for attr, value in new_instance.items():
            if attr != class_column:
                count = len(df[(df[class_column] == class_value) & (df[attr] == value)])
                total = len(df[df[class_column] == class_value])
                conditional_probs *= (count / total)


        probabilities[class_value] = conditional_probs * class_prob


    return probabilities


def main():
    df = get_user_input()
    print("\nDataset:")
    print(df)


    class_column = input("\nEnter the name of the class column: ")
   
    new_instance = {}
    for col in df.columns:
        if col != class_column:
            new_instance[col] = input(f"Enter value for {col} in the new instance: ")


    probabilities = naive_bayes_classify(df, class_column, new_instance)


    print("\nProbabilities:")
    for class_value, prob in probabilities.items():
        print(f"P({class_value} | X) = {prob}")


    predicted_class = max(probabilities, key=probabilities.get)
    print(f"\nThe predicted class is: {predicted_class}")


if __name__ == "__main__":
    main()
"""


    olap = """ 
------------------------------------------- Create example tables
CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    region VARCHAR(50),
    product VARCHAR(50),
    sales DECIMAL(10, 2)
);

------------------------------------------- Insert sample data into sales_data
INSERT INTO sales_data (sale_id, region, product, sales) VALUES
(1, 'East', 'A', 100.00),
(2, 'East', 'B', 200.00),
(3, 'West', 'A', 150.00),
(4, 'West', 'B', 250.00),
(5, 'East', 'A', 300.00),
(6, 'East', 'C', 400.00),
(7, 'West', 'B', 500.00),
(8, 'West', 'C', 600.00);

------------------------------------------- ROLLUP Example
SELECT 
    region, 
    product, 
    SUM(sales) AS total_sales
FROM 
    sales_data
GROUP BY 
    ROLLUP(region, product);

------------------------------------------- DRILL DOWN Example
SELECT 
    region, 
    product, 
    SUM(sales) AS total_sales
FROM 
    sales_data
GROUP BY 
    region, product
ORDER BY 
    region, product;

------------------------------------------- PIVOT Example (SQL Server syntax)
SELECT *
FROM 
    (SELECT 
         region, 
         product, 
         sales 
     FROM 
         sales_data) AS SourceTable
PIVOT 
    (SUM(sales) FOR product IN ([A], [B], [C])) AS PivotTable;

------------------------------------------- DICE Example
SELECT 
    region, 
    product, 
    sales
FROM 
    sales_data
WHERE 
    region IN ('East', 'West') 
    AND product IN ('A', 'B');

------------------------------------------- SLICE Example
SELECT 
    region, 
    product, 
    sales
FROM 
    sales_data
WHERE 
    region = 'East';  -- Slicing for the 'East' region

------------------------------------------- Clean up (optional)
DROP TABLE sales_data;

    """
    
    ai=""" 
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
    


    def __init__(self):
        
        pass  














class CodeLibrary:
    def __init__(self):
        self.cdt = CodeLibraryText()  # Use self to make it an instance attribute
        pass

    def kmeans(self):
        print(self.cdt.kmeans)
        
    def apriori(self):
        print(self.cdt.apriori)

    def pagerank(self):
        print(self.cdt.pagerank)
        
    def fptree(self):
        print(self.cdt.fptree)
        
    def id3(self):
        print(self.cdt.id3)
        
    def naivebayes(self):
        print(self.cdt.naivebayes)
        
        
        
    def all(self):
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("Naive Bayes Algorithm:")
        print(self.cdt.naivebayes)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        
        print("\nID3 Algorithm:")
        print(self.cdt.id3)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        
        print("\nFP-Tree Algorithm:")
        print(self.cdt.fptree)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        
        print("\nPageRank Algorithm:")
        print(self.cdt.pagerank)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        
        print("\nK-Means Algorithm:")
        print(self.cdt.kmeans)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        
        print("\nApriori Algorithm:")
        print(self.cdt.apriori)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

    def olap(self):
        print(self.cdt.olap)

    def input(self):
        print(self.cdt.input)

    def ai(self):
        print(self.cdt.ai)



    def list(self):
        function_names = [
            "List of Functions:",
            "all",
            "olap",
            "input",
            "naivebayes",
            "id3",
            "fptree",
            "pagerank",
            "kmeans",
            "apriori",
        ]

        
        print("\n".join(function_names))  # Use join to print the list as a string




print("printing...")

