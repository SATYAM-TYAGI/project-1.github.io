import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

questions = [
    {
        "question": "What will be the output of the following code?\n\nx = [1, 2, 3]\nx[3] = 4\nprint(x)",
        "options": ["[1, 2, 3, 4]", "IndexError", "[1, 2, 4]", "SyntaxError"],
        "answer": "IndexError"
    },
    {
        "question": "How can you debug a 'TypeError' in Python?",
        "options": ["Check for invalid operations between incompatible data types", "Ignore the error and continue", "Use print statements only", "Restart the Python interpreter"],
        "answer": "Check for invalid operations between incompatible data types"
    },
    {
        "question": "Given the code snippet below, what is the issue?\n\ndef foo():\n    x = 10\n    return x + y\n\nfoo()",
        "options": ["SyntaxError", "IndentationError", "NameError", "TypeError"],
        "answer": "NameError"
    },
    {
        "question": "Which of the following statements is correct for debugging in Python?",
        "options": ["Using print statements is the best way to debug", "The pdb module can be used to set breakpoints", "Ignoring exceptions will help debug faster", "Using the time module is essential for debugging"],
        "answer": "The pdb module can be used to set breakpoints"
    },
    {
        "question": "Consider the following code. What will be the output?\n\nmy_dict = {'a': 1, 'b': 2}\nprint(my_dict['c'])",
        "options": ["KeyError", "None", "0", "SyntaxError"],
        "answer": "KeyError"
    },
    {
        "question": "In the code snippet below, identify the error type:\n\nfor i in range(5):\n    if i == 2\n        print(i)",
        "options": ["SyntaxError", "IndentationError", "TypeError", "ValueError"],
        "answer": "SyntaxError"
    },
    {
        "question": "What will be the output of the following code?\n\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    result = 'Infinity'\nprint(result)",
        "options": ["0", "Infinity", "ZeroDivisionError", "SyntaxError"],
        "answer": "Infinity"
    },
    {
        "question": "How would you handle an AttributeError in Python?",
        "options": ["Check if the object has the attribute before accessing it", "Use a try-except block", "Ensure the object is of the correct type", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What will be the output of the following code?\n\nx = '10'\ny = 5\nprint(x + y)",
        "options": ["105", "15", "TypeError", "SyntaxError"],
        "answer": "TypeError"
    },
    {
        "question": "What can you use to understand the state of your program at a specific point while debugging?",
        "options": ["Breakpoints", "Reading documentation", "Googling the error", "Stack overflow"],
        "answer": "Breakpoints"
    }
]

class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("1000x800")  # Increased window size
        self.score = 0
        self.current_question = 0
        self.create_background()
        self.create_widgets()
    
    def create_background(self):
        self.canvas = tk.Canvas(self.root, width=1000, height=800)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = ImageTk.PhotoImage(Image.open("quiz2.jpg"))
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Python Debugging Quiz", font=("Helvetica", 24, "bold"), bg="lightblue")
        self.title_window = self.canvas.create_window(500, 40, anchor="center", window=self.title_label)
        
        self.remaining_label = tk.Label(self.root, font=("Helvetica", 12), bg="lightblue")
        self.remaining_window = self.canvas.create_window(500, 80, anchor="center", window=self.remaining_label)
        
        self.update_question_widgets()
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 14), bg="green", fg="white")
        self.submit_window = self.canvas.create_window(500, 700, anchor="center", window=self.submit_button)
    
    def update_question_widgets(self):
        question_text = f"Question {self.current_question + 1}: {questions[self.current_question]['question']}"
        remaining_text = f"Questions left: {len(questions) - self.current_question - 1}"
        
        self.question_label = tk.Label(self.root, text=question_text, font=("Helvetica", 16), bg="white", wraplength=800, justify="center")
        self.question_window = self.canvas.create_window(500, 200, anchor="center", window=self.question_label)
        
        self.remaining_label.config(text=remaining_text)
        
        self.options = tk.StringVar(value="")
        self.options_frame = tk.Frame(self.root, bg="white")
        self.options_window = self.canvas.create_window(500, 450, anchor="center", window=self.options_frame)
        
        for option in questions[self.current_question]["options"]:
            tk.Radiobutton(self.options_frame, text=option, variable=self.options, value=option, font=("Helvetica", 14), bg="lightblue", indicatoron=0, width=50, height=3, relief="ridge", bd=2).pack(anchor="center", pady=5)
    
    def check_answer(self):
        if self.options.get() == questions[self.current_question]["answer"]:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question == len(questions):
            messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}")
            self.root.quit()
        else:
            self.update_question()
    
    def update_question(self):
        self.question_label.destroy()
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.update_question_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApplication(root)
    root.mainloop()
