from collections import deque

class MazeSolverDFS:
    def __init__(self, grid, start, goal):
        """
        Initialize the solver.
        :param grid: 2D list representing the maze (0 = Path, 1 = Wall)
        :param start: Tuple (row, col) for start position
        :param goal: Tuple (row, col) for goal position
        """
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.stack = []        
        self.visited = set()   
        self.came_from = {}    

    def get_neighbors(self, node):
        """Returns valid neighbors (Up, Down, Left, Right)."""
        r, c = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        neighbors = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                neighbors.append((nr, nc))
        
        return neighbors

    def solve(self):
        """Executes the DFS algorithm."""
      
        self.stack.append(self.start)
        
        print("🔄 Running DFS...")
        
        while self.stack:
           
            current = self.stack.pop()

            if current == self.goal:
                print("✅ Goal Reached!")
                return self.reconstruct_path()

            
            if current not in self.visited:
                self.visited.add(current)

                
                for neighbor in self.get_neighbors(current):
                    if neighbor not in self.visited:
                        self.stack.append(neighbor)
                        self.came_from[neighbor] = current 
        
        print("❌ No path found.")
        return None

    def reconstruct_path(self):
        """Backtracks from goal to start to generate the path list."""
        path = []
        current = self.goal
        while current != self.start:
            path.append(current)
            current = self.came_from[current]
        path.append(self.start)
        path.reverse() 
        return path


def print_maze(grid, path=None):
    display_grid = [row[:] for row in grid]
    
    if path:
        for r, c in path:
            display_grid[r][c] = '*'
    
    print("\n--- Maze Visualization ---")
    for row in display_grid:
        line = ""
        for cell in row:
            if cell == 1: line += "██"  
            elif cell == '*': line += "👣"
            else: line += "░░"       
        print(line)
    print("-" * 20)

if __name__ == "__main__":
    maze_map = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]

    start_pos = (0, 0) 
    goal_pos = (4, 5)  

    solver = MazeSolverDFS(maze_map, start_pos, goal_pos)
    solution_path = solver.solve()

    if solution_path:
        print(f"📍 Path Length: {len(solution_path)}")
        print(f"👣 Path: {solution_path}")
        print_maze(maze_map, solution_path)