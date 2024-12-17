# Wannabe Quine Program
with open("Day-17-Challenge/input.txt", "r") as file:
    lines = file.readlines()

# Parse the program (no registers)
program = []
program_line = lines[4].split(":")[1].strip()
for value in program_line.split(","):
    program.append(int(value))

if program[-2:] != [3, 0]:
    raise AssertionError("Assumption 1: We assume program jumps only once at the end, otherwise we must branch and it becomes too complicated.")


# Combo operand evaluator
def get_combo_value(operand, registers):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    raise ValueError("Invalid operand combo: 7 or more can not be used")

#Recursive
def find_solution(target, answer):
    if not target:  # Base case: if the target is empty, return the answer
        return answer

    for t in range(8): # 8 branches for each recursion level
        # Initialize registers
        registers = {
            "A": answer << 3 | t, #bitwise shift same as dividing by 8. 
            # Assumption 2: We assume only time we write to A is when it says "0 3" meaning divide by 8. Otherwise change this part.
            "B": 0,
            "C": 0
        }
        output = None
        adv3_encountered = False

        # Instruction execution loop
        for pointer in range(0, len(program) - 2, 2):
            opcode = program[pointer]
            operand = program[pointer + 1]

            if opcode == 0:  # ADV - Division by 8 check
                if adv3_encountered:
                    # Assumption 3: We only have 1 ADV, otherwise multiple ways to get to solution
                    raise ValueError("Error: Program has multiple ADVs")

                if operand != 3:
                    raise ValueError("ADV encountered with invalid operand")

                adv3_encountered = True

            elif opcode == 1:  # BXL - Bitwise XOR with literal
                registers["B"] ^= operand
            elif opcode == 2:  # BST - Set B to combo operand % 8
                registers["B"] = get_combo_value(operand, registers) % 8
            elif opcode == 3:  # JNZ - Unexpected jump instruction
                raise AssertionError("JNZ found outside expected loop body")
            elif opcode == 4:  # BXC - Bitwise XOR between B and C
                registers["B"] ^= registers["C"]
            elif opcode == 5:  # OUT - Output combo operand % 8
                if output is not None:
                    raise ValueError("Program has multiple OUT instructions")
                output = get_combo_value(operand,registers) % 8
            elif opcode == 6:  # BDV - Divide A by combo operand
                registers["B"] = registers["A"] >> get_combo_value(operand, registers)
            elif opcode == 7:  # CDV - Divide C by combo operand
                registers["C"] = registers["A"] >> get_combo_value(operand, registers)
            else:
                raise AssertionError(f"Unknown opcode: {opcode}") # Should never raise

        # Recursively solve the remaining target if output matches from any of 8 branches
        if output == target[-1]:
            sub_result = find_solution(target[:-1], registers["A"])
            if sub_result is not None:
                return sub_result

    return None


solution = find_solution(program, 0)
print(solution)


# n = number of instructions in the program
# m = branching factor (8)
# d = recursion depth / number of digits we are expected to print (size of the "program")

# Time Complexity:
# Reading Input: O(n)
# Recursive Function: O(m^d * n)
# Total: O(m^d * n)

# Space Complexity:
# Storing the Program: O(n)
# Recursion Stack: O(d)
# Temporary Variables: O(1)
# Total: O(n + d)
