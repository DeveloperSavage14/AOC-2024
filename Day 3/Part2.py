import re

# Read the input from the file
with open("Day3.txt", "r") as f:
    puzzle = f.read()

# Define the regular expression patterns
mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")

# Initialize the flag for enabling/disabling mul instructions
mul_enabled = True

# Initialize the total sum
total_sum = 0

# Split the input by lines and iterate through each line
lines = puzzle.split("\n")

for line in lines:
    if line.strip() == "":
        continue  # Skip empty lines

    # Process each part of the line to manage the flag and process mul instructions
    parts = re.split(r"(do\(\)|don't\(\))", line)
    
    for part in parts:
        if part.strip() == "":
            continue
        
        if dont_pattern.match(part):
            mul_enabled = False
            print("Found don't(): mul instructions are disabled.")
        elif do_pattern.match(part):
            mul_enabled = True
            print("Found do(): mul instructions are enabled.")
        elif mul_enabled:
            matches = mul_pattern.findall(part)
            for match in matches:
                x, y = map(int, match)
                print(f"Processing mul({x},{y}): {x} * {y} = {x * y}")
                total_sum += x * y

print(f"Total sum of valid multiplications with conditions: {total_sum}")


