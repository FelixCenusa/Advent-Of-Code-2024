with open("Day-11-Challenge/input.txt", "r") as file:
    line = file.readline().strip()
stones = []
for number in line.split():
    stones.append(int(number))

blinks = 75
for i in range(blinks):
    print(i) # to see how fast it goes
    new_stones = []
    for stone in stones:
        if stone == 0: # if stone is 0
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0: # if even digits
            half_len = len(str(stone)) // 2
            left_half = int(str(stone)[:half_len])
            right_half = int(str(stone)[half_len:])
            new_stones.extend([left_half, right_half])
        else: # otherwise, multiply stone by 2024
            new_stones.append(stone * 2024) # order doesnt matter so just append them
    stones = new_stones

print(len(stones))


# n = total number of stones in the initial input (file size)
# d = average number of digits per stone in the input
# b = total number of blinks

# Time Complexity:
# Reading Input: O(n)
# Processing Stones per Blink: O(n * d)
# Growth Across Blinks: O(n * 2^b)
# Total: O(n * 2^b)

# Space Complexity:
# Stone Storage: O(n * 2^b)
# Temporary Storage (e.g., strings): Negligible.
# Total: O(n * 2^b)
