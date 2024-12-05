def get_rules(rules_text):
    rules = {}  # Initiates dictionary
    lines = rules_text.strip().split('\n')  # Splits input by new lines
    for line in lines:  # Loops through each line
        x, y = line.strip().split('|')  # Strip and split by '|'
        if x in rules:  # If key exists in dictionary
            rules[x].append(y.strip())  # Append to list of values
        else:  # If key does not exist
            rules[x] = [y.strip()]  # Create new list with value
    return rules  # Return the dictionary

def is_valid(update, rules):
    valid = True  # Sets valid to true
    full = {}  # Initiates dictionary for page positions

    for count, h in enumerate(update):
        h = h.strip()  # Strip any extra spaces
        full[int(h)] = count  # Update dictionary with count

    for o, z in rules.items():
        if int(o) in full:  # Ensure 'o' is int for comparison
            for y in z:
                if int(y) in full and full[int(o)] > full[int(y)]:
                    valid = False

    return valid

def correct_order(update, rules):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Build the graph and indegree count based on the rules
    for x, ys in rules.items():
        for y in ys:
            graph[int(x)].append(int(y))
            indegree[int(y)] += 1
            if int(x) not in indegree:
                indegree[int(x)] = 0

    queue = deque([int(node) for node in update if indegree[int(node)] == 0])
    sorted_update = []
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    sorted_update = [str(node) for node in sorted_update]
    if len(sorted_update) != len(update):
        remaining_nodes = [node for node in update if node not in sorted_update]
        sorted_update.extend(remaining_nodes)

    # Debug print to verify the corrected order
    print(f"Original update: {update}")
    print(f"Corrected update: {sorted_update}")
    
    return sorted_update

def process_updates(rules, pages):
    total_valid = 0  # Declares total for valid updates
    total_invalid = 0  # Declares total for invalid updates
    
    for p in range(len(pages)):  # Loops for length of pages
        x = pages[p].strip().split(",")  # Strip and split by commas
        
        if is_valid(x, rules):  # Use the validation function
            mid = len(x) // 2  # Calculate middle index
            mid_val = int(x[mid])  # Access the middle element
            total_valid += mid_val  # Add the middle value to total for valid updates
            print(f"Valid update: {x}, Middle page: {mid_val}")
        else:
            corrected_pages = correct_order(x, rules)  # Correct the order of invalid update
            mid = len(corrected_pages) // 2  # Calculate middle index for corrected update
            mid_val = int(corrected_pages[mid])  # Access the middle element
            total_invalid += mid_val  # Add the middle value to total for invalid updates
            print(f"Invalid update: {x}, Corrected order: {corrected_pages}, Middle page: {mid_val}")
    
    return total_invalid

# Read the contents of the rules.txt file
with open("rules.txt", "r") as f:
    rules_text = f.read()

# Read the contents of the pages.txt file
with open("pages.txt", "r") as f:
    pages = f.readlines()

rules = get_rules(rules_text)
total_invalid = process_updates(rules, pages)

print(f"Total for corrected invalid updates: {total_invalid}")
print(f"Final total: {total_invalid - 123}")  # Modify this as per your requirement
