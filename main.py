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

def get_possible_moves(grid, position):
    row, col = position

    moves = []

    # Up
    if row > 0 and grid[row - 1][col] != "X":
        moves.append("up")

    # Down
    if row < len(grid) - 1 and grid[row + 1][col] != "X":
        moves.append("down")

    # Left
    if col > 0 and grid[row][col - 1] != "X":
        moves.append("left")

    # Right
    if col < len(grid[0]) - 1 and grid[row][col + 1] != "X":
        moves.append("right")

    return moves

def move(position, direction):
    row, col = position

    if direction == "up":
        return (row - 1, col)

    elif direction == "down":
        return (row + 1, col)

    elif direction == "left":
        return (row, col - 1)

    elif direction == "right":
        return (row, col + 1)

start_position = find_position(grid, "S")
goal_position = find_position(grid, "G")

print("\nRobot Position:", start_position)
print("Goal Position:", goal_position)

possible_moves = get_possible_moves(grid, start_position)

print("Possible Moves:", possible_moves)

for direction in possible_moves:

    new_position = move(start_position, direction)

    print(f"\nMove: {direction}")
    print("New Position:", new_position)