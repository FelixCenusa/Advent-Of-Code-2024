with open("Day-15-Challenge/input.txt", "r") as file:
    lines = file.readlines()
final_grid = [["."]*(50) for _ in range(len(lines[0]) - 1)]



def find_soulmate(final_grid, check_row,check_col):
    check = final_grid[check_row][check_col]
    if check == "[":
        return check_row,check_col+1
    if check == "]":
        return check_row,check_col-1

def collect_boxes_and_validate(final_grid, start_row, start_col, go_row, go_col):
    """ Collect all connected boxes and validate movement. """
    boxes_to_move = []  # Store all boxes to move
    queue = [(start_row, start_col)]

    # BFS-style search to collect all connected boxes and their soulmates
    while queue:
        current_row, current_col = queue.pop(0)

        # Add current box and soulmate if not already in the list
        if (current_row, current_col) not in boxes_to_move:
            boxes_to_move.append((current_row, current_col))
            soulmate = find_soulmate(final_grid, current_row, current_col)
            queue.append(soulmate) # soulmate must be searched for additional boxes
            if soulmate and soulmate not in boxes_to_move:
                boxes_to_move.append(soulmate)

        # Check the next box in the direction of movement
        next_row = current_row + go_row
        next_col = current_col + go_col
        if 0 <= next_row < len(final_grid) and 0 <= next_col < len(final_grid[0]):
            if final_grid[next_row][next_col] in ["[", "]"] and (next_row, next_col) not in boxes_to_move:
                queue.append((next_row, next_col))
            elif final_grid[next_row][next_col] == "#":  # Blocked by a wall
                return None

    

    return boxes_to_move


def move_from_to(from_row, from_col, go_row, go_col, final_grid):
    """ Move the robot and boxes in the specified direction. """
    next_row = from_row + go_row
    next_col = from_col + go_col

    # If the target space is free, move the robot
    if final_grid[next_row][next_col] == ".":
        final_grid[from_row][from_col] = "."
        final_grid[next_row][next_col] = "@"
        return True


    # if box, but approach from left or right:
    if go_row == 0 and go_col == -1: # if going left
        if final_grid[from_row+go_row][from_col+go_col] == "]": # if box
            Box_riginal = [[go_row,go_col]]
            while True:
                go_col -= 1
                Box_riginal.append([go_row,go_col])
                
                if final_grid[from_row+go_row][from_col+go_col] == "#":
                    return False # cant
                if final_grid[from_row+go_row][from_col+go_col] == ".": # found empty, execute.
                    final_grid[from_row][from_col] = "." # remove @
                    for i in range(len(Box_riginal)-1,0,-1): # scooch all the paranthesis
                        final_grid[from_row+Box_riginal[i][0]][from_col+Box_riginal[i][1]] = final_grid[from_row+Box_riginal[i-1][0]][from_col+Box_riginal[i-1][1]]
                    final_grid[from_row+Box_riginal[0][0]][from_col+Box_riginal[0][1]] = "@"
                    
                    return True

    # If box, but approach from the right
    if go_row == 0 and go_col == 1:  # If going right
        if final_grid[from_row + go_row][from_col + go_col] == "[":  # If box
            Box_riginal = [[go_row, go_col]]  # Track box positions relative to the robot
            while True:
                go_col += 1  # Move right
                Box_riginal.append([go_row, go_col])  # Add position to the list

                # If we hit a wall, the move is invalid
                if final_grid[from_row + go_row][from_col + go_col] == "#":
                    return False  # Can't move due to wall

                # If we find an empty space, execute the move
                if final_grid[from_row + go_row][from_col + go_col] == ".":
                    final_grid[from_row][from_col] = "."  # Remove the robot

                    # Scooch all the boxes right
                    for i in range(len(Box_riginal) - 1, 0, -1):
                        final_grid[from_row + Box_riginal[i][0]][from_col + Box_riginal[i][1]] = \
                            final_grid[from_row + Box_riginal[i - 1][0]][from_col + Box_riginal[i - 1][1]]

                    # Place the robot in its new position
                    final_grid[from_row + Box_riginal[0][0]][from_col + Box_riginal[0][1]] = "@"
                    return True

   
    # Up or Down, collect and validate all connected boxes
    if final_grid[next_row][next_col] in ["[", "]"]:
        # Collect all connected boxes and validate
        boxes = collect_boxes_and_validate(final_grid, next_row, next_col, go_row, go_col)
        if not boxes:  # Invalid collection or blocked by an obstacle
            return False

        # Move boxes step by step (farthest boxes first)
        boxes = sorted(boxes, reverse=(go_row == 1))  # Bottom-up for down, top-down for up
        for row, col in boxes:
            next_row = row + go_row
            next_col = col + go_col
            final_grid[next_row][next_col] = final_grid[row][col]  # Move the box
            final_grid[row][col] = "."  # Clear old position

        # Move the robot as the final step
        final_grid[from_row][from_col] = "."
        final_grid[from_row + go_row][from_col + go_col] = "@"

        return True

    return False


moves = []
row = 0
for line in lines: #  format
    if "#" in line:
        line = line.split("\n")[0]
        col = 0
        for i in line:
            final_grid[row][col] = i
            col += 1
        row += 1
    else:
        line = line.split("\n")[0]
        for i in line:
            moves.append(i)

# print(final_grid)
# print(moves)
temp_grid = [["."]*(100) for _ in range(len(lines[0]) - 1)]
for row in range(len(final_grid)):
    for col in range(len(final_grid[0])):
        if final_grid[row][col] == "#":
            temp_grid[row][2 * col - 1] = "#"
            temp_grid[row][2 * col    ] = "#"
        if final_grid[row][col] == "O":
            temp_grid[row][2 * col - 1] = "["
            temp_grid[row][2 * col    ] = "]"
        if final_grid[row][col] == ".":
            temp_grid[row][2 * col - 1] = "."
            temp_grid[row][2 * col    ] = "."
        if final_grid[row][col] == "@":
            temp_grid[row][2 * col - 1] = "@"
            temp_grid[row][2 * col    ] = "."
final_grid = temp_grid

def findRobotCoords(final_grid):
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "@":
                return row,col

def boxPoints(final_grid):
    total = 0
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "]":
                total += row * 100 + col
    return total
    
                


for move in moves:
    robot_row,robot_col = findRobotCoords(final_grid)
    # print(final_grid)
    # print("\n\n")
    if move == "<":
        #print("Move:", move)
        #Left
        move_from_to(robot_row,robot_col,0,-1,final_grid)
        continue
    if move == ">":
        #print("Move:", move)
        #Right
        move_from_to(robot_row,robot_col,0,1,final_grid)
        continue

    if move == "^":
        #print("Move:", move)
        #Up
        move_from_to(robot_row,robot_col,-1,0,final_grid)
        continue

    if move == "v":
        #print("Move:", move)
        #Down
        move_from_to(robot_row,robot_col,1,0,final_grid)
        continue
    
#print(final_grid)
print("Box points", boxPoints(final_grid))


# n = total number of moves
# m = size of the grid (rows * columns)
# k = number of boxes connected during traversal

# Time Complexity:
# Reading Input: O(m)
# Finding Robot Coordinates: O(m) per move → O(n * m)
# Box Validation (collect_boxes_and_validate):
#   - BFS to collect linked boxes: O(k)
#   - Checking free space for boxes: O(k)
# Moving Boxes:
#   - Moving all collected boxes: O(k)
# Total: O(n * (m + k))

# Space Complexity:
# Storing the Grid: O(m)
# Storing Moves: O(n)
# BFS Queue and Box Storage: O(k)
# Temporary Variables: O(1)
# Total: O(m + n + k)