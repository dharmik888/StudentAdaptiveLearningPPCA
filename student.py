"""
student.py
==========
Defines the Student class — the central object of the entire project.

Concepts demonstrated:
  - Class definition with __init__
  - Instance attributes (self.name, self.score, etc.)
  - Instance methods (get_level, mark_done, update_progress, etc.)
  - Encapsulation: internal data managed through methods
  - Default parameter values
  - f-strings for output
  - Conditional logic inside methods
"""


class Student:
    """
    Represents a student using the adaptive learning system.

    Attributes:
        name          (str)  : student's full name
        roll_number   (str)  : unique student identifier
        learning_style(str)  : "visual", "reading", or "hands_on"
        daily_budget  (int)  : maximum study time per day in minutes
        weak_topics   (list) : topics the student finds difficult
        strong_topics (list) : topics the student is confident in
        quiz_scores   (dict) : topic → quiz score (0–100)
        completed     (list) : resource IDs the student has finished
        progress      (dict) : topic → percentage complete (0–100)
    """

    def __init__(self, name: str, roll_number: str,
                 learning_style: str, daily_budget: int):
        """
        Initialise a new student profile.

        Parameters:
            name           : student's full name
            roll_number    : unique roll number / ID
            learning_style : one of "visual", "reading", "hands_on"
            daily_budget   : study time available per day (minutes)
        """
        # ── Basic info ──────────────────────────────────────────
        self.name           = name
        self.roll_number    = roll_number
        self.learning_style = learning_style
        self.daily_budget   = daily_budget   # minutes per day

        # ── Topic strengths ──────────────────────────────────────
        self.weak_topics    = []   # list of topic strings
        self.strong_topics  = []   # list of topic strings

        # ── Quiz results ─────────────────────────────────────────
        # Maps topic name → {"score": int, "level": "core"/"advanced"}
        self.quiz_scores    = {}

        # ── Progress tracking ────────────────────────────────────
        self.completed      = []   # list of completed resource IDs
        self.progress       = {}   # topic → % complete (int 0–100)

    # ──────────────────────────────────────────────────────────────
    # QUIZ RESULT METHODS
    # ──────────────────────────────────────────────────────────────

    def save_quiz_result(self, topic: str, score: int, level: str):
        """
        Store the quiz result for a topic.

        Parameters:
            topic  : name of the topic tested
            score  : percentage score (0–100)
            level  : recommended level — "core" or "advanced"
        """
        self.quiz_scores[topic] = {"score": score, "level": level}

    def get_level(self, topic: str) -> str:
        """
        Return the recommended level for a topic.
        Defaults to "core" if no quiz has been taken yet.

        Conditional logic:
            - If quiz taken → use quiz result
            - Else          → default to "core"

        Parameters:
            topic : the topic to look up

        Returns:
            "core" or "advanced"
        """
        if topic in self.quiz_scores:
            return self.quiz_scores[topic]["level"]
        else:
            return "core"    # safe default for unevaluated topics

    def get_score(self, topic: str) -> int:
        """
        Return the quiz score for a topic.
        Returns 0 if no quiz taken.
        """
        if topic in self.quiz_scores:
            return self.quiz_scores[topic]["score"]
        else:
            return 0

    # ──────────────────────────────────────────────────────────────
    # COMPLETION TRACKING METHODS
    # ──────────────────────────────────────────────────────────────

    def mark_done(self, resource_id: str):
        """
        Mark a resource as completed.

        Uses an 'if' guard to prevent duplicates.

        Parameters:
            resource_id : the unique ID of the resource (e.g. "oop_c1")
        """
        if resource_id not in self.completed:
            self.completed.append(resource_id)

    def is_done(self, resource_id: str) -> bool:
        """
        Check whether a resource has been completed.

        Parameters:
            resource_id : unique resource ID

        Returns:
            True if completed, False otherwise
        """
        return resource_id in self.completed

    def calculate_progress(self, topic: str, all_resources: list) -> int:
        """
        Calculate the percentage of resources completed for a topic.

        Formula:
            progress = (completed_count / total_count) × 100

        Parameters:
            topic         : topic name
            all_resources : full list of resource dicts for that topic+level

        Returns:
            Integer percentage (0–100)
        """
        if len(all_resources) == 0:
            return 0    # avoid divide-by-zero

        completed_count = 0
        for resource in all_resources:
            if self.is_done(resource["id"]):
                completed_count += 1

        percentage = int((completed_count / len(all_resources)) * 100)
        self.progress[topic] = percentage    # update stored progress
        return percentage

    # ──────────────────────────────────────────────────────────────
    # DISPLAY METHODS
    # ──────────────────────────────────────────────────────────────

    def display_profile(self):
        """
        Print a formatted summary of the student's profile.
        Uses f-strings for clean output formatting.
        """
        print("\n" + "=" * 55)
        print(f"  STUDENT PROFILE")
        print("=" * 55)
        print(f"  Name           : {self.name}")
        print(f"  Roll Number    : {self.roll_number}")
        print(f"  Learning Style : {self.learning_style.replace('_', ' ').title()}")
        print(f"  Daily Budget   : {self.daily_budget} minutes")

        # Show weak/strong topics only if they exist
        if self.weak_topics:
            print(f"  Weak Topics    : {', '.join(self.weak_topics)}")
        if self.strong_topics:
            print(f"  Strong Topics  : {', '.join(self.strong_topics)}")

        # Show quiz results if any
        if self.quiz_scores:
            print(f"\n  Quiz Results:")
            for topic, result in self.quiz_scores.items():
                print(f"    {topic:<35} {result['score']:>3}%  →  {result['level'].upper()}")

        print("=" * 55)

    def __str__(self) -> str:
        """
        String representation of Student — called when you print(student).
        This is a special (dunder) method Python looks for automatically.
        """
        return f"Student({self.name}, Roll: {self.roll_number}, Style: {self.learning_style})"

    def __repr__(self) -> str:
        """
        Developer representation — useful for debugging.
        """
        return (f"Student(name={self.name!r}, roll={self.roll_number!r}, "
                f"style={self.learning_style!r}, budget={self.daily_budget})")
