import tkinter as tk
from tkinter import messagebox

# ---------------- Quiz Data ----------------
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Islamabad", "Lahore", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "Who developed the Python programming language?",
        "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which of the following is a Python data type?",
        "options": ["int", "real", "float32", "double"],
        "answer": "int"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".python", ".pyt", ".pt"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is mutable in Python?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "List"
    },
    {
        "question": "What symbol is used to comment in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "What is 5 ** 2 equal to in Python?",
        "options": ["10", "25", "7", "Error"],
        "answer": "25"
    },
    {
        "question": "Which built-in function returns the length of an object in Python?",
        "options": ["length()", "size()", "len()", "count()"],
        "answer": "len()"
    },
    {
        "question": "Which library is commonly used for data analysis in Python?",
        "options": ["numpy", "pandas", "math", "os"],
        "answer": "pandas"
    },
]

# ---------------- App Logic ----------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Quiz App by Umer")
        self.root.geometry("650x450")
        self.root.config(bg="#f0f6ff")

        self.question_index = 0
        self.score = 0

        self.title_label = tk.Label(root, text="📘 Python Quiz", font=("Helvetica", 18, "bold"), bg="#f0f6ff", fg="#004aad")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f6ff", wraplength=550, justify="center")
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.buttons = []

        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12),
                                 bg="#f0f6ff", anchor="w", justify="left")
            btn.pack(fill="x", padx=100, pady=5)
            self.buttons.append(btn)

        self.next_button = tk.Button(root, text="Next ➡️", command=self.next_question, bg="#004aad", fg="white", width=12)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question_data = questions[self.question_index]
        self.var.set(None)
        self.question_label.config(text=f"Q{self.question_index + 1}. {question_data['question']}")

        for i, option in enumerate(question_data["options"]):
            self.buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct = questions[self.question_index]["answer"]
        if selected == correct:
            self.score += 1

        self.question_index += 1

        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"🎉 Your Score: {self.score}/{len(questions)}")
        self.root.destroy()


# ---------------- Run App ----------------
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
