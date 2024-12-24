# Parse input
with open("Day-24-Challenge\input.txt", "r") as file:
    lines = file.readlines()

# Separate formulas
formulas = {}
for line in lines:
    if "->" in line:
        data1, operator, data2, arrow, data3 = line.strip().split()
        formulas[data3] = (data1, data2, operator)


# Credit: HyperNeutrino
# Helper functions
def make_wire(prefix, num):
    """Create a wire name like x00, y03, z01."""
    return f"{prefix}{str(num).zfill(2)}"

def verify_z(wire, num):
    """Verify if the final output wire z[num] produces the correct value."""
    if wire not in formulas:
        return False
    x,y,op = formulas[wire]
    if op != "XOR":
        return False
    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or \
           (verify_intermediate_xor(y, num) and verify_carry_bit(x, num))

def verify_intermediate_xor(wire, num):
    """Check if a wire correctly computes an intermediate XOR value."""
    if wire not in formulas:
        return False
    x,y,op = formulas[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    """Check if a wire correctly computes a carry bit."""
    if wire not in formulas:
        return False
    x,y,op = formulas[wire]
    if num == 1:
        return op == "AND" and sorted([x, y]) == ["x00", "y00"]
    if op != "OR":
        return False
    return (verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1)) or \
           (verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1))

def verify_direct_carry(wire, num):
    """Check if a wire computes a direct carry."""
    if wire not in formulas:
        return False
    x,y,op = formulas[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    """Check if a wire correctly propagates a carry bit."""
    if wire not in formulas:
        return False
    x,y,op = formulas[wire]
    if op != "AND":
        return False
    return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or \
           (verify_intermediate_xor(y, num) and verify_carry_bit(x, num))

def verify(num):
    """Verify if the output for the nth bit is correct."""
    return verify_z(make_wire("z", num), num)

def progress():
    """Find the maximum number of bits correctly computed by the system."""
    i = 0
    while verify(i):
        i += 1
    return i

# Find the swaps
swaps = []
for _ in range(4):  # Four pairs of swaps
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y:
                continue
            # Swap and test
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                print(x)
                print(y)
                swaps.append(x)
                swaps.append(y)
                break
            # Undo the swap if it didn't improve
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break

# Output sorted swaps
print(",".join(sorted(swaps)))



# n = number of wires
# g = number of gates

# Time Complexity:
# Parsing Input: O(g)
# Generating Wires for Verification: O(n) per call
# Verifying Each Bit: O(g) per bit
# Progress Function: O(n * g) (verifies each bit until failure)
# Nested Swapping: O(g^2 * n * g) = O(g^3 * n) (4 swaps, each checks all pairs)
# Total: O(g^3 * n)

# Space Complexity:
# Input Storage: O(g)
# Temporary Wire State for Progress/Verification: O(n)
# Swap Tracking: O(8) (fixed swaps for 4 pairs)
# Total: O(g + n)
