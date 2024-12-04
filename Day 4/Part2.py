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
            if grid[x][i] == "M":
                if x <= height - 3 and i >= 2:
                    if grid[x+1][i-1] == "A":
                        if grid[x+2][i-2] == "S":
                            if grid[x][i-2] == "M":
                                if grid[x+2][i] == "S":
                                    count += 1
                            if grid[x][i-2] == "S":
                                if grid[x+2][i] == "M":
                                    count += 1

                if x >= 2 and i >= 2:
                    if grid[x-1][i-1] == "A":
                        if grid[x-2][i-2] == "S":
                            if grid[x][i-2] == "M":
                                if grid[x-2][i] == "S":
                                    count += 1
                            if grid[x][i-2] == "S":
                                if grid[x-2][i] == "M":
                                    count += 1

                if x <= height - 3 and i <= width - 3:
                    if grid[x+1][i+1] == "A":
                        if grid[x+2][i+2] == "S":
                            if grid[x][i+2] == "M":
                                if grid[x+2][i] == "S":
                                    count += 1
                            if grid[x][i+2] == "S":
                                if grid[x+2][i] == "M":
                                    count += 1

                if x >= 2 and i <= width - 3:
                    if grid[x-1][i+1] == "A":
                        if grid[x-2][i+2] == "S":
                            if grid[x][i+2] == "M":
                                if grid[x-2][i] == "S":
                                    count += 1
                            if grid[x][i+2] == "S":
                                if grid[x-2][i] == "M":
                                    count += 1

    count = count // 2
    print(count)
