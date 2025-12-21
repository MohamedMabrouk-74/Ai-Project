import heapq

GRID = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

START = (0, 0)
GOAL = (4, 4)

def ucs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    parent = {}

    while pq:
        cost, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], cost

        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + 1, neighbor))
                    parent[neighbor] = current

    return None, float("inf")

path, cost = ucs(GRID, START, GOAL)

print("Path found:", path)
print("Path cost:", cost)
