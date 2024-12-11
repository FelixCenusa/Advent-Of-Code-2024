from functools import cache

with open("Day-11-Challenge/input.txt", "r") as file:
    line = file.readline().strip()
stones = []
for number in line.split():
    stones.append(int(number))

# Define a cached recursive function to count stones after a given number of steps
# we can do this since stones never merge so a certain node never touches its neighbour.
# faster because we cant get a very large number until we have to split it
# so we sortof make a lookup table for the answer thats already been computed after some time.
@cache
def process_stone(value, remaining_blinks):
    if remaining_blinks == 0:  # Base case: no blinks left
        return 1
    if value == 0:  # if stone is 0
        return process_stone(1, remaining_blinks - 1)
    
    value_str = str(value)
    length = len(value_str)
    
    if length % 2 == 0:  # if even digits
        midpoint = length // 2
        left_half = int(value_str[:midpoint])
        right_half = int(value_str[midpoint:])
        return process_stone(left_half, remaining_blinks - 1) + process_stone(right_half, remaining_blinks - 1)
    else:  # otherwise, multiply stone by 2024
        new_value = value * 2024
        return process_stone(new_value, remaining_blinks - 1)


total_stones = 0
for stone in stones: # for each stone we see how many they make
    total_stones += process_stone(stone, 75)

print(total_stones)

# n = total number of stones in the initial input (file size)
# d = average number of digits per stone in the input
# b = total number of blinks

# Time Complexity:
# Reading Input: O(n)
# Recursive Processing per Stone: O(b * d)
# Total Recursive Processing for All Stones: O(n * b * d)

# Space Complexity:
# Input Storage: O(n)
# Caching Storage: O(n * b)
# Call Stack Depth: O(b)
# Total: O(n * b)
