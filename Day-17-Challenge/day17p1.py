# Read the input from the file
with open("Day-17-Challenge/input.txt", "r") as file:
    lines = file.readlines()

# Parse the registers
registers = {
    "A": int(lines[0].split(":")[1].strip()),
    "B": int(lines[1].split(":")[1].strip()),
    "C": int(lines[2].split(":")[1].strip())
}

# Parse the program
program = []
program_line = lines[4].split(":")[1].strip()
for value in program_line.split(","):
    program.append(int(value))



# Operand combo mapping
def get_combo_value(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        raise ValueError("Invalid operand combo: 7 or more can not be used")

output = []
pointer = 0
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer + 1]

    if opcode == 0:  # adv - Divide register A by a power of 2 (floor division is //)
        registers["A"] //= 2 ** get_combo_value(operand)

    elif opcode == 1:  # bxl - Bitwise XOR of B with a literal operand
        registers["B"] ^= operand

    elif opcode == 2:  # bst - Set B to combo operand value modulo 8
        registers["B"] = get_combo_value(operand) % 8

    elif opcode == 3:  # jnz - Jump to operand position if A is not zero
        if registers["A"] != 0:
            pointer = operand
            continue  # jump directly

    elif opcode == 4:  # bxc - Bitwise XOR of B with C
        registers["B"] ^= registers["C"]

    elif opcode == 5:  # out - Output the combo operand value modulo 8
        output.append(get_combo_value(operand) % 8)

    elif opcode == 6:  # bdv - Divide A by power of 2 and store in B (floor division again)
        registers["B"] = registers["A"] // 2 ** get_combo_value(operand)

    elif opcode == 7:  # cdv - Divide A by power of 2 and store in C (floor)
        registers["C"] = registers["A"] // 2 ** get_combo_value(operand)

    else:  # Error handling for unknown opcodes, should never come up.
        raise ValueError(f"Unknown opcode: {opcode}")

    pointer += 2  # Move to next instruction



string_output = []
for value in output:
    string_output.append(str(value))

#print(output)
print(",".join(string_output))

# n = number of instructions in the program 
# (can be longer then number of digits since it can jump)

# Time Complexity:
# Reading Input: O(n)
# Executing Instructions: O(n)
# Constructing Output: O(n)
# Total: O(n)

# Space Complexity:
# Storing the Program: O(n)
# Storing Registers: O(1)
# Storing Output List: O(n)
# Temporary Variables: O(1)
# Total: O(n)
