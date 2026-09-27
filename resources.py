"""
resources.py
============
Defines all learning resources for Python Programming (Core & Advanced).

A "resource" is one learning item — a video, article, exercise, etc.
Each resource belongs to a TOPIC and a LEVEL (core or advanced).

Concepts used here:
  - Dictionaries  : store resources grouped by topic and level
  - Lists         : hold multiple resources per topic
  - Strings       : resource titles, descriptions, URLs
  - Constants     : TOPICS and ALL_RESOURCES never change at runtime
"""

# ─────────────────────────────────────────────────────────────
#  TOPIC NAMES  (used as keys throughout the project)
# ─────────────────────────────────────────────────────────────
TOPICS = [
    "Variables & Data Types",
    "Operators & Expressions",
    "Control Flow",
    "Loops",
    "Functions",
    "Strings",
    "Lists & Tuples",
    "Dictionaries & Sets",
    "File Handling",
    "Exception Handling",
    "Object-Oriented Programming",
    "Inheritance & Polymorphism",
    "List Comprehensions & Lambdas",
    "Modules & Packages",
    "Decorators & Generators",
]

# ─────────────────────────────────────────────────────────────
#  RESOURCE BANK
#  Structure:
#    ALL_RESOURCES[topic][level] = list of resource dicts
#
#  Each resource dict has these keys:
#    id          – unique identifier
#    title       – display name
#    type        – "video" | "reading" | "exercise" | "quiz" | "project"
#    duration    – estimated minutes to complete
#    description – one-sentence summary
#    url         – where to find it (placeholder links)
# ─────────────────────────────────────────────────────────────
ALL_RESOURCES = {

    "Variables & Data Types": {
        "core": [
            {
                "id": "vdt_c1",
                "title": "Python Variables Explained",
                "type": "video",
                "duration": 15,
                "description": "How Python stores values using variables and the basic data types: int, float, str, bool.",
                "url": "https://realpython.com/python-variables/",
            },
            {
                "id": "vdt_c2",
                "title": "Data Types in Python – Reading",
                "type": "reading",
                "duration": 20,
                "description": "Official Python docs on built-in types with examples.",
                "url": "https://docs.python.org/3/library/stdtypes.html",
            },
            {
                "id": "vdt_c3",
                "title": "Variables & Types – Practice Exercises",
                "type": "exercise",
                "duration": 25,
                "description": "10 hands-on exercises: declare variables, use type(), convert between types.",
                "url": "https://pynative.com/python-variables-and-data-types/",
            },
            {
                "id": "vdt_c4",
                "title": "Variables & Data Types – Quiz",
                "type": "quiz",
                "duration": 10,
                "description": "10 MCQs testing your understanding of Python variables and types.",
                "url": "https://pynative.com/python-data-types-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "vdt_a1",
                "title": "Type Hinting & Annotations in Python",
                "type": "reading",
                "duration": 25,
                "description": "Use Python type annotations to write self-documenting, safer code.",
                "url": "https://realpython.com/lessons/type-hinting/",
            },
            {
                "id": "vdt_a2",
                "title": "Mutable vs Immutable Objects",
                "type": "video",
                "duration": 20,
                "description": "Deep dive into why lists are mutable but tuples and strings are not — and how this affects your code.",
                "url": "https://realpython.com/courses/immutability-python/",
            },
        ],
    },

    "Operators & Expressions": {
        "core": [
            {
                "id": "ops_c1",
                "title": "Python Operators – Full Guide",
                "type": "reading",
                "duration": 20,
                "description": "Arithmetic, comparison, logical, bitwise, and assignment operators with examples.",
                "url": "https://realpython.com/python-operators-expressions/",
            },
            {
                "id": "ops_c2",
                "title": "Operator Precedence – Video",
                "type": "video",
                "duration": 15,
                "description": "Learn the order Python evaluates expressions (PEMDAS for Python).",
                "url": "https://www.youtube.com/watch?v=kCGE6CSlCVs",
            },
            {
                "id": "ops_c3",
                "title": "Operators – Exercise Set",
                "type": "exercise",
                "duration": 20,
                "description": "Practice using all operator types in small coding challenges.",
                "url": "https://pynative.com/python-operators-and-expression-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "ops_a1",
                "title": "Walrus Operator (:=) in Python 3.8+",
                "type": "reading",
                "duration": 15,
                "description": "Use the walrus operator for assignment expressions in conditions and comprehensions.",
                "url": "https://realpython.com/walrus-operator/",
            },
        ],
    },

    "Control Flow": {
        "core": [
            {
                "id": "cf_c1",
                "title": "if / elif / else – Python Control Flow",
                "type": "video",
                "duration": 20,
                "description": "Write conditional logic to make programs make decisions.",
                "url": "https://realpython.com/python-conditional-statements/",
            },
            {
                "id": "cf_c2",
                "title": "Conditional Statements – Reading",
                "type": "reading",
                "duration": 15,
                "description": "Detailed article on truthiness, nested conditions, and ternary expressions.",
                "url": "https://docs.python.org/3/tutorial/controlflow.html",
            },
            {
                "id": "cf_c3",
                "title": "Control Flow Exercises",
                "type": "exercise",
                "duration": 30,
                "description": "15 problems: grade calculator, age groups, leap year checker, and more.",
                "url": "https://pynative.com/python-if-else-and-for-loop-exercise/",
            },
            {
                "id": "cf_c4",
                "title": "Control Flow Quiz",
                "type": "quiz",
                "duration": 10,
                "description": "10 MCQs on if/elif/else, nested conditions, and short-circuit evaluation.",
                "url": "https://pynative.com/python-if-else-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "cf_a1",
                "title": "Structural Pattern Matching (match / case) – Python 3.10+",
                "type": "reading",
                "duration": 25,
                "description": "Python's modern alternative to long if/elif chains: pattern matching.",
                "url": "https://realpython.com/structural-pattern-matching/",
            },
        ],
    },

    "Loops": {
        "core": [
            {
                "id": "lp_c1",
                "title": "for Loops & while Loops in Python",
                "type": "video",
                "duration": 25,
                "description": "Iterate over lists, ranges, and strings; use break, continue, and else.",
                "url": "https://realpython.com/python-for-loop/",
            },
            {
                "id": "lp_c2",
                "title": "Loop Exercises – 20 Problems",
                "type": "exercise",
                "duration": 40,
                "description": "Patterns, number sequences, FizzBuzz, nested loops — all classic loop problems.",
                "url": "https://pynative.com/python-loop-exercise/",
            },
            {
                "id": "lp_c3",
                "title": "Loop Quiz",
                "type": "quiz",
                "duration": 10,
                "description": "Test your knowledge of for/while loops, range(), and loop control.",
                "url": "https://pynative.com/python-loop-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "lp_a1",
                "title": "Iterators & Iterables in Python",
                "type": "reading",
                "duration": 30,
                "description": "Understand __iter__ and __next__ — what powers Python's for loops under the hood.",
                "url": "https://realpython.com/python-iterators-iterables/",
            },
            {
                "id": "lp_a2",
                "title": "enumerate() & zip() – Power Looping",
                "type": "video",
                "duration": 15,
                "description": "Write cleaner loops using Python's built-in enumerate() and zip().",
                "url": "https://realpython.com/python-enumerate/",
            },
        ],
    },

    "Functions": {
        "core": [
            {
                "id": "fn_c1",
                "title": "Defining & Calling Python Functions",
                "type": "video",
                "duration": 25,
                "description": "def keyword, parameters, return values, and scope (local vs global).",
                "url": "https://realpython.com/defining-your-own-python-function/",
            },
            {
                "id": "fn_c2",
                "title": "Default & Keyword Arguments",
                "type": "reading",
                "duration": 20,
                "description": "Use default parameters and keyword arguments to make functions flexible.",
                "url": "https://realpython.com/python-kwargs-and-args/",
            },
            {
                "id": "fn_c3",
                "title": "Functions Exercises",
                "type": "exercise",
                "duration": 35,
                "description": "Write functions for: calculator, palindrome checker, Fibonacci, prime number checker.",
                "url": "https://pynative.com/python-functions-exercise/",
            },
            {
                "id": "fn_c4",
                "title": "Functions Quiz",
                "type": "quiz",
                "duration": 10,
                "description": "12 questions on function definitions, scope, return values, and arguments.",
                "url": "https://pynative.com/python-functions-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "fn_a1",
                "title": "*args and **kwargs – Variable Arguments",
                "type": "video",
                "duration": 20,
                "description": "Accept any number of positional and keyword arguments in your functions.",
                "url": "https://realpython.com/python-kwargs-and-args/",
            },
            {
                "id": "fn_a2",
                "title": "Recursion in Python",
                "type": "reading",
                "duration": 30,
                "description": "Write recursive functions; understand base cases, call stack, and memoization.",
                "url": "https://realpython.com/python-recursion/",
            },
        ],
    },

    "Strings": {
        "core": [
            {
                "id": "str_c1",
                "title": "Python Strings – Complete Guide",
                "type": "reading",
                "duration": 25,
                "description": "String creation, indexing, slicing, and all essential string methods.",
                "url": "https://realpython.com/python-strings/",
            },
            {
                "id": "str_c2",
                "title": "f-Strings & String Formatting",
                "type": "video",
                "duration": 15,
                "description": "Format strings with f-strings, .format(), and % — and when to use each.",
                "url": "https://realpython.com/python-f-strings/",
            },
            {
                "id": "str_c3",
                "title": "String Exercises – 20 Problems",
                "type": "exercise",
                "duration": 35,
                "description": "Reverse a string, count vowels, check anagram, Caesar cipher, and more.",
                "url": "https://pynative.com/python-string-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "str_a1",
                "title": "Regular Expressions in Python (re module)",
                "type": "video",
                "duration": 40,
                "description": "Pattern matching with regex: search, match, findall, groups, and substitution.",
                "url": "https://realpython.com/regex-python/",
            },
        ],
    },

    "Lists & Tuples": {
        "core": [
            {
                "id": "lt_c1",
                "title": "Python Lists – Creation, Indexing & Methods",
                "type": "video",
                "duration": 25,
                "description": "append, insert, remove, pop, sort, reverse — all list operations.",
                "url": "https://realpython.com/python-lists-tuples/",
            },
            {
                "id": "lt_c2",
                "title": "Tuples vs Lists – When to Use Which",
                "type": "reading",
                "duration": 15,
                "description": "Understand the immutability of tuples and why it matters for your design.",
                "url": "https://realpython.com/python-tuple/",
            },
            {
                "id": "lt_c3",
                "title": "List & Tuple Exercises",
                "type": "exercise",
                "duration": 35,
                "description": "Sort a list, find duplicates, flatten a nested list, rotate elements, and more.",
                "url": "https://pynative.com/python-list-exercise/",
            },
            {
                "id": "lt_c4",
                "title": "Lists & Tuples Quiz",
                "type": "quiz",
                "duration": 10,
                "description": "15 MCQs on list operations, slicing, and tuple unpacking.",
                "url": "https://pynative.com/python-list-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "lt_a1",
                "title": "Nested Lists & 2D Matrices",
                "type": "exercise",
                "duration": 30,
                "description": "Work with 2D lists: matrix addition, transpose, and spiral traversal.",
                "url": "https://pynative.com/python-nested-list/",
            },
        ],
    },

    "Dictionaries & Sets": {
        "core": [
            {
                "id": "ds_c1",
                "title": "Python Dictionaries – Full Guide",
                "type": "video",
                "duration": 25,
                "description": "Create, access, update, and delete dictionary entries; use .keys(), .values(), .items().",
                "url": "https://realpython.com/python-dicts/",
            },
            {
                "id": "ds_c2",
                "title": "Python Sets – Operations & Use Cases",
                "type": "reading",
                "duration": 20,
                "description": "Union, intersection, difference, and when sets outperform lists.",
                "url": "https://realpython.com/python-sets/",
            },
            {
                "id": "ds_c3",
                "title": "Dictionary & Set Exercises",
                "type": "exercise",
                "duration": 35,
                "description": "Word frequency counter, phone book app, remove list duplicates with sets.",
                "url": "https://pynative.com/python-dictionary-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "ds_a1",
                "title": "defaultdict, Counter & OrderedDict",
                "type": "reading",
                "duration": 25,
                "description": "Use Python's collections module for powerful specialized dictionaries.",
                "url": "https://realpython.com/python-collections-module/",
            },
        ],
    },

    "File Handling": {
        "core": [
            {
                "id": "fh_c1",
                "title": "Reading & Writing Files in Python",
                "type": "video",
                "duration": 25,
                "description": "open(), read(), write(), and the 'with' statement for safe file handling.",
                "url": "https://realpython.com/read-write-files-python/",
            },
            {
                "id": "fh_c2",
                "title": "Working with CSV Files",
                "type": "reading",
                "duration": 20,
                "description": "Read and write CSV files using Python's built-in csv module.",
                "url": "https://realpython.com/python-csv/",
            },
            {
                "id": "fh_c3",
                "title": "File Handling Exercises",
                "type": "exercise",
                "duration": 30,
                "description": "Count words in a file, search for a pattern, merge two files, write a log.",
                "url": "https://pynative.com/python-file-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "fh_a1",
                "title": "JSON in Python – json Module",
                "type": "video",
                "duration": 25,
                "description": "Serialize and deserialize Python objects to/from JSON format.",
                "url": "https://realpython.com/python-json/",
            },
            {
                "id": "fh_a2",
                "title": "os & pathlib – File System Navigation",
                "type": "reading",
                "duration": 20,
                "description": "List, create, move, and delete files and directories with Python.",
                "url": "https://realpython.com/python-pathlib/",
            },
        ],
    },

    "Exception Handling": {
        "core": [
            {
                "id": "eh_c1",
                "title": "try / except / finally – Python Error Handling",
                "type": "video",
                "duration": 25,
                "description": "Catch and handle exceptions gracefully so your programs don't crash.",
                "url": "https://realpython.com/python-exceptions/",
            },
            {
                "id": "eh_c2",
                "title": "Built-in Exception Types",
                "type": "reading",
                "duration": 20,
                "description": "Learn ValueError, TypeError, FileNotFoundError, IndexError and when each is raised.",
                "url": "https://docs.python.org/3/library/exceptions.html",
            },
            {
                "id": "eh_c3",
                "title": "Exception Handling Exercises",
                "type": "exercise",
                "duration": 25,
                "description": "Safe integer input, safe file reader, divide-by-zero guard, custom exceptions.",
                "url": "https://pynative.com/python-exception-handling-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "eh_a1",
                "title": "Creating Custom Exception Classes",
                "type": "reading",
                "duration": 20,
                "description": "Define your own exception hierarchy by subclassing Exception.",
                "url": "https://realpython.com/python-exceptions/#user-defined-exceptions",
            },
        ],
    },

    "Object-Oriented Programming": {
        "core": [
            {
                "id": "oop_c1",
                "title": "Classes & Objects in Python",
                "type": "video",
                "duration": 35,
                "description": "Define classes, create objects, write __init__, and understand self.",
                "url": "https://realpython.com/python3-object-oriented-programming/",
            },
            {
                "id": "oop_c2",
                "title": "Instance vs Class vs Static Methods",
                "type": "reading",
                "duration": 25,
                "description": "Understand the difference between @staticmethod, @classmethod, and regular methods.",
                "url": "https://realpython.com/instance-class-and-static-methods-demystified/",
            },
            {
                "id": "oop_c3",
                "title": "OOP Exercises – Build Real Classes",
                "type": "exercise",
                "duration": 50,
                "description": "Build a BankAccount class, a Student class, and a simple Library system.",
                "url": "https://pynative.com/python-object-oriented-programming-oop-exercise/",
            },
            {
                "id": "oop_c4",
                "title": "OOP Quiz",
                "type": "quiz",
                "duration": 10,
                "description": "15 MCQs on classes, objects, __init__, self, encapsulation.",
                "url": "https://pynative.com/python-oop-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "oop_a1",
                "title": "Special (Dunder) Methods – __str__, __len__, __eq__",
                "type": "reading",
                "duration": 30,
                "description": "Make your classes behave like built-in Python types using magic methods.",
                "url": "https://realpython.com/operator-function-overloading/",
            },
        ],
    },

    "Inheritance & Polymorphism": {
        "core": [
            {
                "id": "inh_c1",
                "title": "Inheritance in Python",
                "type": "video",
                "duration": 30,
                "description": "Create child classes, call super(), and override parent methods.",
                "url": "https://realpython.com/inheritance-composition-python/",
            },
            {
                "id": "inh_c2",
                "title": "Polymorphism & Method Overriding",
                "type": "reading",
                "duration": 20,
                "description": "Write code that works with any subclass through a common interface.",
                "url": "https://realpython.com/python-polymorphism/",
            },
            {
                "id": "inh_c3",
                "title": "Inheritance Exercises",
                "type": "exercise",
                "duration": 40,
                "description": "Build an Animal → Dog/Cat hierarchy; a Shape → Circle/Rectangle hierarchy.",
                "url": "https://pynative.com/python-oop-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "inh_a1",
                "title": "Abstract Classes & Interfaces (abc module)",
                "type": "reading",
                "duration": 25,
                "description": "Enforce a common interface across subclasses using abstract base classes.",
                "url": "https://realpython.com/python-interface/",
            },
            {
                "id": "inh_a2",
                "title": "Multiple Inheritance & MRO",
                "type": "video",
                "duration": 25,
                "description": "How Python resolves method lookup with the Method Resolution Order (C3 linearisation).",
                "url": "https://realpython.com/python-multiple-inheritance/",
            },
        ],
    },

    "List Comprehensions & Lambdas": {
        "core": [
            {
                "id": "lcl_c1",
                "title": "List Comprehensions in Python",
                "type": "video",
                "duration": 20,
                "description": "Write concise, readable list-building expressions in one line.",
                "url": "https://realpython.com/list-comprehension-python/",
            },
            {
                "id": "lcl_c2",
                "title": "Lambda Functions, map() & filter()",
                "type": "reading",
                "duration": 20,
                "description": "Anonymous functions and Python's functional programming tools.",
                "url": "https://realpython.com/python-lambda/",
            },
            {
                "id": "lcl_c3",
                "title": "Comprehension & Lambda Exercises",
                "type": "exercise",
                "duration": 30,
                "description": "Rewrite loops as comprehensions; use map/filter to process lists.",
                "url": "https://pynative.com/python-list-comprehension-exercise/",
            },
        ],
        "advanced": [
            {
                "id": "lcl_a1",
                "title": "Dict & Set Comprehensions",
                "type": "reading",
                "duration": 15,
                "description": "Extend comprehension syntax to build dictionaries and sets in one line.",
                "url": "https://realpython.com/python-comprehensions/",
            },
        ],
    },

    "Modules & Packages": {
        "core": [
            {
                "id": "mp_c1",
                "title": "Python Modules & import Statement",
                "type": "video",
                "duration": 20,
                "description": "Create your own modules, use import/from-import, and understand __name__.",
                "url": "https://realpython.com/python-modules-packages/",
            },
            {
                "id": "mp_c2",
                "title": "Useful Standard Library Modules",
                "type": "reading",
                "duration": 25,
                "description": "Explore math, random, datetime, os, sys — modules every Python dev should know.",
                "url": "https://docs.python.org/3/library/",
            },
            {
                "id": "mp_c3",
                "title": "Modules Exercise",
                "type": "exercise",
                "duration": 25,
                "description": "Split a project into modules; use random for a dice game; use datetime for a timer.",
                "url": "https://pynative.com/python-module-quiz/",
            },
        ],
        "advanced": [
            {
                "id": "mp_a1",
                "title": "Creating & Publishing a Python Package",
                "type": "reading",
                "duration": 30,
                "description": "Structure a package with __init__.py, setup.py, and publish to PyPI.",
                "url": "https://realpython.com/pypi-publish-python-package/",
            },
        ],
    },

    "Decorators & Generators": {
        "core": [
            {
                "id": "dg_c1",
                "title": "Python Decorators – What & Why",
                "type": "video",
                "duration": 30,
                "description": "Wrap functions to add timing, logging, or access control without changing them.",
                "url": "https://realpython.com/primer-on-python-decorators/",
            },
            {
                "id": "dg_c2",
                "title": "Generators & yield in Python",
                "type": "reading",
                "duration": 25,
                "description": "Generate values lazily with yield for memory-efficient iteration.",
                "url": "https://realpython.com/introduction-to-python-generators/",
            },
        ],
        "advanced": [
            {
                "id": "dg_a1",
                "title": "Decorator Factory with Arguments",
                "type": "reading",
                "duration": 25,
                "description": "Write decorators that accept their own parameters using nested closures.",
                "url": "https://realpython.com/primer-on-python-decorators/#decorators-with-arguments",
            },
            {
                "id": "dg_a2",
                "title": "Generator Expressions & Advanced yield",
                "type": "exercise",
                "duration": 30,
                "description": "Use generator expressions in pipelines; implement your own range() with yield.",
                "url": "https://realpython.com/introduction-to-python-generators/#advanced-generator-methods",
            },
        ],
    },
}


def get_resources(topic: str, level: str) -> list:
    """
    Return the list of resources for a given topic and level.

    Parameters:
        topic (str) : one of the keys in ALL_RESOURCES
        level (str) : "core" or "advanced"

    Returns:
        list of resource dicts (empty list if not found)
    """
    return ALL_RESOURCES.get(topic, {}).get(level, [])


def get_all_topics() -> list:
    """Return the list of all topic names."""
    return TOPICS
