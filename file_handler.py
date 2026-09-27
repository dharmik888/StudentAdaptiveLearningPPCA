"""
file_handler.py
===============
Handles saving and loading student profiles using JSON files.

Why JSON?
  - Human-readable (you can open the file in Notepad and read it)
  - Built into Python — no extra libraries needed
  - Easy to convert to/from Python dictionaries

Concepts demonstrated:
  - File I/O  : open(), read, write
  - json module : json.dump() and json.load()
  - 'with' statement : context manager (auto-closes file)
  - os module : check if file exists, create directories
  - Exception handling : catch FileNotFoundError, JSONDecodeError
  - Functions : each operation is a separate function
  - Dictionaries : profile stored and loaded as dict
"""

import json
import os

from student import Student


# ── Directory where all profile files are saved ──────────────
#  os.path.dirname(__file__) gives the folder this file is in
#  os.path.join builds a cross-platform path
SAVE_DIR = os.path.join(os.path.dirname(__file__), "data", "students")


def setup_save_directory():
    """
    Create the save directory if it doesn't already exist.
    os.makedirs with exist_ok=True won't raise an error if it exists.
    """
    os.makedirs(SAVE_DIR, exist_ok=True)


def get_profile_path(roll_number: str) -> str:
    """
    Build the file path for a student's profile.

    Example: roll "23CS101" → "data/students/23CS101.json"

    Parameters:
        roll_number : student's roll number

    Returns:
        Full file path as a string
    """
    # Replace any slashes or spaces in roll number to make a safe filename
    safe_name = roll_number.replace("/", "_").replace(" ", "_")
    return os.path.join(SAVE_DIR, f"{safe_name}.json")


def save_profile(student: Student):
    """
    Save a Student object to a JSON file.

    Serialisation:
      Python Student object → Python dictionary → JSON text → file

    The Student class has Enum-like attributes (strings) and lists,
    all of which are JSON-compatible directly.

    Parameters:
        student : the Student object to save
    """
    setup_save_directory()

    # Convert Student object → plain dictionary
    profile_data = {
        "name":           student.name,
        "roll_number":    student.roll_number,
        "learning_style": student.learning_style,
        "daily_budget":   student.daily_budget,
        "weak_topics":    student.weak_topics,
        "strong_topics":  student.strong_topics,
        "quiz_scores":    student.quiz_scores,   # already a dict
        "completed":      student.completed,     # already a list
        "progress":       student.progress,      # already a dict
    }

    file_path = get_profile_path(student.roll_number)

    # 'with' ensures the file is closed properly even if an error occurs
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(profile_data, file, indent=4)  # indent=4 → pretty formatted

    print(f"  Profile saved: {file_path}")


def load_profile(roll_number: str):
    """
    Load a Student profile from its JSON file.

    Deserialisation:
      JSON file → JSON text → Python dictionary → Student object

    Parameters:
        roll_number : roll number to load

    Returns:
        Student object if found, None if not found
    """
    file_path = get_profile_path(roll_number)

    # ── Check if file exists before trying to open it ────────────
    if not os.path.exists(file_path):
        return None    # profile does not exist yet

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)    # JSON text → Python dictionary

        # Reconstruct the Student object from the dictionary
        student = Student(
            name           = data["name"],
            roll_number    = data["roll_number"],
            learning_style = data["learning_style"],
            daily_budget   = data["daily_budget"],
        )

        # Restore all stored data back into the object
        student.weak_topics   = data.get("weak_topics",  [])
        student.strong_topics = data.get("strong_topics",[])
        student.quiz_scores   = data.get("quiz_scores",  {})
        student.completed     = data.get("completed",    [])
        student.progress      = data.get("progress",     {})

        return student

    except json.JSONDecodeError:
        # File exists but is not valid JSON (e.g. corrupted)
        print(f"  Error: Profile file is corrupted: {file_path}")
        return None

    except KeyError as e:
        # A required key is missing from the file
        print(f"  Error: Missing field in profile: {e}")
        return None


def list_saved_profiles() -> list:
    """
    Return a list of all saved roll numbers.

    Reads the save directory and returns filenames (without .json).

    Returns:
        List of roll number strings, e.g. ["23CS101", "23CS102"]
    """
    setup_save_directory()

    saved = []

    # os.listdir returns all file/folder names in the directory
    for filename in os.listdir(SAVE_DIR):
        if filename.endswith(".json"):
            # Remove the ".json" suffix to get the roll number
            roll = filename[:-5]   # [:-5] removes last 5 chars (".json")
            saved.append(roll)

    return saved


def delete_profile(roll_number: str) -> bool:
    """
    Delete a student's saved profile.

    Parameters:
        roll_number : roll number of the profile to delete

    Returns:
        True if deleted, False if file was not found
    """
    file_path = get_profile_path(roll_number)

    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    else:
        return False
