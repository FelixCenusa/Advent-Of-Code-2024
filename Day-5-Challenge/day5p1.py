def parse(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()
    
    rules_part, updates_part = content.split("\n\n")
    
    # Parse rules into list of tuples of integers
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y))) #tuple (X, Y) appended to the list

    # Parse updates into lists of integers
    updates = []
    update_lines = updates_part.splitlines()
    for line in update_lines:
        pages = line.split(",")
        updates.append([int(page) for page in pages])

    return rules, updates


def solve(rules, updates):
    total = 0

    for update in updates:
        # Precompute indices for O(1) lookups
        page_indices = {}
        index = 0
        for page in update:
            page_indices[page] = index
            index += 1

        
        is_valid = True

        for x, y in rules:
            # Instead of checking membership in a list (O(P)),
            # dictionary allows O(1) membership checks.
            if x in page_indices and y in page_indices: # If both exist in update 
                if page_indices[x] > page_indices[y]:  # Rule violated
                    is_valid = False
                    break

        if is_valid:
            middle_page = len(update) // 2 # if even takes from right.
            total += update[middle_page]

    return total



file_path = "Day-5-Challenge\input.txt"
rules, updates = parse(file_path)
result = solve(rules, updates)
print(result)


# U = number of updates
# P = pages per update
# R = number of rules

# n = total input size (number of rules + pages in updates)

# Time Complexity:
# Parse Rules: O(R)                 O(n)
# Parse Updates: O(U * P)           O(n)
# Precompute Indices: O(U * P)      O(n)
# Rule Validation: O(U * R)         O(n)
# Total: O(U * (P + R))             O(n)

# Space Complexity:
# Rules List: O(R)                  O(n)
# Updates List: O(U * P)            O(n)
# Page Indices Dictionary: O(U * P) O(n)
# Total: O(U * P + R)               O(n)
