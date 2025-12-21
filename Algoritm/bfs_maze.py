from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    queue = deque([start])
    parent = {start: None}
    visited = {start}

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] == 0 and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return None


maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = bfs(maze, start, goal)

if path:
    print("Find path", path)
else:
    print("Not")
