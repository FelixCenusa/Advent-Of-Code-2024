with open("Day-23-Challenge/input.txt", "r") as file: 
    lines = file.readlines()

# Build graph x - y
connections = []
for line in lines:
    connection = line.strip().split("-")
    connections.append(connection)


# Build adjacency list representation of the graph x: {y,z} y: {x} z:{x}
graph = {}
for a, b in connections:
    if a not in graph: graph[a] = set()
    if b not in graph: graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

# Find all sets of three interconnected computers
three_nodes = set()
for node in graph:
    neighbors = graph[node]
    for n1 in neighbors:
        for n2 in neighbors:
            if n1 != n2 and n2 in graph[n1]:
                three_nodes.add(tuple(sorted([node, n1, n2])))

# Filter three_nodes to include at least one computer starting with 't'
filtered_three_nodes = []
for triad in three_nodes:
    for computer in triad:
        if computer.startswith('t'):
            filtered_three_nodes.append(triad)
            break  # Exit inner loop as soon as a match is found

# Output the result
print(len(filtered_three_nodes))


# n = number of lines in the input
# m = average number of neighbors per node
# k = number of triads

# Time Complexity:
# Reading Input: O(n)
# Building Graph: O(n)
# Finding Triads: O(n * m^2)
# Filtering Triads: O(k)
# Total: O(n + n * m^2 + k) so O(n * m^2 + k)

# Space Complexity:
# Input Storage: O(n)
# Graph Storage: O(n * m)
# Triads Storage: O(k)
# Total: O(n * m + k)
