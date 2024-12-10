def read_map(file_path):
    with open(file_path, "r") as file:
        height_map = []
        for line in file:
            height_map.append(list(map(int, line.strip())))
    return height_map

def find_trailheads(height_map): # == find zeros
    trailheads = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def dfs_count_trails(height_map, x, y, visited): # Depth First Search
    rows, cols = len(height_map), len(height_map[0])
    
    # Base case: Stop if we've reached a height of 9
    if height_map[x][y] == 9:
        return 1
    
    visited.add((x, y))
    total_trails = 0
    current_height = height_map[x][y]
    
    # Explore all possible moves recursively
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  #  left, right, down, up
        new_x, new_y = x + dx, y + dy
        # if not out of range, not visited and just +1 in height
        if (0 <= new_x < rows and 0 <= new_y < cols and
                (new_x, new_y) not in visited and
                height_map[new_x][new_y] == current_height + 1):
            total_trails += dfs_count_trails(height_map, new_x, new_y, visited.copy())
    
    return total_trails

def calculate_trailhead_ratings(height_map):
    trailheads = find_trailheads(height_map) # coordinates of zeros
    total_rating = 0
    
    for trailhead in trailheads:
        visited = set()
        total_rating += dfs_count_trails(height_map, trailhead[0], trailhead[1], visited)
    
    return total_rating

file_path = "Day-10-Challenge/input.txt"
height_map = read_map(file_path)
total_rating = calculate_trailhead_ratings(height_map)
print(total_rating)


# n = total number of elements in the input grid (file size)
# k = average number of valid recursive paths explored per trailhead

# Time Complexity:
# Read Map: O(n)                               
# Find Trailheads: O(n)                        
# Recursive DFS Calls per Trailhead: O(k)      
# Total DFS for All Trailheads: O(n * k)       Worst-case: O(n^2)

# Space Complexity:
# Height Map Storage: O(n)                    
# Visited Set Storage: O(n)                   
# Call Stack Depth per DFS: O(n)              
# Total: O(n)
