grid = [
    ["S", ".", ".", "."],
    ["X", "X", ".", "."],
    [".", ".", ".", "G"]
]

def find_position(grid, symbol):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == symbol:
                return (row, col)

print("Robot Environment:\n")

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()

start_position = find_position(grid, "S")
goal_position = find_position(grid, "G")

print("\nRobot Position:", start_position)
print("Goal Position:", goal_position)