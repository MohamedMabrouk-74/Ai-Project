# 🕸️ AI Maze Pathfinder

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Algorithm](https://img.shields.io/badge/Algorithms-BFS%20%7C%20DFS%20%7C%20A*-purple)

## 🗺️ Introduction

This project is a visualization tool for **Artificial Intelligence Search Algorithms** applied to 2D Maze generation and solving. The agent's goal is to navigate from a **Start Node (S)** to a **Goal Node (G)** avoiding walls and obstacles.

It serves as a comparative study between **Uninformed (Blind)** and **Informed (Heuristic)** search strategies to understand pathfinding efficiency.

---

## ⚡ Key Features

* **Maze Visualization:** Real-time rendering of the search process (visited nodes vs. final path).
* **Comprehensive Algorithm Suite:** Implements 6 different search strategies.
* **Performance Metrics:** Calculates Path Length, Nodes Visited, and Execution Time.
* **Custom Maps:** Support for loading custom maze layouts from text files.

---

## 🛠️ Search Strategies Implemented

### 🔹 Uninformed Search (Blind)

#### 1. Breadth-First Search (BFS) 
* **Behavior:** Explores the maze layer by layer like a flood fill.
* **Pros:** Guarantees the **Shortest Path** in an unweighted grid.
* **Cons:** High memory usage; explores all directions equally, even those moving away from the goal.

#### 2. Depth-First Search (DFS) 
* **Behavior:** Explores a path as far as possible before backtracking.
* **Pros:** Low memory usage.
* **Cons:** **Not Optimal**. Can find extremely long, winding paths and get stuck exploring dead ends for a long time.

#### 3. Iterative Deepening Search (IDS)
* **Behavior:** Repeatedly runs DFS with increasing depth limits (Depth 1, Depth 2, ...).
* **Pros:** Finds the shortest path (like BFS) but with the memory efficiency of DFS.
* **Cons:** Re-generates states multiple times, though overhead is negligible in branching mazes.

#### 4. Uniform Cost Search (UCS)
* **Behavior:** Expands the node with the lowest path cost $g(n)$.
* **Pros:** Guarantees the optimal path even in **Weighted Mazes** (e.g., mud tiles cost more than grass).
* **Cons:** Identical to BFS in unweighted mazes.

---

### 🔹 Informed Search (Heuristic)

#### 5. Hill Climbing
* **Behavior:** A greedy algorithm that always moves to the neighbor closest to the goal.
* **Pros:** Extremely fast and requires almost no memory.
* **Cons:** **Not Complete**. It easily gets stuck in "Concave Walls" (Local Optima) where every move seems to take it further from the goal, failing to solve complex mazes.

#### 6. A* Search (A-Star) 
* **Behavior:** Uses $f(n) = g(n) + h(n)$ to select the most promising node.
* **Heuristics ($h(n)$):**
    * **Manhattan Distance:** $|x_1 - x_2| + |y_1 - y_2|$ (Best for grid movement).
    * **Euclidean Distance:** $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$ (Best for diagonal movement).
* **Pros:** The industry standard. Finds the shortest path much faster than BFS by "aiming" towards the goal.

---
## 📈 Expected Results

The following results demonstrate the performance differences between algorithms on a **20x20 Grid Maze** with moderate obstacles.

### 1. Performance Metrics Table

| Algorithm | Path Cost (Steps) | Nodes Expanded (Visits) | Execution Time (ms) | Status |
| :--- | :---: | :---: | :---: | :---: |
| **BFS** | **42** (Optimal) | 380 | 15ms | ✅ Solved |
| **DFS** | 98 (Long path) | **110** | **4ms** | ✅ Solved |
| **UCS** | **42** (Optimal) | 385 | 16ms | ✅ Solved |
| **A* (Manhattan)** | **42** (Optimal) | 125 | 6ms | ✅ Solved |
| **Hill Climbing** | N/A | 40 | 1ms | ❌ Stuck (Local Optima) |

> **Observation:** notice how **A\*** finds the same optimal path as BFS but visits significantly fewer nodes (125 vs 380), making it the most balanced choice.

---
