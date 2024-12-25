with open("Day-25-Challenge-final/input.txt", "r") as file:
    lines = file.read()

# Parse input into locks and keys
def parse_schematics(data):
    sections = data.split("\n\n")  # Split when we find empty line
    locks = []
    keys = []

    for section in sections:
        schematic = []
        for line in section.splitlines():
            schematic.append(line)
        if all(char == "#" for char in schematic[0]):  # Top row filled, it's a lock
            locks.append(schematic)
        elif all(char == "#" for char in schematic[-1]):  # Bottom row filled, it's a key
            keys.append(schematic)

    return locks, keys

# Convert schematics to heights
def schematic_to_heights(schematic, reverse=False):
    heights = []
    width = len(schematic[0])
    height = len(schematic)

    for col in range(width):
        count = 0
        for row in range(height):
            if not reverse:
                char = schematic[row][col]
            else:
                char = schematic[height - 1 - row][col]
            if char == "#":
                count += 1
            else:
                break
        heights.append(count)

    return heights

# Count fitting pairs
def count_fitting_pairs(lock_heights, key_heights, max_height):
    count = 0
    for lock in lock_heights:
        for key in key_heights:
            fit = True
            for i in range(len(lock)):  # Assuming lock and key have the same width
                if lock[i] + key[i] > max_height:
                    fit = False
                    break

            if fit:
                count += 1

    return count


locks, keys = parse_schematics(lines)

# Convert locks and keys to height lists
lock_heights = []
for lock in locks:
    lock_heights.append(schematic_to_heights(lock))

key_heights = []
for key in keys:
    key_heights.append(schematic_to_heights(key, reverse=True)) # reverse to process

# Define the max height (number of rows in a lock or key)
max_height = len(locks[0])

# Calculate the number of fitting pairs
result = count_fitting_pairs(lock_heights, key_heights, max_height)

print(result)


# n = total number of schematics (locks + keys)
# w = number of columns (width of schematics)
# h = number of rows (height of schematics)

# Time Complexity:
# Parsing Input:               O(n * h), process each schematic line by line.
# Converting to Heights:       O(n * w * h), process all rows and columns for each schematic.
# Counting Fitting Pairs:      O(n^2 * w), compare each lock with each key across columns.
# Total:                       O(n * h + n * w * h + n^2 * w) so O(n^2)

# Space Complexity:
# Storing Parsed Schematics:   O(n * h), store all schematic rows.
# Storing Heights:             O(n * w), store heights for locks and keys.
# Total:                       O(n * h + n * w) so O(n)
