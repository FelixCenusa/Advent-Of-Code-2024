def read_map(file_path):
    with open(file_path, "r") as file:
        raw_lines = file.readlines()
    map_grid = []
    for line in raw_lines:
        map_grid.append(list(line.strip()))
    return map_grid


def simulate_guard(grid):
    #               down     right  up       left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Find guard starting position and direction
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in "^>v<":
                guard_position = (row, col)
                current_direction = "^>v<".index(grid[row][col])
                #print(row, " ", col)
                break

    visited_positions = set([guard_position])
    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate next position
        row, col = guard_position
        dy, dx = directions[current_direction]
        next_position = (row + dy, col + dx)

        # Stop if the guard leaves the grid
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        # Check if the next position is blocked
        if grid[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4  # Turn right
        else:
            guard_position = next_position  # Move forward
            visited_positions.add(guard_position)

    return len(visited_positions)


file_path = "Day-6-Challenge/input.txt"
grid = read_map(file_path)
result = simulate_guard(grid)

print(result)


# r = rows in the grid
# c = columns in the grid
# k = cells guard visits during movement

# n = total input size (rows + columns)

# Time Complexity:
# Read Map: O(r * c)                 O(n)
# Find Guard's Start: O(r * c)       O(n)
# Simulate Movement: O(k)            O(k)
# Total: O(r * c + k)                O(n + k)

# Space Complexity:
# Grid Storage: O(r * c)             O(n)
# Visited Positions Set: O(r * c)    O(n)
# Auxiliary Variables: O(1)          O(1)
# Total: O(r * c + k)                O(n + k)

