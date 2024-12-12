with open("Day-12-Challenge/input.txt", "r") as file:
    garden_map = []
    for line in file:
        garden_map.append(list(map(str, line.strip())))


def get_area(region_cells):
    return len(region_cells)

def get_perimeter(region_cells, garden_map):
    perimeter = 0
    rows = len(garden_map)
    cols = len(garden_map[0]) if rows > 0 else 0
    for r, c in region_cells:
        # Check Up
        if r == 0 or garden_map[r-1][c] != garden_map[r][c]:
            perimeter += 1
        # Down
        if r == rows-1 or garden_map[r+1][c] != garden_map[r][c]:
            perimeter += 1
        # Left
        if c == 0 or garden_map[r][c-1] != garden_map[r][c]:
            perimeter += 1
        # Right
        if c == cols-1 or garden_map[r][c+1] != garden_map[r][c]:
            perimeter += 1
    return perimeter

def find_regions(garden_map):
    visited_cells = set()
    all_regions = []
    total_rows = len(garden_map)
    total_cols = len(garden_map[0]) if total_rows > 0 else 0

    def depth_first_search(start_row, start_col, crop_type):
        stack = [(start_row, start_col)]
        current_region = []
        while stack: # bfs would be implemented with queue
            row, col = stack.pop()
            if (row, col) in visited_cells:
                continue
            visited_cells.add((row, col))
            current_region.append((row, col))
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_row, neighbor_col = row + delta_row, col + delta_col
                if 0 <= neighbor_row < total_rows and 0 <= neighbor_col < total_cols:
                    if (garden_map[neighbor_row][neighbor_col] == crop_type and
                            (neighbor_row, neighbor_col) not in visited_cells):
                        stack.append((neighbor_row, neighbor_col))
        return current_region

    for row in range(total_rows):
        for col in range(total_cols):
            if (row, col) not in visited_cells:
                new_region = depth_first_search(row, col, garden_map[row][col])
                all_regions.append(new_region)

    return all_regions


regions = find_regions(garden_map)
total_price = 0
for region in regions:
    area = get_area(region)
    perimeter = get_perimeter(region, garden_map)
    total_price += area * perimeter

print(total_price)

# n = total number of cells in the garden map

# Time Complexity:
# Reading Input: O(n)
# Finding Regions (DFS): O(n)
# Calculating Perimeter: O(n)
# Total: O(n)

# Space Complexity:
# Storing garden_map: O(n)
# Visited Set: O(n)
# DFS Stack: O(n)
# Temporary Storage (regions): O(n)
# Total: O(n)
