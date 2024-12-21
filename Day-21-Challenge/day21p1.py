# Same code as part 2, but compute_sequence_length(sequence, depth=2): not 25
from collections import deque
from functools import cache
from itertools import product

# Precompute all sequences between keys on a keypad using BFS
def compute_sequences(keypad_layout):
    key_positions = {}
    for row_idx, row in enumerate(keypad_layout):
        for col_idx, key in enumerate(row):
            if key is not None:
                key_positions[key] = (row_idx, col_idx)

    sequences = {}
    for start_key in key_positions:
        for target_key in key_positions:
            if start_key == target_key:
                sequences[(start_key, target_key)] = ["A"]
                continue

            possible_paths = []
            queue = deque([(key_positions[start_key], "")])
            shortest_length = float("inf")

            while queue:
                (current_row, current_col), path = queue.popleft()
                for new_row, new_col, move in [
                    (current_row - 1, current_col, "^"),
                    (current_row + 1, current_col, "v"),
                    (current_row, current_col - 1, "<"),
                    (current_row, current_col + 1, ">")
                ]:
                    if new_row < 0 or new_col < 0 or new_row >= len(keypad_layout) or new_col >= len(keypad_layout[0]):
                        continue
                    if keypad_layout[new_row][new_col] is None:
                        continue

                    if keypad_layout[new_row][new_col] == target_key:
                        if len(path) + 1 > shortest_length:
                            break
                        shortest_length = len(path) + 1
                        possible_paths.append(path + move + "A")
                    else:
                        queue.append(((new_row, new_col), path + move))
                else:
                    continue
                break

            sequences[(start_key, target_key)] = possible_paths

    return sequences

# Generate all possible sequences for an input string using precomputed paths
def generate_sequences(input_string, sequences):
    sequence_options = []
    for current_key, next_key in zip("A" + input_string, input_string):
        sequence_options.append(sequences[(current_key, next_key)])
    combined_sequences = []
    for sequence in product(*sequence_options):
        combined_sequences.append("".join(sequence))
    return combined_sequences

# Define keypads
numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

directional_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]


# Compute the length of a sequence, accounting for intermediate keypads recursively
@cache
def compute_sequence_length(sequence, depth=2):
    if depth == 1:
        total_length = 0
        for start, end in zip("A" + sequence, sequence):
            total_length += directional_lengths[(start, end)]
        return total_length

    total_length = 0
    for start, end in zip("A" + sequence, sequence):
        shortest_path = min(
            compute_sequence_length(subsequence, depth - 1)
            for subsequence in directional_sequences[(start, end)]
        )
        total_length += shortest_path
    return total_length


# Precompute sequences for both keypads
numeric_sequences = compute_sequences(numeric_keypad)
directional_sequences = compute_sequences(directional_keypad)

# Precompute path lengths for directional keypad
directional_lengths = {}
for key_pair, paths in directional_sequences.items():
    first_path = paths[0]
    directional_lengths[key_pair] = len(first_path)

total_complexity = 0

with open("Day-21-Challenge/input.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    numeric_inputs = generate_sequences(line, numeric_sequences)
    lengths = []
    for sequence in numeric_inputs:
        lengths.append(compute_sequence_length(sequence))
    shortest_length = min(lengths)
    total_complexity += shortest_length * int(line[:-1])

print(total_complexity)
