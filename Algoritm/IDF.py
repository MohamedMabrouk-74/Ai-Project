def get_neighbors(maze, node):
    x, y = node
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] != 1:
                neighbors.append((nx, ny))

    return neighbors

def dls(maze, node, goal, depth, visited, path):
    if node == goal:
        return path

    if depth == 0:
        return None

    visited.add(node)

    for neighbor in get_neighbors(maze, node):
        if neighbor not in visited:
            result = dls(
                maze,
                neighbor,
                goal,
                depth - 1,
                visited,
                path + [neighbor]
            )
            if result:
                return result

    visited.remove(node)
    return None


def ids(maze, start, goal):
    depth = 0
    while True:
        visited = set()
        result = dls(maze, start, goal, depth, visited, [start])
        if result:
            return result
        depth += 1


if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    path = ids(maze, start, goal)

    if path:
        print(path)
    else:
        print("No path found")
