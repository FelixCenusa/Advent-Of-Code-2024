with open("Day-23-Challenge/input.txt", "r") as file: 
    lines = file.readlines()

# Build adjacency list representation of the graph
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

# Helper function to find the largest network using search
visited_networks = set()

def search(node, network):
    key = tuple(sorted(network))
    if key in visited_networks:
        return
    visited_networks.add(key)

    for neighbor in graph[node]:
        if neighbor in network:
            continue
        if not all(neighbor in graph[other] for other in network):
            continue
        search(neighbor, network | {neighbor}) # union of sets

# Find all networks
for node in graph:
    search(node, {node})

# Get the largest network
largest_network = max(visited_networks, key=len)

# Generate the password
password = ",".join(sorted(largest_network))
print(password)


# n = number of lines in the input
# m = average number of neighbors per node
# l = size of the largest network

# Time Complexity:
# Reading Input: O(n)
# Building Graph: O(n)
# Search Function: O(n * 2^n) (explores all subsets of nodes)
# Finding Largest Network: O(2^n)
# Generating Password: O(l * log(l))
# Total: O(n + n * 2^n + l * log(l)) so O(n * 2^n)

# Space Complexity:
# Input Storage: O(n)
# Graph Storage: O(n * m)
# Visited Networks Storage: O(2^n)
# Total: O(n * m + 2^n)
