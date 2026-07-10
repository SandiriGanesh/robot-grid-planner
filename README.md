# Robot Grid Planner using Breadth-First Search (BFS)

## Project Overview

This project implements a simple robot path planning algorithm using **Breadth-First Search (BFS)** in Python. The robot navigates through a 2D grid environment containing free cells, obstacles, a start position, and a goal position. The algorithm explores the grid level by level and finds the shortest path from the start to the goal while avoiding obstacles.

---

## Problem Statement

Design a robot navigation system that:

* Represents the environment as a 2D grid.
* Identifies the robot's starting position (`S`) and goal position (`G`).
* Detects valid movements while avoiding obstacles (`X`).
* Uses the **Breadth-First Search (BFS)** algorithm to explore the environment.
* Reconstructs and displays the shortest path from the start to the goal.

---

## Objectives

* Build a grid-based robot environment.
* Detect the robot and goal positions.
* Generate all valid neighboring positions.
* Implement Breadth-First Search (BFS).
* Avoid revisiting previously explored positions.
* Reconstruct and display the shortest path after reaching the goal.

---

## Features

* 2D grid environment representation.
* Obstacle detection.
* Valid movement generation (Up, Down, Left, Right).
* Breadth-First Search (BFS) implementation.
* Visited node tracking.
* Parent tracking for shortest path reconstruction.
* Displays the shortest path and total number of moves.

---

## Technologies Used

* Python 3.x
* collections.deque (for BFS queue)

---

## Project Structure

```text
robot-grid-planner/
│── main.py
│── README.md
```

---

## Grid Representation

```text
S . . .
X X . .
. . . G
```

Where:

* `S` = Start Position
* `G` = Goal Position
* `.` = Free Cell
* `X` = Obstacle

---

## Algorithm

The project follows these steps:

1. Create the robot environment.
2. Locate the start and goal positions.
3. Generate valid robot movements.
4. Generate neighboring positions.
5. Perform Breadth-First Search (BFS).
6. Track visited positions.
7. Reconstruct the shortest path.
8. Display the final path and total moves.

---

## Example Output

```text
Robot Environment:

S . . .
X X . .
. . . G

Robot Position: (0, 0)
Goal Position: (2, 3)

Starting BFS Search...

Exploring: (0, 0)
Exploring: (0, 1)
Exploring: (0, 2)
Exploring: (1, 2)
Exploring: (0, 3)
Exploring: (2, 2)
Exploring: (1, 3)
Exploring: (2, 1)
Exploring: (2, 3)

Goal Found!

Shortest Path:

Step 0: (0, 0)
Step 1: (0, 1)
Step 2: (0, 2)
Step 3: (1, 2)
Step 4: (2, 2)
Step 5: (2, 3)

Total Moves: 5
```

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd robot-grid-planner
```

3. Run the program.

```bash
python main.py
```

---

## Concepts Demonstrated

* Breadth-First Search (BFS)
* Robot Path Planning
* Graph Search
* Queue Data Structure
* State Space Exploration
* Parent Tracking
* Shortest Path Reconstruction

---

This project was developed as part of my robotics and autonomous systems learning journey to strengthen my understanding of search algorithms and robot path planning using Python.
