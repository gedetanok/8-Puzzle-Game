# 🧩 8-Puzzle Solver with GUI using BFS & DFS (State-Space Tree)

This is a Python program that solves the classic **8-Puzzle problem** using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. It includes a graphical interface built with **Tkinter**, and visualizes the solution path step by step using a slider.

---

## 📌 Features

- Solve 8-Puzzle using **BFS** (optimal) or **DFS** (non-optimal).
- State-space tree built **explicitly** using `Node` objects.
- **Manual implementation of Queue** to reinforce algorithm understanding.
- Interactive GUI with:
  - Puzzle canvas
  - Algorithm selector (BFS / DFS)
  - Step-by-step slider of the solution path
- Pop-up message if no solution is found.

---

## 📷 Preview

![8-Puzzle GUI Screenshot](https://via.placeholder.com/600x300?text=8-Puzzle+GUI+Screenshot)

---

## 🧠 How it Works

- The puzzle board is represented as a tuple of 9 numbers (0 = empty space).
- The program builds a **state-space tree** by generating all possible valid moves.
- BFS explores level by level, ensuring shortest path.
- DFS explores depth-first with a configurable max depth.
- When the goal state is reached, the path is reconstructed and visualized.

---

## 🛠 Technologies Used

- Python 3
- Tkinter (built-in GUI library)
- NumPy (for grid reshaping)

---

## ▶️ How to Run

1. **Install Python** (if not installed):

https://www.python.org/downloads/

2. **Clone this repository:**
```bash
git clone https://github.com/gedetanok/8-Puzzle-Game.git
cd 8-Puzzle-Game
```

3. Run the program:

```bash
python main.py
```

🧑‍💻 Author
Nama: Gede Tanok Arta Wijaya  
NIM: 2315101018  
GitHub: https://github.com/gedetanok

