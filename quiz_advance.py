import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # pip install pillow
import random
from datetime import datetime
import os

# -------------------- QUIZ DATA: 6 topics x 20 MCQs each --------------------
topics = {
    "Basics": [
        {"question": "Which keyword is used to create a variable in Python?",
         "options": ["var", "let", "no keyword, just name", "declare"],
         "answer": "no keyword, just name"},
        {"question": "What is the output type of 5/2 in Python 3?",
         "options": ["int", "float", "str", "complex"],
         "answer": "float"},
        {"question": "Which function prints to the console?",
         "options": ["echo()", "print()", "console.log()", "puts()"],
         "answer": "print()"},
        {"question": "How do you start a comment in Python?",
         "options": ["//", "#", "/*", "<!--"],
         "answer": "#"},
        {"question": "Which operator is used for exponentiation?",
         "options": ["^", "**", "pow()", "exp()"],
         "answer": "**"},
        {"question": "What will 'Hello' + 'World' produce?",
         "options": ["Hello World", "HelloWorld", "Error", "Hello+World"],
         "answer": "HelloWorld"},
        {"question": "Which of these is a valid variable name?",
         "options": ["1name", "user_name", "user-name", "user name"],
         "answer": "user_name"},
        {"question": "What built-in type represents text?",
         "options": ["int", "float", "str", "bool"],
         "answer": "str"},
        {"question": "What does '=' do in Python?",
         "options": ["Equality test", "Assignment", "Comparison", "None"],
         "answer": "Assignment"},
        {"question": "What symbol is used for floor division?",
         "options": ["/", "//", "%", "div"],
         "answer": "//"},
        {"question": "Which boolean values exist in Python?",
         "options": ["yes/no", "true/false", "True/False", "1/0"],
         "answer": "True/False"},
        {"question": "How to get type of a variable?",
         "options": ["typeof(x)", "type(x)", "gettype(x)", "what(x)"],
         "answer": "type(x)"},
        {"question": "Which of these is immutable?",
         "options": ["list", "dict", "tuple", "set"],
         "answer": "tuple"},
        {"question": "What does len([1,2,3]) return?",
         "options": ["0", "2", "3", "Error"],
         "answer": "3"},
        {"question": "Which statement is used to exit a loop immediately?",
         "options": ["stop", "end", "break", "exit"],
         "answer": "break"},
        {"question": "Which is the correct way to import a module?",
         "options": ["include math", "using math", "import math", "require math"],
         "answer": "import math"},
        {"question": "What is the index of first element in a list?",
         "options": ["0", "1", "-1", "Depends"],
         "answer": "0"},
        {"question": "Which keyword defines a function?",
         "options": ["function", "def", "fun", "lambda"],
         "answer": "def"},
        {"question": "What will bool('') evaluate to?",
         "options": ["True", "False", "Error", "None"],
         "answer": "False"},
        {"question": "Which of these converts a value to integer?",
         "options": ["int()", "integer()", "to_int()", "cast_int()"],
         "answer": "int()"},
    ],
    "Data Types": [
        {"question": "Which type stores key:value pairs?",
         "options": ["list", "tuple", "dict", "set"],
         "answer": "dict"},
        {"question": "Which type is unordered and unique collection?",
         "options": ["list", "set", "tuple", "str"],
         "answer": "set"},
        {"question": "Which method adds an item to end of list?",
         "options": ["add()", "append()", "push()", "insert()"],
         "answer": "append()"},
        {"question": "How to get keys of a dict d?",
         "options": ["d.keys()", "keys(d)", "d.getkeys()", "getkeys(d)"],
         "answer": "d.keys()"},
        {"question": "Which type allows duplicate elements?",
         "options": ["set", "dict", "list", "frozenset"],
         "answer": "list"},
        {"question": "Which method removes and returns last item of list?",
         "options": ["pop()", "remove()", "del()", "discard()"],
         "answer": "pop()"},
        {"question": "What is a tuple?",
         "options": ["Mutable list", "Immutable list", "Dictionary", "Function"],
         "answer": "Immutable list"},
        {"question": "How to create an empty set?",
         "options": ["{}", "set()", "[]", "empty()"],
         "answer": "set()"},
        {"question": "Which of these converts string to list of characters?",
         "options": ["list(s)", "chars(s)", "splitchars(s)", "s.split()"],
         "answer": "list(s)"},
        {"question": "What does .items() on dict return?",
         "options": ["list of keys", "list of values", "pairs of (key,value)", "iterator of keys"],
         "answer": "pairs of (key,value)"},
        {"question": "Which type is best for ordered mapping (Python 3.7+)?",
         "options": ["list", "dict", "set", "tuple"],
         "answer": "dict"},
        {"question": "Which is immutable: string or list?",
         "options": ["string", "list", "both", "none"],
         "answer": "string"},
        {"question": "Which method returns index of first matching item in list?",
         "options": ["find()", "index()", "locate()", "search()"],
         "answer": "index()"},
        {"question": "Which method merges two lists a and b in-place?",
         "options": ["a.concat(b)", "a.extend(b)", "a + b", "append(b)"],
         "answer": "a.extend(b)"},
        {"question": "Which literal creates bytes in Python?",
         "options": ["b'abc'", "'abc'", "u'abc'", "r'abc'"],
         "answer": "b'abc'"},
        {"question": "What type does range() produce?",
         "options": ["list", "range", "iterator", "tuple"],
         "answer": "range"},
        {"question": "Which method removes item by value from list?",
         "options": ["delete()", "remove()", "discard()", "pop(value)"],
         "answer": "remove()"},
        {"question": "Which is mutable: dict or tuple?",
         "options": ["dict", "tuple", "both", "none"],
         "answer": "dict"},
        {"question": "How to copy a list shallowly?",
         "options": ["list.copy()", "copy(list)", "list[:]","All of the above"],
         "answer": "All of the above"},
        {"question": "Which type cannot be used as dict key?",
         "options": ["tuple", "int", "list", "str"],
         "answer": "list"},
    ],
    "Control Flow": [
        {"question": "Which statement checks a condition?",
         "options": ["for", "if", "while", "switch"],
         "answer": "if"},
        {"question": "Which loop runs a fixed number of times typically?",
         "options": ["while", "for", "do-while", "repeat"],
         "answer": "for"},
        {"question": "How to skip current iteration?",
         "options": ["skip", "continue", "pass", "break"],
         "answer": "continue"},
        {"question": "Which statement exits a loop?",
         "options": ["stop", "break", "exit", "return"],
         "answer": "break"},
        {"question": "What does 'else' after a loop run when?",
         "options": ["Always after loop", "Only if loop not terminated by break", "Only if loop used for", "Never"],
         "answer": "Only if loop not terminated by break"},
        {"question": "Which keyword creates anonymous function?",
         "options": ["anon", "lambda", "def", "func"],
         "answer": "lambda"},
        {"question": "How to handle exceptions?",
         "options": ["try/except", "try/catch", "begin/rescue", "handle/except"],
         "answer": "try/except"},
        {"question": "Which built-in raises an exception intentionally?",
         "options": ["raise", "throw", "error", "abort"],
         "answer": "raise"},
        {"question": "What is 'pass' used for?",
         "options": ["Do nothing placeholder", "Break loop", "Continue loop", "Return value"],
         "answer": "Do nothing placeholder"},
        {"question": "Which comparison operator checks equality?",
         "options": ["=", "==", "is", "equals()"],
         "answer": "=="},
        {"question": "Which operator checks identity (same object)?",
         "options": ["==", "is", "equals", "==="],
         "answer": "is"},
        {"question": "How to run code while condition is true?",
         "options": ["for", "while", "loop", "repeat"],
         "answer": "while"},
        {"question": "What does 'elif' mean?",
         "options": ["else if", "else once", "else loop", "end if"],
         "answer": "else if"},
        {"question": "Which statement returns from function?",
         "options": ["stop", "break", "return", "exit"],
         "answer": "return"},
        {"question": "Which of these is valid conditional expression?",
         "options": ["x if cond else y", "if cond then x else y", "cond ? x : y", "cond => x"],
         "answer": "x if cond else y"},
        {"question": "What happens if exception not handled?",
         "options": ["Program continues", "Traceback and stops", "Ignored", "Default handler fixes it"],
         "answer": "Traceback and stops"},
        {"question": "Which loop can have an else clause?",
         "options": ["for only", "while only", "for and while", "none"],
         "answer": "for and while"},
        {"question": "Which keyword can be used to define a generator function?",
         "options": ["yield", "return", "generate", "yieldfrom"],
         "answer": "yield"},
        {"question": "How do you check multiple conditions (AND)?",
         "options": ["&&", "and", "&", "AND"],
         "answer": "and"},
        {"question": "Which is correct to catch all exceptions?",
         "options": ["except:", "except Exception:", "except BaseException:", "except *:"],
         "answer": "except Exception:"},
    ],
    "Functions": [
        {"question": "Which keyword defines a function?",
         "options": ["func", "def", "function", "lambda"],
         "answer": "def"},
        {"question": "How do you create an anonymous function?",
         "options": ["def", "lambda", "anon", "function"],
         "answer": "lambda"},
        {"question": "Which statement exits a function returning a value?",
         "options": ["break", "return", "exit", "stop"],
         "answer": "return"},
        {"question": "How to document a function briefly inside the function?",
         "options": ["comment", "docstring", "note", "describe"],
         "answer": "docstring"},
        {"question": "How do you pass variable number of positional args?",
         "options": ["*args", "**kwargs", "*kwargs", "args[]"],
         "answer": "*args"},
        {"question": "How do you pass variable number of keyword args?",
         "options": ["*args", "**kwargs", "args", "kwargs"],
         "answer": "**kwargs"},
        {"question": "What does @staticmethod decorator do?",
         "options": ["Creates staticmethod", "Creates classmethod", "Runs function at import", "Nothing"],
         "answer": "Creates staticmethod"},
        {"question": "What does @classmethod decorator do?",
         "options": ["Pass class as first arg", "Pass instance as first arg", "Make function static", "None"],
         "answer": "Pass class as first arg"},
        {"question": "Which builtin returns function object attributes like __name__?",
         "options": ["attrs()", "dir()", "help()", "inspect()"],
         "answer": "dir()"},
        {"question": "Which module helps inspect functions (signature, source)?",
         "options": ["inspect", "functools", "itertools", "types"],
         "answer": "inspect"},
        {"question": "How to wrap a function preserving metadata?",
         "options": ["use wrapper()", "use functools.wraps", "use decorator", "do nothing"],
         "answer": "use functools.wraps"},
        {"question": "Which return type can a function have in Python?",
         "options": ["Only int", "Only str", "Any type", "None only"],
         "answer": "Any type"},
        {"question": "Can functions be assigned to variables?",
         "options": ["Yes", "No", "Only methods", "Only lambdas"],
         "answer": "Yes"},
        {"question": "What is recursion?",
         "options": ["Function calling itself", "Function returning value", "Loop inside function", "Lambda use"],
         "answer": "Function calling itself"},
        {"question": "Which statement stops execution of current function?",
         "options": ["return", "break", "stop", "exit"],
         "answer": "return"},
        {"question": "What is a closure?",
         "options": ["Function with inner state bound to outer scope", "Decorator", "Lambda", "Generator"],
         "answer": "Function with inner state bound to outer scope"},
        {"question": "What is the purpose of 'nonlocal'?",
         "options": ["Access module var", "Access outer non-global var", "Same as global", "No use"],
         "answer": "Access outer non-global var"},
        {"question": "Which statement creates a generator function?",
         "options": ["yield", "return", "generate", "yieldfrom"],
         "answer": "yield"},
        {"question": "What is a decorator?",
         "options": ["Function that modifies another function", "Loop", "Error handler", "Type of variable"],
         "answer": "Function that modifies another function"},
    ],
    "Libraries": [
        {"question": "Which library is used for numerical arrays?",
         "options": ["pandas", "numpy", "matplotlib", "requests"],
         "answer": "numpy"},
        {"question": "Which library is commonly used for dataframes?",
         "options": ["numpy", "pandas", "tkinter", "sys"],
         "answer": "pandas"},
        {"question": "Which library plots graphs?",
         "options": ["seaborn", "matplotlib", "both", "csv"],
         "answer": "both"},
        {"question": "Which library helps HTTP requests?",
         "options": ["requests", "urllib3", "http", "Both requests and urllib3"],
         "answer": "Both requests and urllib3"},
        {"question": "Which library is built-in for JSON?",
         "options": ["json", "simplejson", "ujson", "rapidjson"],
         "answer": "json"},
        {"question": "Which library is for machine learning (popular)?",
         "options": ["scikit-learn", "requests", "tkinter", "flask"],
         "answer": "scikit-learn"},
        {"question": "Which library is used for web frameworks?",
         "options": ["flask", "matplotlib", "numpy", "pandas"],
         "answer": "flask"},
        {"question": "Which library helps creating GUIs?",
         "options": ["tkinter", "numpy", "pandas", "requests"],
         "answer": "tkinter"},
        {"question": "Which is used for HTML parsing?",
         "options": ["beautifulsoup4", "pandas", "numpy", "tkinter"],
         "answer": "beautifulsoup4"},
        {"question": "Which library aids image processing?",
         "options": ["Pillow", "OpenCV", "Both", "matplotlib"],
         "answer": "Both"},
        {"question": "Which library provides data visualization high-level API?",
         "options": ["matplotlib", "seaborn", "requests", "sys"],
         "answer": "seaborn"},
        {"question": "Which library helps asynchronous programming?",
         "options": ["asyncio", "threading", "multiprocessing", "socket"],
         "answer": "asyncio"},
        {"question": "Which library is for creating REST APIs easily?",
         "options": ["FastAPI", "csv", "json", "tkinter"],
         "answer": "FastAPI"},
        {"question": "Which package manager installs packages?",
         "options": ["pip", "apt", "npm", "gem"],
         "answer": "pip"},
        {"question": "What does 'import os' provide?",
         "options": ["Operating system interaction", "Networking", "Plotting", "Dataframes"],
         "answer": "Operating system interaction"},
        {"question": "Which library helps testing in Python?",
         "options": ["pytest", "unittest", "both", "nose"],
         "answer": "both"},
        {"question": "Which library helps working with dates/times?",
         "options": ["datetime", "time", "arrow", "All of the above"],
         "answer": "All of the above"},
        {"question": "Which library is used for scientific computing beyond numpy?",
         "options": ["scipy", "pandas", "tkinter", "requests"],
         "answer": "scipy"},
        {"question": "Which library can create interactive dashboards?",
         "options": ["dash", "tkinter", "matplotlib", "pandas"],
         "answer": "dash"},
        {"question": "Which library is best for parsing command line arguments?",
         "options": ["argparse", "sys.argv", "click", "All of the above"],
         "answer": "All of the above"},
    ],
    "General Knowledge": [
        {"question": "What is the capital of Pakistan?",
         "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
         "answer": "Islamabad"},
        {"question": "Which planet is known as the Red Planet?",
         "options": ["Earth", "Mars", "Jupiter", "Venus"],
         "answer": "Mars"},
        {"question": "Who wrote 'The Star-Spangled Banner' (national anthem of the USA)?",
         "options": ["Francis Scott Key", "Walt Whitman", "John Keats", "Rabindranath Tagore"],
         "answer": "Francis Scott Key"},
        {"question": "Which language is primarily used for Android app development?",
         "options": ["Swift", "Java/Kotlin", "Python", "C#"],
         "answer": "Java/Kotlin"},
        {"question": "Which gas do plants primarily use for photosynthesis?",
         "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
         "answer": "Carbon dioxide"},
        {"question": "Which ocean is the largest by surface area?",
         "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
         "answer": "Pacific"},
        {"question": "Who painted the Mona Lisa?",
         "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
         "answer": "Leonardo da Vinci"},
        {"question": "Which country hosted the 2016 Summer Olympics?",
         "options": ["China", "Brazil", "UK", "Russia"],
         "answer": "Brazil"},
        {"question": "Which element has chemical symbol 'O'?",
         "options": ["Gold", "Oxygen", "Osmium", "Silver"],
         "answer": "Oxygen"},
        {"question": "Which is the largest mammal on Earth?",
         "options": ["African elephant", "Blue whale", "Giraffe", "Hippopotamus"],
         "answer": "Blue whale"},
        {"question": "Which invention is Thomas Edison famous for?",
         "options": ["Telephone", "Light bulb (practical)", "Radio", "Airplane"],
         "answer": "Light bulb (practical)"},
        {"question": "Which city is the capital of Japan?",
         "options": ["Seoul", "Tokyo", "Beijing", "Bangkok"],
         "answer": "Tokyo"},
        {"question": "Which country is known for the Great Barrier Reef?",
         "options": ["Australia", "USA", "South Africa", "India"],
         "answer": "Australia"},
        {"question": "What is H2O commonly known as?",
         "options": ["Salt", "Water", "Hydrogen peroxide", "Oxygen"],
         "answer": "Water"},
        {"question": "Which continent is Egypt located in?",
         "options": ["Asia", "Europe", "Africa", "Australia"],
         "answer": "Africa"},
        {"question": "Who is known as the 'Father of Computers' (concept of programmable computer)?",
         "options": ["Alan Turing", "Charles Babbage", "Tim Berners-Lee", "Bill Gates"],
         "answer": "Charles Babbage"},
        {"question": "Which month has an extra day in a leap year?",
         "options": ["February", "March", "April", "June"],
         "answer": "February"},
        {"question": "What is the freezing point of water (Celsius)?",
         "options": ["0", "32", "-1", "100"],
         "answer": "0"},
        {"question": "Which device measures temperature?",
         "options": ["Barometer", "Thermometer", "Hygrometer", "Odometer"],
         "answer": "Thermometer"},
        {"question": "Which is the tallest mountain in the world (above sea level)?",
         "options": ["K2", "Kangchenjunga", "Everest", "Lhotse"],
         "answer": "Everest"},
    ],
}

# -------------------- APP --------------------
RESULTS_FILE = "quiz_results.txt"
QUESTION_TIME = 15  # seconds per question

class QuizProApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Umer's Python Quiz Pro")
        self.root.geometry("980x700")
        self.root.resizable(False, False)
        self.root.config(bg="#f6f9ff")

        # Top bar: logo + title
        top = tk.Frame(self.root, bg="#0b5bd7")
        top.pack(fill="x")
        try:
            logo_img = Image.open("quiz_logo.png")
            logo_img = logo_img.resize((64, 64))
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(top, image=self.logo, bg="#0b5bd7").pack(side="left", padx=12, pady=8)
        except Exception:
            tk.Label(top, text="🧠", font=("Arial", 40), bg="#0b5bd7", fg="white").pack(side="left", padx=12, pady=8)
        tk.Label(top, text="Umer's Python Quiz Pro", bg="#0b5bd7", fg="white",
                 font=("Helvetica", 24, "bold")).pack(side="left", padx=6)

        # Container for screens
        self.container = tk.Frame(self.root, bg="#f6f9ff")
        self.container.pack(fill="both", expand=True)

        # State
        self.current_topic = None
        self.question_list = []
        self.question_index = 0
        self.score = 0
        self.user_answers = []  # list of dicts per question: {question, options, correct_answer, chosen, correct}
        self.timer_after_id = None
        self.time_left = QUESTION_TIME

        # Show topic selection initially
        self.show_topics_screen()

    # ---------------- Topics screen ----------------
    def show_topics_screen(self):
        self.cancel_timer()
        for w in self.container.winfo_children():
            w.destroy()

        tk.Label(self.container, text="✨ Select Topic ✨", bg="#f6f9ff",
                 font=("Arial", 22, "bold")).pack(pady=22)

        grid = tk.Frame(self.container, bg="#f6f9ff")
        grid.pack(pady=10)
        for i, name in enumerate(topics.keys()):
            b = tk.Button(grid, text=name, width=24, height=2,
                          font=("Arial", 14, "bold"), bg="#eaf2ff", fg="#06345a",
                          cursor="hand2", command=lambda n=name: self.start_topic(n))
            b.grid(row=i // 2, column=i % 2, padx=18, pady=14)

        # small instructions
        tk.Label(self.container, text=f"Each topic contains 20 MCQs. You have {QUESTION_TIME} sec per question.",
                 bg="#f6f9ff", font=("Arial", 12)).pack(pady=10)

        tk.Button(self.container, text="❌ Exit", command=self.root.destroy,
                  bg="#d9534f", fg="white", font=("Arial", 12, "bold"), width=12).pack(pady=12)

    # ---------------- Start topic ----------------
    def start_topic(self, topic_name):
        self.current_topic = topic_name
        pool = topics[topic_name].copy()
        random.shuffle(pool)
        self.question_list = pool[:20]
        self.user_answers = []
        self.question_index = 0
        self.score = 0
        self.show_question_screen()

    # ---------------- Show question ----------------
    def show_question_screen(self):
        self.cancel_timer()
        for w in self.container.winfo_children():
            w.destroy()

        qdata = self.question_list[self.question_index]
        # top info bar
        topbar = tk.Frame(self.container, bg="#f6f9ff")
        topbar.pack(fill="x", pady=(10, 0))
        tk.Label(topbar, text=f"Topic: {self.current_topic}", bg="#f6f9ff",
                 font=("Arial", 12, "bold")).pack(side="left", padx=10)
        tk.Label(topbar, text=f"Q {self.question_index + 1} / {len(self.question_list)}",
                 bg="#f6f9ff", font=("Arial", 12)).pack(side="left", padx=6)

        # Progress bar
        pb_frame = tk.Frame(self.container, bg="#f6f9ff")
        pb_frame.pack(fill="x", padx=14, pady=(6, 0))
        self.progress = ttk.Progressbar(pb_frame, maximum=len(self.question_list), value=self.question_index)
        self.progress.pack(fill="x", pady=6)

        # Timer label
        timer_frame = tk.Frame(self.container, bg="#f6f9ff")
        timer_frame.pack(fill="x", padx=14)
        self.time_left = QUESTION_TIME
        self.timer_label = tk.Label(timer_frame, text=f"Time left: {self.time_left} s", bg="#f6f9ff",
                                    font=("Arial", 12, "bold"), fg="#b02a2a")
        self.timer_label.pack(side="right", padx=10)

        # Question text
        qtext = f"Q{self.question_index + 1}. {qdata['question']}"
        tk.Label(self.container, text=qtext, bg="#f6f9ff", font=("Arial", 16, "bold"),
                 wraplength=920, justify="left").pack(pady=16, padx=12)

        # Options (shuffle displayed options)
        self.var = tk.StringVar(value="")
        opts = qdata["options"].copy()
        random.shuffle(opts)
        opts_frame = tk.Frame(self.container, bg="#f6f9ff")
        opts_frame.pack(pady=6)
        for opt in opts:
            rb = tk.Radiobutton(opts_frame, text=opt, variable=self.var, value=opt,
                                font=("Arial", 13), bg="#eef6ff", anchor="w",
                                width=110, padx=8, pady=6, indicatoron=0, relief="raised", cursor="hand2")
            rb.pack(pady=6)

        # If user already answered this index (navigated back), prefill
        if self.question_index < len(self.user_answers):
            prev_choice = self.user_answers[self.question_index]["chosen"]
            if prev_choice:
                self.var.set(prev_choice)

        # Navigation buttons
        nav = tk.Frame(self.container, bg="#f6f9ff")
        nav.pack(pady=14)
        tk.Button(nav, text="⬅ Topics", command=self.show_topics_screen,
                  bg="#eef6ff", font=("Arial", 11), width=14).grid(row=0, column=0, padx=8)
        prev_btn = tk.Button(nav, text="Previous ◀", command=self.previous_question,
                             bg="#eaf2ff", font=("Arial", 11), width=12)
        prev_btn.grid(row=0, column=1, padx=8)
        tk.Button(nav, text="Submit ▶", command=self.submit_answer,
                  bg="#0b5bd7", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=2, padx=8)

        if self.question_index == 0:
            prev_btn.config(state="disabled")

        # Start the timer
        self.update_timer()

    # ---------------- Timer ----------------
    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left} s")
        if self.time_left <= 0:
            # auto-submit with No Answer if nothing selected
            if not self.var.get():
                self.var.set("")  # ensure empty
            self.submit_answer(auto=True)
            return
        self.time_left -= 1
        self.timer_after_id = self.root.after(1000, self.update_timer)

    def cancel_timer(self):
        try:
            if self.timer_after_id:
                self.root.after_cancel(self.timer_after_id)
        except Exception:
            pass
        self.timer_after_id = None

    # ---------------- Previous question ----------------
    def previous_question(self):
        # allow moving back and keep store updated
        if self.question_index > 0:
            self.question_index -= 1
            self.show_question_screen()

    # ---------------- Submit answer ----------------
    def submit_answer(self, auto=False):
        # auto True if timer expired
        choice = self.var.get()
        # if empty and auto, set "No Answer"
        if choice == "":
            choice = "No Answer"

        current_q = self.question_list[self.question_index]
        correct = current_q["answer"]

        # If answer already exists in this index, update it; else append
        if self.question_index < len(self.user_answers):
            self.user_answers[self.question_index]["chosen"] = choice
            self.user_answers[self.question_index]["correct"] = (choice == correct)
        else:
            self.user_answers.append({
                "question": current_q["question"],
                "options": current_q["options"],
                "correct_answer": correct,
                "chosen": choice,
                "correct": (choice == correct)
            })

        # recompute score safely
        self.score = sum(1 for a in self.user_answers if a["correct"])

        # move forward
        self.question_index += 1
        # update progress bar (value = number of answered questions)
        if self.question_index <= len(self.question_list):
            # progress value = answered count
            answered = len(self.user_answers)
            try:
                self.progress['value'] = answered
            except Exception:
                pass

        if self.question_index < len(self.question_list):
            self.show_question_screen()
        else:
            self.cancel_timer()
            self.show_result_screen()
            self.save_result_to_file()

    # ---------------- Results ----------------
    def show_result_screen(self):
        for w in self.container.winfo_children():
            w.destroy()

        total = len(self.question_list)
        percent = int((self.score / total) * 100) if total else 0
        remark = "🌟 Outstanding!" if percent >= 80 else "👍 Good Job!" if percent >= 50 else "😅 Keep Practicing!"

        tk.Label(self.container, text="🏁 Quiz Completed", bg="#f6f9ff",
                 font=("Helvetica", 20, "bold")).pack(pady=(12, 6))
        tk.Label(self.container, text=f"Topic: {self.current_topic}", bg="#f6f9ff",
                 font=("Arial", 14)).pack(pady=4)
        tk.Label(self.container, text=f"Score: {self.score} / {total}", bg="#f6f9ff",
                 font=("Arial", 16, "bold")).pack(pady=4)
        tk.Label(self.container, text=f"Percentage: {percent}%", bg="#f6f9ff",
                 font=("Arial", 14)).pack(pady=2)
        tk.Label(self.container, text=remark, bg="#f6f9ff", font=("Arial", 13)).pack(pady=8)

        btns = tk.Frame(self.container, bg="#f6f9ff")
        btns.pack(pady=12)
        tk.Button(btns, text="🔁 Restart Topic", command=self.restart_topic,
                  bg="#0b5bd7", fg="white", font=("Arial", 12, "bold"), width=16).grid(row=0, column=0, padx=8)
        tk.Button(btns, text="🔙 Back to Topics", command=self.show_topics_screen,
                  bg="#eaf2ff", font=("Arial", 12), width=14).grid(row=0, column=1, padx=8)
        tk.Button(btns, text="📝 Review Answers", command=self.open_review_window,
                  bg="#eef6ff", font=("Arial", 12), width=14).grid(row=0, column=2, padx=8)
        tk.Button(btns, text="❌ Exit", command=self.root.destroy,
                  bg="#d9534f", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=3, padx=8)

    def restart_topic(self):
        # reshuffle and start same topic anew
        self.start_topic(self.current_topic)

    # ---------------- Save result to file ----------------
    def save_result_to_file(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = len(self.question_list)
        percent = int((self.score / total) * 100) if total else 0
        line = f"{now} | Topic: {self.current_topic} | Score: {self.score}/{total} | {percent}%\n"
        try:
            with open(RESULTS_FILE, "a", encoding="utf-8") as f:
                f.write(line)
        except Exception as e:
            # non-fatal: show small warning
            print("Could not write results file:", e)

    # ---------------- Review answers window ----------------
    def open_review_window(self):
        review = tk.Toplevel(self.root)
        review.title(f"Review — {self.current_topic}")
        review.geometry("920x560")
        review.config(bg="#f8fbff")

        header = tk.Label(review, text=f"Review — {self.current_topic}", bg="#0b4f8c", fg="white",
                          font=("Helvetica", 14, "bold"), pady=8)
        header.pack(fill="x")

        canvas = tk.Canvas(review, bg="#f8fbff")
        scrollbar = tk.Scrollbar(review, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#f8fbff")

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Show each Q and user's chosen + correct if wrong
        for i, a in enumerate(self.user_answers, start=1):
            q_label = tk.Label(scroll_frame, text=f"{i}. {a['question']}", bg="#f8fbff",
                               font=("Arial", 11, "bold"), wraplength=860, justify="left")
            q_label.pack(anchor="w", pady=(10, 0), padx=10)

            chosen = a["chosen"]
            correct = a["correct_answer"]
            if a["correct"]:
                your_label = tk.Label(scroll_frame, text=f"Your answer: {chosen}  ✅", bg="#f8fbff",
                                      font=("Arial", 11), justify="left")
                your_label.pack(anchor="w", padx=24)
            else:
                your_label = tk.Label(scroll_frame, text=f"Your answer: {chosen}  ❌", bg="#f8fbff",
                                      font=("Arial", 11), justify="left")
                your_label.pack(anchor="w", padx=24)
                corr_label = tk.Label(scroll_frame, text=f"Correct answer: {correct}", bg="#f8fbff",
                                      font=("Arial", 11, "bold"), justify="left")
                corr_label.pack(anchor="w", padx=24)

        tk.Button(review, text="Close", command=review.destroy,
                  bg="#0b5bd7", fg="white", font=("Arial", 11, "bold"), width=12).pack(pady=10)

# -------------------- Main --------------------
if __name__ == "__main__":
    # ensure results file exists
    if not os.path.exists(RESULTS_FILE):
        open(RESULTS_FILE, "w", encoding="utf-8").close()

    root = tk.Tk()
    app = QuizProApp(root)
    root.mainloop()
