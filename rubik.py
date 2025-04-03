import tkinter as tk
from tkinter import messagebox

class RubiksCubeSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Solver")
        self.steps = [
            "Step 1: Solve the White Cross",
            "Step 2: Solve the White Corners",
            "Step 3: Solve the Middle Layer Edges",
            "Step 4: Solve the Yellow Cross",
            "Step 5: Solve the Yellow Corners",
            "Step 6: Solve the Final Layer Edges"
        ]
        
        self.label = tk.Label(root, text="Welcome to the Rubik's Cube Solver!", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.step_label = tk.Label(root, text="Select a step to get instructions or start solving:")
        self.step_label.pack()
        
        self.step_var = tk.StringVar()
        self.step_entry = tk.Entry(root, textvariable=self.step_var)
        self.step_entry.pack()
        
        self.get_step_button = tk.Button(root, text="Get Step", command=self.get_step)
        self.get_step_button.pack(pady=5)
        
        self.solve_button = tk.Button(root, text="Start Solving", command=self.solve)
        self.solve_button.pack(pady=5)
        
    def get_step(self):
        """Displays the instruction for the given step number."""
        step_number = self.step_var.get()
        if step_number.isdigit():
            step_number = int(step_number)
            if 1 <= step_number <= len(self.steps):
                messagebox.showinfo("Step Instruction", self.steps[step_number - 1])
            else:
                messagebox.showerror("Error", "Invalid step number. Enter a number between 1 and 6.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    def solve(self):
        """Guides the user through solving the cube step by step interactively."""
        for step in self.steps:
            messagebox.showinfo("Solving Step", step)
        messagebox.showinfo("Congratulations!", "You have solved the Rubik's Cube!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RubiksCubeSolverApp(root)
    root.mainloop()
