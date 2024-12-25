import os

base_directory = "Challenges"
# move them out after, just dont want a mess at first.
if not os.path.exists(base_directory):
    os.mkdir(base_directory)
for day in range(1, 26):
    day_folder = os.path.join(base_directory, f"Day-{day}-Challenge")
    if not os.path.exists(day_folder):
        os.mkdir(day_folder)
    # Create a challenge file in each folder
    challenge_file = os.path.join(day_folder, "input.txt")
    if not os.path.exists(challenge_file):
        with open(challenge_file, "w") as file:
            file.write(f"Day {day} Challenge")

    challenge_file = os.path.join(day_folder, f"day{day}p1.py")
    if not os.path.exists(challenge_file):
        with open(challenge_file, "w") as file:
            file.write(f"Day {day} Challenge")

    challenge_file = os.path.join(day_folder, f"day{day}p2.py")
    if not os.path.exists(challenge_file):
        with open(challenge_file, "w") as file:
            file.write(f"Day {day} Challenge")

    challenge_file = os.path.join(day_folder, f"ActualProblemHere.txt")
    if not os.path.exists(challenge_file):
        with open(challenge_file, "w") as file:
            file.write(f"https://adventofcode.com/2024/day/{day}")
