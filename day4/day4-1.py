with open("day4_input.txt", "r") as day4_input:
	lines = day4_input.readlines()

grid = lines
print(len(grid))

# Print the grid
print("Grid:")
for row in grid:
    print(row)

# Define the word to search for
word = "MAS"
word_length = len(word)

count = 0
# Scan through the grid to find all "X" positions
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'X':

            if c + word_length < len(grid):
                if grid[r][c+1] == 'M' and grid[r][c+2] == 'A' and grid[r][c+3] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the forward direction")
                    count+=1

            if c - word_length > -1:
                if grid[r][c-1] == 'M' and grid[r][c-2] == 'A' and grid[r][c-3] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the backward direction")
                    count+=1

            if r + word_length < len(grid):
                if grid[r+1][c] == 'M' and grid[r+2][c] == 'A' and grid[r+3][c] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the downward direction (top to bottom)")
                    count+=1

            if r - word_length > -1:
                if grid[r-1][c] == 'M' and grid[r-2][c] == 'A' and grid[r-3][c] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the upward direction (bottom to top)")
                    count+=1

            if c + word_length < len(grid) and r + word_length < len(grid):
                if grid[r+1][c+1] == 'M' and grid[r+2][c+2] == 'A' and grid[r+3][c+3] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the diagonal (top left to bottom right)")
                    count+=1
            if c - word_length > -1 and r - word_length > -1:
                if grid[r-1][c-1] == 'M' and grid[r-2][c-2] == 'A' and grid[r-3][c-3] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the diagonal (bottom right to top left)")
                    count+=1

            if r - word_length > -1 and c + word_length < len(grid):
                if grid[r-1][c+1] == 'M' and grid[r-2][c+2] == 'A' and grid[r-3][c+3] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the diagonal (bottom left to top right)")
                    count+=1

            if r + word_length < len(grid) and c - word_length > -1:
                if grid[r+1][c-1] == 'M' and grid[r+2][c-2] == 'A' and grid[r+3][c-3] == 'S':
                    print(f"Found 'MAS' starting from 'X' at position ({r}, {c}) in the diagonal (top right to bottom left)")
                    count+=1
            
            print(count)
