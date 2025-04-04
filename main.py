import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

# Queue class
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def is_empty(self):
        return len(self.data) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        
# Node Class
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.depth = 0 if parent is None else parent.depth + 1

INITIAL_STATE = (2, 8, 3,
                 1, 6, 4,
                 7, 0, 5)

GOAL_STATE = (1, 2, 3,
              8, 0, 4,
              7, 6, 5)

# fungsi untuk mendapatkan neighbors yang possible
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    moves = []

    if row > 0:
        moves.append((-1, 0))
    if row < 2:
        moves.append((1, 0))
    if col > 0:
        moves.append((0, -1))
    if col < 2: 
        moves.append((0, 1))

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        new_index = new_row * 3 + new_col
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        neighbors.append(tuple(new_state))

    return neighbors

# BFS with state-space tree
def bfs(initial, goal):
    root = Node(initial)
    queue = Queue()
    queue.enqueue(root)
    visited = {initial}
    solution_node = None

    while not queue.is_empty():
        current_node = queue.dequeue()
        
        if current_node.state == goal:
            solution_node = current_node
            break

        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state not in visited:
                child_node = Node(neighbor_state, parent=current_node)
                current_node.children.append(child_node)
                queue.enqueue(child_node)
                visited.add(neighbor_state)

    # rekontruksi jalur solusi dari goal ke rooot
    path = []
    if solution_node:
        current = solution_node
        while current:
            path.append(current)
            current = current.parent
        
        path.reverse()
    return path

# DFS with state space tree
def dfs(initial,  goal, max_depth=50):
    root = Node(initial)
    stack = [root]
    visited = {initial}
    solution_node = None

    while stack:
        current_node = stack.pop()

        if current_node.state == goal:
            solution_node = current_node
            break

        if current_node.depth < max_depth:
            for neighbor_state in get_neighbors(current_node.state):
                if neighbor_state not in visited:
                    child_node = Node(neighbor_state, parent=current_node)
                    current_node.children.append(child_node)
                    stack.append(child_node)
                    visited.add(neighbor_state)

    # rekontruksi jalur solusi
    path = []
    if solution_node:
        current = solution_node
        while current:
            path.append(current)
            current = current.parent
        path.reverse()

    return path

# THE GUIIII!!!!!
class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        root.title('8-Puzzle Solver (State-Space Tree)')
        
        # pilihan algorithma
        self.algorithm_variable = tk.StringVar(value='BFS')

        algorithm_frame = ttk.LabelFrame(root, text='Pilih Algoritma')
        algorithm_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        ttk.Radiobutton(algorithm_frame, 
                        text='BFS', 
                        variable=self.algorithm_variable,
                        value='BFS').grid(row=0,
                                          column=0,
                                          padx=5,
                                          pady=5)
        
        ttk.Radiobutton(algorithm_frame, 
                        text='DFS', 
                        variable=self.algorithm_variable,
                        value='DFS').grid(row=0,
                                          column=1,
                                          padx=5,
                                          pady=5)

        # tombol solve
        self.solve_button = ttk.Button(root, text='Solve', command=self.solve_puzzle)
        self.solve_button.grid(row=0, column=1, padx=10, pady=10)

        # canvas papan puzzle
        self.canvas = tk.Canvas(root, width=300, height=300, background='white')
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.draw_board(INITIAL_STATE)

        # slider untuk menampilkan branch solusi
        self.solution_slider = ttk.Scale(root, from_=0, to=0, orient='horizontal', command=self.update_board)
        self.solution_slider.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # label untuk menampilkan step
        self.step_label = ttk.Label(root, text='Step: 0')
        self.step_label.grid(row=3, column=0, columnspan=2)

        self.solution_path = []

    def draw_board(self, state):
        self.canvas.delete('all')
        board = np.array(state).reshape(3, 3)
        cell_size = 100

        for i in range(3):
            for j in range(3):
                x0 = j * cell_size
                y0 = i * cell_size
                x1 = x0 + cell_size
                y1 = y0 + cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='lightblue', outline='black')
                num = board[i, j]
                if num != 0:
                    self.canvas.create_text(x0 + cell_size/2, 
                                            y0 + cell_size/2, 
                                            text=str(num), 
                                            font=('Arial', 24))
                    
    def update_board(self, event=None):
        if self.solution_path:
            index = int(float(self.solution_slider.get()))
            state = self.solution_path[index]
            self.draw_board(state)
            self.step_label.config(text=f'Step : {index + 1} / {len(self.solution_path)}')
        
    def solve_puzzle(self):
        algorithm = self.algorithm_variable.get()
        if algorithm == 'BFS':
            node_path = bfs(INITIAL_STATE, GOAL_STATE)
        else :
            node_path = dfs(INITIAL_STATE, GOAL_STATE, 50)

        if not node_path:
            messagebox.showinfo("Info", "Solusi tidak ditemukan dari posisi awal ke goal.")
            return

        # ambil semua node path untuk slider
        self.solution_path = [node.state for node in node_path]
        self.solution_slider.config(from_=0, to=len(self.solution_path) - 1)
        self.solution_slider.set(0)
        self.update_board()

        print(f'Solution path : ')
        for node in node_path:
            print(node.state)

# Run semuanya
if __name__ == '__main__':
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()