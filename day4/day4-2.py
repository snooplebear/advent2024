with open("day4_input.txt", "r") as day4_input:
	lines = day4_input.readlines()

# Convert grid into a list of strings (rows)
grid = lines
print(len(grid))

count = 0
# Scan through the grid to find all "X" positions
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'A':
            print(f"Found 'A' at position ({r}, {c})")
            if c + 1 < len(grid) and r + 1 < len(grid) and r - 1 > -1 and c - 1 > -1:
                if grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S' and grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S': # MAS MAS
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c})")
                    count+=1 
                if grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M' and grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M': # SAM SAM
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c})")
                    count+=1 
                elif grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M' and grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S': # SAM MAS
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c})")
                    count+=1
                elif grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S' and grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M': # MAS SAM
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c})")
                    count+=1             

print(count)

# r + 1 |  c + 1 bottom right
# r + 1 |  c - 1 bottom left
# r - 1 |  c + 1 top right
# r - 1 |  c - 1 top left
