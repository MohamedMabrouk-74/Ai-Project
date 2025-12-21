GRID = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

START = (0, 0)
GOAL = (4, 4)

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def hill_climbing(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    current = start
    path = [current]
    visited = set([current])

    while current != goal:
        x, y = current
        neighbors = []

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    neighbors.append(neighbor)

        if not neighbors:
            return None, float("inf")

        next_node = min(neighbors, key=lambda n: heuristic(n, goal))

        if heuristic(next_node, goal) >= heuristic(current, goal):
            return None, float("inf")

        current = next_node
        visited.add(current)
        path.append(current)

    return path, len(path) - 1

path, cost = hill_climbing(GRID, START, GOAL)
if path:
    print("Path found:", path)
    print("Path cost:", cost)
else:
    print("No path found")
