from functools import cache
with open("Day-19-Challenge/input.txt", "r") as file: 
    lines = file.readlines()

towel_patterns = []
designs = []

split_index = lines.index("\n") # find where data splits

raw_patterns = lines[:split_index][0]
raw_pattern_list = raw_patterns.split(",")
towel_patterns = []
for pattern in raw_pattern_list:
    towel_patterns.append(pattern.strip())

raw_designs = lines[split_index+1:]
designs = []
for design in raw_designs:
    designs.append(design.strip())

@cache
def can_construct_design(design):
    # Recursive
    if not design:
        return True
    for pattern in towel_patterns:
        if design[:len(pattern)] == pattern:  # start of the design matches the pattern?
            if can_construct_design(design[len(pattern):]):
                return True

    return False

possible_designs = 0
for design in designs:
    if can_construct_design(design):
        possible_designs += 1

print(possible_designs)

# t = total number of towel patterns
# d = average length of a design
# n = total number of designs

# Time Complexity:
# Reading Input: O(t + n)
# Recursive Processing per Design: O(t^d)
# Total: O(n * t^d)

# Space Complexity:
# Input Storage: O(t + n)
# Caching Storage: O(n * d)
# Call Stack Depth: O(d)
# Total: O(n * d)
