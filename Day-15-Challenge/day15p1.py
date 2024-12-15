with open("Day-15-Challenge/input.txt", "r") as file:
    lines = file.readlines()
final_grid = [["."]*(50) for _ in range(len(lines[0]) - 1)]

def move_from_to(from_row,from_col,go_row,go_col, final_grid):
    if final_grid[from_row+go_row][from_col+go_col] == ".": # if no obstacles
        final_grid[from_row][from_col] = "." #remove robot
        final_grid[from_row+go_row][from_col+go_col] = "@" #add it to new location
        return True
    if final_grid[from_row+go_row][from_col+go_col] == "O": # if box
        O_riginal = [go_row,go_col]
        while True:
            if go_row > 0: # check what direction were going in, and keep going there
                go_row +=1
            if go_row < 0:
                go_row -=1
            if go_col > 0:
                go_col +=1
            if go_col < 0:
                go_col -=1
            
            if final_grid[from_row+go_row][from_col+go_col] == "#":
                return False # cant
            if final_grid[from_row+go_row][from_col+go_col] == ".":
                final_grid[from_row][from_col] = "." # remove @
                final_grid[from_row+O_riginal[0]][from_col+O_riginal[1]] = "@"
                final_grid[from_row+go_row][from_col+go_col] = "O"
                
                return True
    return False



moves = []
row = 0
for line in lines: #  format
    if "#" in line[0]:
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

print(final_grid)
print(moves)

def findRobotCoords(final_grid):
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "@":
                return row,col

def boxPoints(final_grid):
    total = 0
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "O":
                total += row * 100 + col
    return total
    
                


for move in moves:
    robot_row,robot_col = findRobotCoords(final_grid)
    # print(final_grid)
    # print("\n\n")
    if move == "<":
        #Left
        move_from_to(robot_row,robot_col,0,-1,final_grid)
        continue
    if move == ">":
        #Right
        move_from_to(robot_row,robot_col,0,1,final_grid)
        continue

    if move == "^":
        #Up
        move_from_to(robot_row,robot_col,-1,0,final_grid)
        continue

    if move == "v":
        #Down
        move_from_to(robot_row,robot_col,1,0,final_grid)
        continue
print(final_grid)
print("\n\n")
print(moves)
print("Box points", boxPoints(final_grid))


# n = total number of moves
# m = size of the grid (rows * columns)

# Time Complexity:
# Reading Input: O(m)
# Finding Robot Coordinates: O(m) per move → O(n * m)
# Move Execution:
#   - Free Space: O(1)
#   - Pushing Boxes: O(m) worst case
# Total: O(n * m)

# Space Complexity:
# Storing the Grid: O(m)
# Storing Moves: O(n)
# Temporary Variables: O(1)
# Total: O(m + n)