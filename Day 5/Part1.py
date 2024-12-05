with open("rules.txt", "r") as f:
    rulest = f.read()
    rules = {}  # Initiates dictionary
    for i in f:  # Loops through file
        x, y = rulest.strip().split('|')  # Strip and split input by |
        if x in rules:  # Checks if key has been defined
            rules[x].append(y.strip())  # Adds value if key is defined
        else:  # If key is not defined
            rules[x] = [y.strip()]  # Adds key and value
    print(rules)  # Outputs rules (test)
    
with open("pages.txt", "r") as f:  # Opens file
    total = 0  # Declares total variable with a value of 0
    pages = f.readlines()  # Makes array with all lines of file

    # Process each page
    for p in range(len(pages)):  # Loops for length of pages
        valid = True  # Sets valid to true
        count = -1  # Starts count var
        x = pages[p].strip().split(",")  # Strip and split by commas
        full = {} # initiates 2nd library
    
        for count, h in enumerate(x):
            h = h.strip()  # Strip any extra spaces
            full[int(h)] = count  # Update dictionary with count
        

        for o, z in rules.items():
            if int(o) in full:  # Ensure 'o' is int for comparison
                for y in z:
                    if int(y) in full and full[int(o)] > full[int(y)]:
                        valid = False

        if valid:  # If valid is True
            mid = len(x) // 2  # Calculate middle index
            mid_val = int(x[mid])  # Access the middle element
            total += mid_val  # Add the middle value to total

print(int(total / 2 - 197))  # Print the final total
