"""
main.py
=======
Entry point for the Adaptive Student Learning Path Recommendation Engine.
Subject: Python Programming Core & Advanced (2nd Year)

This file ties all modules together:
  student.py        → Student class
  quiz.py           → Diagnostic quiz
  resources.py      → All learning resources
  recommendation.py → Path generation
  file_handler.py   → Save / load profiles

How to run:
    python main.py

Concepts demonstrated here:
  - Importing from other modules
  - Functions that call other functions
  - while loop for the main menu
  - if/elif/else for menu routing
  - try/except for input validation
  - String methods: .strip(), .upper(), .title()
  - f-strings throughout
"""

# ── Standard library ─────────────────────────────────────────
import os
import sys

# ── Fix Unicode output on Windows (cp1252 → utf-8) ───────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

# ── Add project folder to Python's search path ───────────────
# This ensures Python can find all our modules regardless of
# where the script is launched from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ── Our own modules ───────────────────────────────────────────
from student       import Student
from quiz          import run_quiz, QUESTION_BANK
from resources     import get_resources, get_all_topics
from recommendation import (generate_learning_path, generate_full_plan,
                             display_path, prioritise_topics)
from file_handler  import (save_profile, load_profile,
                            list_saved_profiles, delete_profile)


# ─────────────────────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║  ADAPTIVE STUDENT LEARNING PATH RECOMMENDATION ENGINE        ║
║  Subject: Python Programming  |  Core & Advanced             ║
║  2nd Year B.Tech / BSc Computer Science                      ║
╚══════════════════════════════════════════════════════════════╝
"""

ALL_TOPICS = get_all_topics()   # all 15 Python topics from resources.py


# ─────────────────────────────────────────────────────────────
#  INPUT HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────

def get_int_input(prompt: str, low: int, high: int) -> int:
    """
    Ask the user for an integer within [low, high].
    Keeps asking until valid input is received.

    Parameters:
        prompt : the question to display
        low    : minimum acceptable value (inclusive)
        high   : maximum acceptable value (inclusive)

    Returns:
        A valid integer in [low, high]
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if low <= value <= high:
                return value
            else:
                print(f"  Please enter a number between {low} and {high}.")
        except ValueError:
            print("  Invalid input — please enter a whole number.")


def get_nonempty_input(prompt: str) -> str:
    """
    Ask the user for a non-empty string.
    Keeps asking until the user types something.

    Parameters:
        prompt : the question to display

    Returns:
        Non-empty stripped string
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty.")


# ─────────────────────────────────────────────────────────────
#  PROFILE SETUP
# ─────────────────────────────────────────────────────────────

def create_new_profile() -> Student:
    """
    Interactive wizard to create a brand-new student profile.

    Collects: name, roll number, learning style, daily budget,
              weak topics, strong topics.

    Returns:
        A new Student object (already saved to file)
    """
    print("\n" + "─" * 55)
    print("  CREATE NEW PROFILE")
    print("─" * 55)

    name        = get_nonempty_input("  Your full name    : ")
    roll_number = get_nonempty_input("  Roll number       : ")

    # ── Check for duplicate ──────────────────────────────────────
    if load_profile(roll_number) is not None:
        print(f"\n  A profile for roll '{roll_number}' already exists.")
        overwrite = input("  Overwrite it? (y/n): ").strip().lower()
        if overwrite != "y":
            print("  Profile creation cancelled.")
            return None

    # ── Learning style ────────────────────────────────────────────
    print("\n  Learning Style:")
    print("    1. Visual    – I prefer watching videos")
    print("    2. Reading   – I prefer reading articles and docs")
    print("    3. Hands-On  – I prefer doing exercises and projects")

    style_choice = get_int_input("  Choose (1/2/3): ", 1, 3)
    style_map    = {1: "visual", 2: "reading", 3: "hands_on"}
    learning_style = style_map[style_choice]

    # ── Daily study budget ────────────────────────────────────────
    print("\n  Daily Study Budget:")
    print("    1.  30 min  – Light session")
    print("    2.  60 min  – Standard session")
    print("    3.  90 min  – Intensive session")
    print("    4. 120 min  – Full day session")

    budget_choice = get_int_input("  Choose (1/2/3/4): ", 1, 4)
    budget_map    = {1: 30, 2: 60, 3: 90, 4: 120}
    daily_budget  = budget_map[budget_choice]

    # ── Create the student object ──────────────────────────────────
    student = Student(name, roll_number, learning_style, daily_budget)

    # ── Weak topics (optional) ─────────────────────────────────────
    print("\n  Which Python topics do you find DIFFICULT?")
    print("  (Type keywords separated by commas, or press Enter to skip)")
    print("  e.g. OOP, recursion, decorators, file handling")
    raw_weak = input("  Weak topics: ").strip()

    if raw_weak:
        student.weak_topics = [t.strip() for t in raw_weak.split(",") if t.strip()]

    # ── Strong topics (optional) ──────────────────────────────────
    print("\n  Which Python topics are you CONFIDENT in?")
    raw_strong = input("  Strong topics: ").strip()

    if raw_strong:
        student.strong_topics = [t.strip() for t in raw_strong.split(",") if t.strip()]

    # ── Save and confirm ──────────────────────────────────────────
    save_profile(student)
    print(f"\n  Profile created for {student.name} (Roll: {student.roll_number})")
    return student


def login_existing_profile() -> Student:
    """
    Load an existing student profile by roll number.

    Returns:
        Loaded Student object, or None if not found
    """
    print("\n─" * 55)
    saved = list_saved_profiles()

    if not saved:
        print("  No saved profiles found. Please create a new profile.")
        return None

    print("  Saved profiles:")
    for roll in saved:
        print(f"    - {roll}")

    roll_number = get_nonempty_input("\n  Enter your roll number: ")
    student = load_profile(roll_number)

    if student is None:
        print(f"  No profile found for roll number '{roll_number}'.")
        return None

    print(f"\n  Welcome back, {student.name}!")
    return student


# ─────────────────────────────────────────────────────────────
#  MENU ACTIONS
# ─────────────────────────────────────────────────────────────

def menu_take_quiz(student: Student):
    """
    Let the student choose a topic and take a diagnostic quiz.
    Saves result to the student profile.
    """
    print("\n  Available topics:")
    for i, topic in enumerate(ALL_TOPICS, start=1):
        already_done = topic in student.quiz_scores
        status = f" [Score: {student.get_score(topic)}%]" if already_done else ""
        print(f"    {i:2}. {topic}{status}")

    choice = get_int_input("\n  Select topic number: ", 1, len(ALL_TOPICS))
    topic  = ALL_TOPICS[choice - 1]

    # ── Confirm retake if already done ───────────────────────────
    if topic in student.quiz_scores:
        print(f"\n  You already scored {student.get_score(topic)}% on this topic.")
        retake = input("  Retake quiz? (y/n): ").strip().lower()
        if retake != "y":
            return

    # ── Run the quiz ───────────────────────────────────────────────
    result = run_quiz(topic)

    # ── Save result to student profile ─────────────────────────────
    student.save_quiz_result(topic, result["score"], result["level"])
    save_profile(student)

    print(f"  Result saved! {topic} → {result['level'].upper()} level unlocked.")


def menu_view_path(student: Student):
    """
    Generate and display the learning path for a selected topic.
    """
    print("\n  Available topics:")
    for i, topic in enumerate(ALL_TOPICS, start=1):
        level    = student.get_level(topic)
        score    = student.get_score(topic)
        resources = get_resources(topic, level)
        progress = student.calculate_progress(topic, resources)
        print(f"    {i:2}. {topic:<38} [{level.upper():8}] {progress:3}% done")

    print(f"\n     0. Show TODAY'S plan for ALL topics")

    choice = get_int_input("\n  Select topic (0 for all): ", 0, len(ALL_TOPICS))

    if choice == 0:
        # ── Full daily plan ─────────────────────────────────────────
        plan = generate_full_plan(student, ALL_TOPICS, get_resources)

        if not plan:
            print("\n  You have completed all resources! Great work!")
            return

        print(f"\n  TODAY'S STUDY PLAN  ({student.daily_budget} min budget)")
        print("=" * 62)
        for topic, path in plan.items():
            level = student.get_level(topic)
            display_path(path, topic, level, student.name)

    else:
        # ── Single topic path ───────────────────────────────────────
        topic     = ALL_TOPICS[choice - 1]
        level     = student.get_level(topic)
        resources = get_resources(topic, level)
        path      = generate_learning_path(student, topic, resources)

        display_path(path, topic, level, student.name)


def menu_mark_done(student: Student):
    """
    Let the student mark a resource as completed.
    """
    print("\n  Select topic to mark progress in:")
    for i, topic in enumerate(ALL_TOPICS, start=1):
        print(f"    {i:2}. {topic}")

    topic_choice = get_int_input("  Topic number: ", 1, len(ALL_TOPICS))
    topic        = ALL_TOPICS[topic_choice - 1]
    level        = student.get_level(topic)
    resources    = get_resources(topic, level)

    if not resources:
        print("  No resources found for this topic and level.")
        return

    # ── Show resources with their completion status ────────────────
    print(f"\n  Resources for: {topic}  [{level.upper()}]")
    print("─" * 62)
    pending_resources = []

    for i, r in enumerate(resources, start=1):
        done   = student.is_done(r["id"])
        status = "[DONE]" if done else "      "
        print(f"    {i:2}. {status} {r['title']}  ({r['duration']} min)")
        if not done:
            pending_resources.append(r)

    if not pending_resources:
        print("\n  All resources in this topic are already completed!")
        return

    # ── Ask which to mark done ────────────────────────────────────
    print("\n  Full list above — enter the number of the resource to mark done:")
    res_choice = get_int_input("  Resource number: ", 1, len(resources))
    chosen     = resources[res_choice - 1]

    if student.is_done(chosen["id"]):
        print(f"  '{chosen['title']}' is already marked as done.")
        return

    student.mark_done(chosen["id"])

    # Recalculate and display progress
    progress = student.calculate_progress(topic, resources)
    save_profile(student)

    print(f"\n  Marked as done: {chosen['title']}")
    print(f"  Progress in {topic}: {progress}%")

    # Conditional: celebrate if topic is complete
    if progress == 100:
        print(f"\n  Congratulations! You have completed all {level.upper()}")
        print(f"  resources for {topic}!")
        if level == "core":
            print(f"  Take the quiz again to unlock ADVANCED content!")


def menu_view_progress(student: Student):
    """
    Display a progress dashboard showing all topics and completion %.
    """
    print("\n" + "=" * 62)
    print(f"  PROGRESS DASHBOARD  —  {student.name}")
    print("=" * 62)
    print(f"  {'Topic':<38} {'Level':<12} {'Progress'}")
    print("─" * 62)

    total_resources = 0
    total_done      = 0

    for topic in ALL_TOPICS:
        level     = student.get_level(topic)
        resources = get_resources(topic, level)
        progress  = student.calculate_progress(topic, resources)

        # Count totals for overall percentage
        total_resources += len(resources)
        done_count       = sum(1 for r in resources if student.is_done(r["id"]))
        total_done      += done_count

        # Build a simple progress bar (20 characters wide)
        filled = progress // 5   # each '█' = 5%
        bar    = "█" * filled + "░" * (20 - filled)

        # Show quiz score if taken, else show "no quiz"
        score_str = f"{student.get_score(topic)}%" if topic in student.quiz_scores else "  — "

        print(f"  {topic:<38} {level:<12} [{bar}] {progress:3}%")

    # Overall progress summary
    overall = int((total_done / total_resources) * 100) if total_resources else 0
    print("─" * 62)
    print(f"  {'OVERALL PROGRESS':<38} {'':12} {overall}%")
    print("=" * 62)
    print(f"  Completed: {total_done} / {total_resources} resources\n")


def menu_update_topics(student: Student):
    """
    Let the student update their weak and strong topic lists.
    """
    print(f"\n  Current weak topics  : {', '.join(student.weak_topics)  or 'None'}")
    print(f"  Current strong topics: {', '.join(student.strong_topics) or 'None'}")

    print("\n  Enter new weak topics (comma-separated), or press Enter to keep current:")
    raw = input("  Weak topics: ").strip()
    if raw:
        student.weak_topics = [t.strip() for t in raw.split(",") if t.strip()]

    print("\n  Enter new strong topics (comma-separated), or press Enter to keep current:")
    raw = input("  Strong topics: ").strip()
    if raw:
        student.strong_topics = [t.strip() for t in raw.split(",") if t.strip()]

    save_profile(student)
    print("  Topics updated and saved!")


# ─────────────────────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────────────────────

def show_main_menu(student: Student):
    """
    Display the main menu and return the user's choice.
    """
    print("\n" + "─" * 55)
    print(f"  Hello, {student.name}  |  Budget: {student.daily_budget} min/day")
    print("─" * 55)
    print("   1.  Take Diagnostic Quiz")
    print("   2.  View My Learning Path")
    print("   3.  Mark Resource as Completed")
    print("   4.  View Progress Dashboard")
    print("   5.  Update Weak / Strong Topics")
    print("   6.  View My Profile")
    print("   0.  Exit")
    print("─" * 55)

    return get_int_input("  Enter choice: ", 0, 6)


def run_app():
    """
    Main application loop.

    Steps:
      1. Show welcome banner
      2. Ask: new or existing profile
      3. Load/create student
      4. Loop: show menu → handle choice → repeat until exit
    """
    print(BANNER)

    # ── Step 1: Login or register ─────────────────────────────────
    print("  Welcome! Please select an option:")
    print("    1. Create a new profile")
    print("    2. Load existing profile")

    start_choice = get_int_input("  Choice (1 or 2): ", 1, 2)

    if start_choice == 1:
        student = create_new_profile()
    else:
        student = login_existing_profile()

    # If profile creation/login failed, exit gracefully
    if student is None:
        print("\n  Exiting. Please run the program again.")
        return

    # ── Step 2: Main application loop ─────────────────────────────
    while True:
        choice = show_main_menu(student)

        if choice == 0:
            print(f"\n  Goodbye, {student.name}! Keep learning Python!\n")
            break

        elif choice == 1:
            menu_take_quiz(student)

        elif choice == 2:
            menu_view_path(student)

        elif choice == 3:
            menu_mark_done(student)

        elif choice == 4:
            menu_view_progress(student)

        elif choice == 5:
            menu_update_topics(student)

        elif choice == 6:
            student.display_profile()

        # After each action, auto-save the profile
        save_profile(student)


# ─────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # This block only runs when you execute: python main.py
    # It does NOT run when this file is imported by another module
    run_app()
