from collections import deque

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
    
def get_children(grid, position):
    children = []

    possible_moves = get_possible_moves(grid, position)

    for direction in possible_moves:
        child = move(position, direction)
        children.append(child)

    return children

def is_goal(position, goal):
    return position == goal


def bfs(grid, start, goal):

    queue = deque()

    visited = set()

    queue.append(start)

    visited.add(start)

    while queue:

        current = queue.popleft()

        print("\nExploring:", current)

        if is_goal(current, goal):
            print("\nGoal Found!")
            return True

        children = get_children(grid, current)

        for child in children:

            if child not in visited:

                visited.add(child)

                queue.append(child)

    print("\nGoal Not Found!")
    return False

start_position = find_position(grid, "S")
goal_position = find_position(grid, "G")

print("\nRobot Position:", start_position)
print("Goal Position:", goal_position)

possible_moves = get_possible_moves(grid, start_position)

print("Possible Moves:", possible_moves)

print("\nStarting BFS Search...")

bfs(grid, start_position, goal_position)