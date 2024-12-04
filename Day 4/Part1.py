with open("Day4.txt", "r") as f:
    
    contents = f.read()
    lines = contents.split("\n")
    grid = [
        list(line)
        for line in lines
        if line
    ]
    width = len(grid[0])
    height = len(grid)
    count = 0
    for x in range(height):
        for i in range(len(grid[x])):
            if grid[x][i] == "X":
                if i >= 3:
                    if grid[x][i-1] == "M":
                        if grid[x][i-2] == "A":
                            if grid[x][i-3] == "S":
                                count += 1
                if i <= width - 4:
                    if grid[x][i+1] == "M":
                        if grid[x][i+2] == "A":
                            if grid[x][i+3] == "S":
                                count += 1
                if x >= 3:
                    if grid[x-1][i] == "M":
                        if grid[x-2][i] == "A":
                            if grid[x-3][i] == "S":
                                count += 1
                if x <= height - 4:
                    if grid[x+1][i] == "M":
                        if grid[x+2][i] == "A":
                            if grid[x+3][i] == "S":
                                count += 1
                if x >= 3 and i <= width - 4:
                    if grid[x-1][i+1] == "M":
                        if grid[x-2][i+2] == "A":
                            if grid[x-3][i+3] == "S":
                               count += 1
                if x >= 3 and i >= 3:
                    if grid[x-1][i-1] == "M":
                        if grid[x-2][i-2] == "A":
                            if grid[x-3][i-3] == "S":
                               count += 1
                if x <= height - 4 and i <= width - 4:
                    if grid[x+1][i+1] == "M":
                        if grid[x+2][i+2] == "A":
                            if grid[x+3][i+3] == "S":
                               count += 1
                if x <= height - 4 and i >= 3:
                    if grid[x+1][i-1] == "M":
                        if grid[x+2][i-2] == "A":
                            if grid[x+3][i-3] == "S":
                               count += 1

    print(count)
                
                    
                
    
    
