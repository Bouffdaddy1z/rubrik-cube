import tkinter as tk
from tkinter import messagebox

class RubiksCubeSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Solver")
        
        self.steps = {
            "Initialize Rubik's Cube": "Start by ensuring the cube is properly scrambled and ready to be solved systematically.",
            "Solve First Layer": "Align the white edges, match center colors, and position corners correctly to form a complete white layer.",
            "Solve Second Layer": "Find and insert the correct edge pieces into the second layer without disturbing the first layer.",
            "Solve Yellow Cross": "Orient the yellow edges correctly to form a cross on the top face of the cube.",
            "Solve Yellow Corners": "Position and orient the yellow corners correctly to complete the yellow face.",
            "Position Yellow Corners": "Move yellow corners into their correct locations while maintaining the yellow cross.",
            "Orient Yellow Corners": "Rotate the yellow corners correctly to align all colors.",
            "Finish Cube": "Position and orient the remaining edges to fully solve the Rubik's Cube.",
        }

        self.label = tk.Label(root, text="Welcome to the Rubik's Cube Solver!", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.step_label = tk.Label(root, text="Select a step to get instructions:")
        self.step_label.pack()
        
        self.step_listbox = tk.Listbox(root, height=len(self.steps))
        for step in self.steps.keys():
            self.step_listbox.insert(tk.END, step)
        self.step_listbox.pack(pady=5)
        
        self.get_step_button = tk.Button(root, text="Get Step", command=self.get_step)
        self.get_step_button.pack(pady=5)
        
        self.solve_button = tk.Button(root, text="Start Solving", command=self.solve)
        self.solve_button.pack(pady=5)
        
        self.close_button = tk.Button(root, text="Close", command=root.quit)
        self.close_button.pack(pady=5)
        
    def get_step(self):
        """Displays the instruction for the selected step."""
        selected_index = self.step_listbox.curselection()
        if selected_index:
            step_name = self.step_listbox.get(selected_index)
            messagebox.showinfo("Step Instruction", self.steps[step_name])
        else:
            messagebox.showerror("Error", "Please select a step from the list.")
    
    def solve(self):
        """Guides the user through solving the cube step by step interactively."""
        for step, instruction in self.steps.items():
            messagebox.showinfo("Solving Step", f"{step}:\n{instruction}")
        messagebox.showinfo("Congratulations!", "You have solved the Rubik's Cube!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RubiksCubeSolverApp(root)
    root.mainloop()
