"""
quiz.py
=======
Diagnostic quiz for Python Programming (Core & Advanced).

Each topic has questions at two levels:
  - Core     : fundamental concepts every 2nd-year student should know
  - Advanced : deeper understanding for higher marks

How the adaptive level decision works (conditional logic):
  - Score >= 70%  →  Student is ready for ADVANCED content
  - Score >= 40%  →  Student should revise CORE content
  - Score <  40%  →  Student needs CORE fundamentals first

Concepts demonstrated:
  - Dictionaries  : question bank stored as dict of lists
  - Lists         : multiple questions per topic
  - Tuples        : (question, options, correct_answer_index, level)
  - for loops     : iterate through selected questions
  - while loops   : keep asking until valid input
  - try/except    : handle non-numeric input gracefully
  - Functions     : select_questions(), run_quiz(), determine_level()
  - Conditional   : if/elif/else for level determination
  - random.sample : pick questions without repetition
"""

import random


# ─────────────────────────────────────────────────────────────
#  QUESTION BANK
#  Format: QUESTION_BANK[topic] = list of tuples
#  Each tuple: (question_text, [option_A, B, C, D], correct_index, difficulty)
#    correct_index : 0 = A, 1 = B, 2 = C, 3 = D
#    difficulty    : "core" or "advanced"
# ─────────────────────────────────────────────────────────────
QUESTION_BANK = {

    "Variables & Data Types": [
        ("What is the data type of the value 3.14 in Python?",
         ["int", "float", "str", "double"], 1, "core"),

        ("Which of the following is an immutable data type?",
         ["list", "dict", "tuple", "set"], 2, "core"),

        ("What does the type() function return?",
         ["The value of a variable", "The memory address", "The data type of a variable", "The size of a variable"], 2, "core"),

        ("What is the result of: int('42') + 8?",
         ["Error", "'428'", "50", "42.8"], 2, "core"),

        ("Which of the following correctly annotates a variable as an integer?",
         ["x: int = 5", "x = int(5)", "x = 5 # int", "int x = 5"], 0, "advanced"),

        ("What is the output of: print(type(True))?",
         ["<class 'int'>", "<class 'bool'>", "<class 'str'>", "True"], 1, "core"),
    ],

    "Control Flow": [
        ("What is the output of:\nx = 10\nif x > 5:\n    print('big')\nelse:\n    print('small')",
         ["small", "big", "Error", "None"], 1, "core"),

        ("Which keyword is used to skip the rest of the current loop iteration?",
         ["break", "pass", "return", "continue"], 3, "core"),

        ("What does the 'pass' statement do in Python?",
         ["Ends the program", "Skips one iteration", "Does nothing — it is a placeholder", "Exits a loop"], 2, "core"),

        ("What is the output of:\nfor i in range(1, 6):\n    if i == 3:\n        break\n    print(i)",
         ["1 2 3", "1 2", "3 4 5", "1 2 3 4 5"], 1, "core"),

        ("What is the result of: 5 if 10 > 3 else 0?",
         ["0", "True", "5", "Error"], 2, "advanced"),

        ("Which Python 3.10+ feature replaces long if/elif chains?",
         ["switch/case", "match/case", "select/when", "choose/when"], 1, "advanced"),
    ],

    "Loops": [
        ("What does range(2, 10, 3) produce?",
         ["[2, 5, 8]", "[2, 3, 4, 5, 6, 7, 8, 9]", "[2, 4, 6, 8]", "[3, 6, 9]"], 0, "core"),

        ("How many times will this loop execute?\nfor i in range(5):\n    print(i)",
         ["4", "5", "6", "Infinite"], 1, "core"),

        ("What is the output of:\nx = 0\nwhile x < 3:\n    x += 1\nprint(x)",
         ["0", "2", "3", "4"], 2, "core"),

        ("What does enumerate() do?",
         ["Sorts a list", "Returns pairs of (index, value) while iterating", "Converts a list to a set", "Reverses a list"], 1, "advanced"),

        ("What is the output of:\nprint(list(zip([1,2,3], ['a','b','c'])))",
         ["[(1,'a'), (2,'b'), (3,'c')]", "[[1,'a'], [2,'b'], [3,'c']]", "Error", "[(1,2,3), ('a','b','c')]"], 0, "advanced"),

        ("Which statement correctly uses a for-else construct?",
         ["for else is invalid syntax", "else runs only if the loop completed without a break", "else runs only if the loop ran 0 times", "else runs only when break is hit"], 1, "advanced"),
    ],

    "Functions": [
        ("What keyword is used to define a function in Python?",
         ["func", "define", "def", "function"], 2, "core"),

        ("What does the return statement do?",
         ["Prints a value", "Ends the program", "Sends a value back to the caller and exits the function", "Defines a variable"], 2, "core"),

        ("What is the output of:\ndef greet(name='World'):\n    return 'Hello, ' + name\nprint(greet())",
         ["Hello,", "Hello, World", "Error", "None"], 1, "core"),

        ("What does *args allow in a function?",
         ["Only keyword arguments", "A fixed number of arguments", "Any number of positional arguments", "No arguments at all"], 2, "advanced"),

        ("What is the scope of a variable defined inside a function?",
         ["Global", "Local — only accessible within that function", "Class-level", "Module-level"], 1, "core"),

        ("What does **kwargs allow in a function?",
         ["A fixed number of keyword arguments", "Any number of keyword arguments as a dictionary", "Variable positional arguments", "Arguments with type checking"], 1, "advanced"),
    ],

    "Lists & Tuples": [
        ("Which method adds an element to the END of a list?",
         ["add()", "insert()", "append()", "push()"], 2, "core"),

        ("What is the output of:\nmy_list = [10, 20, 30, 40]\nprint(my_list[-1])",
         ["10", "40", "30", "Error"], 1, "core"),

        ("What is the output of:\nt = (1, 2, 3)\nprint(t[1])",
         ["1", "2", "3", "Error"], 1, "core"),

        ("Can you change elements of a tuple after creation?",
         ["Yes, using indexing", "Yes, using .update()", "No — tuples are immutable", "Only with type casting"], 2, "core"),

        ("What does list slicing [1:4] return from [0,1,2,3,4,5]?",
         ["[1,2,3,4]", "[1,2,3]", "[0,1,2,3]", "[2,3,4]"], 1, "advanced"),

        ("What is the output of:\nx = [1,2,3]\ny = x\ny.append(4)\nprint(x)",
         ["[1,2,3]", "[1,2,3,4]", "[4]", "Error"], 1, "advanced"),
    ],

    "Dictionaries & Sets": [
        ("How do you access the value for key 'name' in a dictionary d?",
         ["d.name", "d[name]", "d['name']", "d->name"], 2, "core"),

        ("Which method returns all the keys of a dictionary?",
         [".values()", ".items()", ".keys()", ".all()"], 2, "core"),

        ("What is the output of:\nd = {'a': 1, 'b': 2}\nprint(d.get('c', 0))",
         ["None", "Error", "0", "'c'"], 2, "core"),

        ("What data structure guarantees unique elements and is unordered?",
         ["list", "tuple", "dict", "set"], 3, "core"),

        ("What does set intersection return?",
         ["All elements from both sets", "Elements only in the first set", "Elements common to both sets", "Elements in neither set"], 2, "advanced"),

        ("What is the output of:\nd = {}\nd['x'] = d.get('x', 0) + 1\nprint(d)",
         ["{'x': 0}", "{'x': 1}", "Error", "{}"], 1, "advanced"),
    ],

    "File Handling": [
        ("Which mode opens a file for writing and CREATES it if it doesn't exist?",
         ["'r'", "'a'", "'w'", "'x'"], 2, "core"),

        ("What does the 'with' statement guarantee when opening files?",
         ["Faster file reading", "The file is closed automatically when the block ends", "The file is created if missing", "File locking"], 1, "core"),

        ("What does file.read() return?",
         ["A list of lines", "The entire file content as a single string", "One character at a time", "The file size"], 1, "core"),

        ("Which Python module is used to work with JSON files?",
         ["csv", "json", "os", "pickle"], 1, "advanced"),

        ("What does json.dumps() do?",
         ["Loads JSON from a file", "Converts a Python object to a JSON-formatted string", "Deletes a JSON key", "Formats JSON on screen"], 1, "advanced"),

        ("What is the difference between 'w' and 'a' file modes?",
         ["No difference", "'w' overwrites; 'a' appends to existing content", "'a' overwrites; 'w' appends", "'w' is read-only"], 1, "core"),
    ],

    "Exception Handling": [
        ("Which keyword starts a block that catches errors?",
         ["try", "except", "catch", "error"], 1, "core"),

        ("What exception is raised when you divide by zero?",
         ["ValueError", "TypeError", "ZeroDivisionError", "ArithmeticError"], 2, "core"),

        ("What does the 'finally' block do?",
         ["Runs only if no exception occurred", "Runs only if an exception occurred", "Always runs, whether or not an exception occurred", "Re-raises the exception"], 2, "core"),

        ("How do you raise a custom error in Python?",
         ["throw ValueError('msg')", "raise ValueError('msg')", "error ValueError('msg')", "throw new ValueError('msg')"], 1, "core"),

        ("Which base class should custom exceptions inherit from?",
         ["BaseError", "Error", "Exception", "RuntimeError"], 2, "advanced"),

        ("What is the output if you catch a ValueError when a TypeError occurs?",
         ["The ValueError handler runs", "The TypeError is caught", "The TypeError propagates uncaught", "Python converts the error type"], 2, "advanced"),
    ],

    "Object-Oriented Programming": [
        ("What keyword creates a new class in Python?",
         ["object", "class", "def", "struct"], 1, "core"),

        ("What is 'self' in Python class methods?",
         ["A keyword like 'this' in Java — refers to the class itself", "A reference to the current instance of the class", "A built-in variable holding the class name", "An optional parameter for static methods"], 1, "core"),

        ("What is the purpose of the __init__ method?",
         ["To destroy an object", "To copy an object", "To initialise an object's attributes when it is created", "To define class-level variables"], 2, "core"),

        ("What does encapsulation mean?",
         ["Inheriting from a parent class", "Bundling data and methods together in a class and restricting direct access", "Making all attributes public", "Writing multiple methods with the same name"], 1, "core"),

        ("What is the difference between @classmethod and @staticmethod?",
         ["They are identical", "@classmethod receives cls as the first argument; @staticmethod receives neither self nor cls", "@staticmethod can only be called on instances", "@classmethod cannot access class variables"], 1, "advanced"),

        ("What is a dunder (magic) method?",
         ["A method starting with a capital letter", "A private method", "A special method surrounded by double underscores like __str__", "A method that raises an error"], 2, "advanced"),
    ],

    "Inheritance & Polymorphism": [
        ("How does a child class inherit from a parent class in Python?",
         ["child class extends parent", "class Child(Parent):", "class Child inherits Parent:", "child = Parent()"], 1, "core"),

        ("What does super() do inside a child class?",
         ["Creates a new instance", "Calls the parent class's method", "Deletes the parent class", "Converts to parent type"], 1, "core"),

        ("What is method overriding?",
         ["Calling the same method twice", "A child class providing its own version of a method defined in the parent", "Adding more parameters to a method", "Deleting a parent method"], 1, "core"),

        ("What is polymorphism?",
         ["Only one class can be used at a time", "Multiple classes having different names", "The ability for different classes to be treated through a common interface", "Copying an object"], 2, "core"),

        ("What does ABC stand for in Python's abc module?",
         ["Automatic Base Class", "Abstract Base Class", "Advanced Base Component", "Assigned Base Constructor"], 1, "advanced"),

        ("What happens if you don't implement an abstract method in a subclass?",
         ["Python ignores it", "The method is inherited as-is", "A TypeError is raised when you try to instantiate the subclass", "The program runs fine"], 2, "advanced"),
    ],

    "List Comprehensions & Lambdas": [
        ("What is the output of: [x*2 for x in range(4)]",
         ["[0,1,2,3]", "[2,4,6,8]", "[0,2,4,6]", "[1,2,3,4]"], 2, "core"),

        ("What is a lambda function?",
         ["A named function defined with def", "An anonymous, single-expression function defined with lambda", "A function that returns None", "A function stored in a class"], 1, "core"),

        ("What does filter(lambda x: x%2==0, [1,2,3,4,5]) return when converted to a list?",
         ["[1,3,5]", "[2,4]", "[False,True,False,True,False]", "Error"], 1, "advanced"),

        ("What is the output of: list(map(lambda x: x**2, [1,2,3]))",
         ["[1,4,9]", "[2,4,6]", "[1,2,3]", "[1,8,27]"], 0, "advanced"),

        ("What is a dict comprehension?",
         ["{k:v for k,v in items}", "[k:v for k,v in items]", "(k,v for k,v in items)", "{k for k,v in items}"], 0, "advanced"),

        ("What is the output of: [x for x in range(10) if x%3==0]",
         ["[3,6,9]", "[0,3,6,9]", "[1,4,7]", "[0,1,2,3]"], 1, "core"),
    ],

    "Decorators & Generators": [
        ("What symbol is used to apply a decorator in Python?",
         ["#", "@", "$", "&"], 1, "core"),

        ("What does the 'yield' keyword do in a function?",
         ["Exits the function completely", "Makes the function return a generator that produces values one at a time", "Pauses execution forever", "Returns None"], 1, "advanced"),

        ("What is a generator in Python?",
         ["A function that generates random numbers", "A function that uses yield to lazily produce a sequence of values", "A special type of list", "A faster version of range()"], 1, "advanced"),

        ("When is a decorator function executed?",
         ["Every time the decorated function is called", "At class instantiation", "At the time the @decorator line is encountered — when the module is loaded", "Only during testing"], 2, "advanced"),

        ("What does a decorator fundamentally do?",
         ["Renames a function", "Wraps a function to add behaviour before/after without modifying its source code", "Deletes a function after first call", "Converts a function to a class"], 1, "advanced"),
    ],

}


# ─────────────────────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────

def select_questions(topic: str, num_core: int = 3, num_advanced: int = 3) -> list:
    """
    Pick a balanced mix of core and advanced questions for the quiz.

    Uses random.sample() so a different set appears each time.

    Parameters:
        topic        : the Python topic to quiz on
        num_core     : how many core questions to include (default 3)
        num_advanced : how many advanced questions to include (default 3)

    Returns:
        A shuffled list of question tuples
    """
    all_questions = QUESTION_BANK.get(topic, [])

    # Separate questions by difficulty
    core_qs     = [q for q in all_questions if q[3] == "core"]
    advanced_qs = [q for q in all_questions if q[3] == "advanced"]

    # Sample without replacement (don't repeat the same question)
    chosen_core     = random.sample(core_qs,     min(num_core, len(core_qs)))
    chosen_advanced = random.sample(advanced_qs, min(num_advanced, len(advanced_qs)))

    selected = chosen_core + chosen_advanced
    random.shuffle(selected)   # mix core and advanced together
    return selected


def determine_level(score: int) -> str:
    """
    Decide the recommended level based on quiz score.

    CONDITIONAL LOGIC (this is the adaptive decision engine):
        score >= 70  →  ready for ADVANCED content
        score >= 40  →  revise CORE content first
        score <  40  →  needs CORE fundamentals

    Parameters:
        score : integer 0–100

    Returns:
        "advanced" or "core"
    """
    if score >= 70:
        return "advanced"
    elif score >= 40:
        return "core"
    else:
        return "core"    # below 40% → core with extra attention needed


def get_score_label(score: int) -> str:
    """
    Return a descriptive label for a quiz score.

    Parameters:
        score : integer 0–100

    Returns:
        A string description
    """
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good — Advanced level unlocked"
    elif score >= 50:
        return "Average — Keep practising Core"
    elif score >= 30:
        return "Below average — Focus on Core fundamentals"
    else:
        return "Needs improvement — Start from the basics"


def run_quiz(topic: str) -> dict:
    """
    Run an interactive diagnostic quiz for the given topic.

    Steps:
      1. Select 6 questions (3 core + 3 advanced)
      2. Display each question with 4 options (A/B/C/D)
      3. Accept and validate user input
      4. Give immediate feedback after each answer
      5. Calculate score and determine level
      6. Return result dictionary

    Parameters:
        topic : the Python topic to test

    Returns:
        dict with keys: "score", "correct", "total", "level", "label"
    """
    questions = select_questions(topic, num_core=3, num_advanced=3)

    if not questions:
        print(f"  No questions found for topic: {topic}")
        return {"score": 0, "correct": 0, "total": 0, "level": "core", "label": "N/A"}

    # ── Quiz header ────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(f"  QUIZ: {topic}")
    print("=" * 60)
    print(f"  {len(questions)} questions  |  Type A, B, C, or D to answer\n")

    correct_count = 0
    option_letters = ["A", "B", "C", "D"]

    # ── Question loop ──────────────────────────────────────────────
    for i, (question, options, correct_index, difficulty) in enumerate(questions, start=1):

        print(f"  Q{i}. [{difficulty.upper()}]  {question}")

        # Display the 4 options
        for letter, option_text in zip(option_letters, options):
            print(f"       {letter}. {option_text}")

        # ── Input validation loop ──────────────────────────────────
        # Keep asking until the user gives a valid answer (A, B, C, or D)
        while True:
            try:
                user_answer = input("\n     Your answer: ").strip().upper()
                if user_answer in option_letters:
                    break   # valid input received
                else:
                    print("     Please enter A, B, C, or D.")
            except (ValueError, EOFError):
                print("     Please enter A, B, C, or D.")

        # ── Check answer ───────────────────────────────────────────
        correct_letter = option_letters[correct_index]

        if user_answer == correct_letter:
            print("     CORRECT!\n")
            correct_count += 1
        else:
            print(f"     Incorrect. Correct answer: {correct_letter}. {options[correct_index]}\n")

    # ── Calculate result ───────────────────────────────────────────
    total      = len(questions)
    score      = int((correct_count / total) * 100)
    level      = determine_level(score)
    label      = get_score_label(score)

    # ── Result summary ─────────────────────────────────────────────
    print("─" * 60)
    print(f"  Score : {correct_count}/{total}  ({score}%)")
    print(f"  Result: {label}")
    print(f"  Level : {level.upper()} content recommended")
    print("─" * 60 + "\n")

    return {
        "score":   score,
        "correct": correct_count,
        "total":   total,
        "level":   level,
        "label":   label,
    }
