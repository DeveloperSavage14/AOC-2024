import re

# Read the input from the file
with open("Day3.txt", "r") as f:
    puzzle = f.read()

# Define the regular expression pattern for valid mul(X,Y) instructions
pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

# Find all matches in the puzzle input
matches = pattern.findall(puzzle)

# Calculate the sum of all valid multiplications
total_sum = 0
for match in matches:
    x, y = map(int, match)
    total_sum += x * y

print(f"Total sum of valid multiplications: {total_sum}")
