"""
demo.py
=======
Automated demonstration of the Adaptive Learning Engine.
Runs WITHOUT any user input — perfect for showcasing the project.

Shows:
  1. Student profile creation  (3 students, fully loaded with quiz data)
  2. Quiz conditional logic    (level determination table)
  3. Adaptive path for Alice   (Visual learner, OOP struggles)
  4. Full daily plan for Bob   (Hands-On learner, weak-topic-first)
  5. Full daily plan for Priya (Reading learner, advanced in some areas)
  6. Progress tracking         (visual progress bar)
  7. Student comparison table  (quiz scores across all 15 topics)

Run with:
    python demo.py
"""

import sys
import os

# Fix Unicode output on Windows (cp1252 → utf-8)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from student        import Student
from quiz           import determine_level, get_score_label
from resources      import get_resources, get_all_topics
from recommendation import (generate_learning_path, generate_full_plan,
                             display_path, prioritise_topics)


# ─────────────────────────────────────────────────────────────
#  DUMMY DATA — All 15 Topics & Quiz Scores
# ─────────────────────────────────────────────────────────────

ALL_TOPICS = get_all_topics()

# Alice: Visual learner — strong at loops/strings, weak at OOP & advanced topics
ALICE_SCORES = {
    "Variables & Data Types":          (82, "advanced"),
    "Operators & Expressions":         (75, "advanced"),
    "Control Flow":                    (78, "advanced"),
    "Loops":                           (88, "advanced"),
    "Functions":                       (65, "core"),
    "Strings":                         (85, "advanced"),
    "Lists & Tuples":                  (72, "advanced"),
    "Dictionaries & Sets":             (60, "core"),
    "File Handling":                   (55, "core"),
    "Exception Handling":              (48, "core"),
    "Object-Oriented Programming":     (52, "core"),
    "Inheritance & Polymorphism":      (40, "core"),
    "List Comprehensions & Lambdas":   (58, "core"),
    "Modules & Packages":              (63, "core"),
    "Decorators & Generators":         (35, "core"),
}

# Bob: Hands-On learner — strong in basics, weak in file & exception handling
BOB_SCORES = {
    "Variables & Data Types":          (85, "advanced"),
    "Operators & Expressions":         (80, "advanced"),
    "Control Flow":                    (83, "advanced"),
    "Loops":                           (79, "advanced"),
    "Functions":                       (77, "advanced"),
    "Strings":                         (70, "advanced"),
    "Lists & Tuples":                  (68, "core"),
    "Dictionaries & Sets":             (62, "core"),
    "File Handling":                   (38, "core"),
    "Exception Handling":              (42, "core"),
    "Object-Oriented Programming":     (55, "core"),
    "Inheritance & Polymorphism":      (48, "core"),
    "List Comprehensions & Lambdas":   (73, "advanced"),
    "Modules & Packages":              (60, "core"),
    "Decorators & Generators":         (30, "core"),
}

# Priya: Reading learner — advanced in theory, weak in OOP/advanced topics
PRIYA_SCORES = {
    "Variables & Data Types":          (92, "advanced"),
    "Operators & Expressions":         (88, "advanced"),
    "Control Flow":                    (90, "advanced"),
    "Loops":                           (85, "advanced"),
    "Functions":                       (87, "advanced"),
    "Strings":                         (91, "advanced"),
    "Lists & Tuples":                  (83, "advanced"),
    "Dictionaries & Sets":             (80, "advanced"),
    "File Handling":                   (72, "advanced"),
    "Exception Handling":              (76, "advanced"),
    "Object-Oriented Programming":     (45, "core"),
    "Inheritance & Polymorphism":      (38, "core"),
    "List Comprehensions & Lambdas":   (65, "core"),
    "Modules & Packages":              (70, "advanced"),
    "Decorators & Generators":         (32, "core"),
}


def line(char="─", width=62):
    print(char * width)


def section(title):
    print("\n" + "=" * 62)
    print(f"  {title}")
    print("=" * 62)


def make_bar(progress, width=20):
    """Return a block-style progress bar string."""
    filled = int(progress * width / 100)
    return "█" * filled + "░" * (width - filled)


# ─────────────────────────────────────────────────────────────

def demo_1_student_profiles():
    section("DEMO 1: Creating Student Profiles (OOP)")

    # ── Student A: Alice — Visual learner ───────────────────────
    alice = Student(
        name           = "Alice Sharma",
        roll_number    = "23CS101",
        learning_style = "visual",
        daily_budget   = 60,
    )
    alice.weak_topics   = ["OOP", "inheritance", "decorators", "exception handling"]
    alice.strong_topics = ["loops", "lists", "strings", "variables"]

    for topic, (score, level) in ALICE_SCORES.items():
        alice.save_quiz_result(topic, score, level)

    # ── Student B: Bob — Hands-On learner ───────────────────────
    bob = Student(
        name           = "Bob Patel",
        roll_number    = "23CS102",
        learning_style = "hands_on",
        daily_budget   = 90,
    )
    bob.weak_topics   = ["file handling", "exception handling", "decorators"]
    bob.strong_topics = ["functions", "control flow", "loops", "operators"]

    for topic, (score, level) in BOB_SCORES.items():
        bob.save_quiz_result(topic, score, level)

    # ── Student C: Priya — Reading learner ──────────────────────
    priya = Student(
        name           = "Priya Nair",
        roll_number    = "23CS103",
        learning_style = "reading",
        daily_budget   = 75,
    )
    priya.weak_topics   = ["OOP", "inheritance", "decorators", "list comprehensions"]
    priya.strong_topics = ["strings", "control flow", "functions", "file handling"]

    for topic, (score, level) in PRIYA_SCORES.items():
        priya.save_quiz_result(topic, score, level)

    print("\n  Three students created using the Student class:\n")
    alice.display_profile()
    bob.display_profile()
    priya.display_profile()

    print("\n  Demonstrating __str__ and __repr__ dunder methods:")
    print(f"  str(alice)  → {alice}")
    print(f"  repr(bob)   → {repr(bob)}")
    print(f"  str(priya)  → {priya}")

    return alice, bob, priya


# ─────────────────────────────────────────────────────────────

def demo_2_quiz_conditional_logic():
    section("DEMO 2: Quiz Conditional Logic — Level Determination")

    print("""
  The engine uses if/elif/else to determine the student's level:

      if score >= 70:
          return "advanced"     ← ready for harder content
      elif score >= 40:
          return "core"         ← needs more practice
      else:
          return "core"         ← needs fundamentals first
    """)

    test_cases = [
        (95, "Perfect score — immediate Advanced"),
        (78, "Good — Advanced level unlocked"),
        (70, "Exactly on the Advanced threshold"),
        (65, "Just below — stays at Core"),
        (55, "Average — Core revision needed"),
        (40, "Borderline — Core recommended"),
        (25, "Low — start from fundamentals"),
        (10, "Very low — Core basics required"),
    ]

    print(f"  {'Score':>6}  {'Level':>10}  {'Bar':>12}  Label")
    line()
    for score, description in test_cases:
        level = determine_level(score)
        label = get_score_label(score)
        bar   = make_bar(score, width=10)
        print(f"  {score:>5}%  {level:>10}  [{bar}]  {label}")

    print()


# ─────────────────────────────────────────────────────────────

def demo_3_adaptive_path(alice: Student):
    section("DEMO 3: Adaptive Path for Alice (Visual, Weak: OOP / Exception / Decorators)")

    from recommendation import score_resource

    for topic in ["Object-Oriented Programming", "Exception Handling", "Decorators & Generators"]:
        level     = alice.get_level(topic)
        resources = get_resources(topic, level)

        print(f"\n  ── Topic: {topic} ──")
        print(f"  Alice's level: {level.upper()}  |  Style: visual  |  Budget: {alice.daily_budget} min")
        print(f"\n  Resources scored & ranked for Alice:")

        scored = sorted(
            resources,
            key=lambda r: score_resource(r, alice.learning_style,
                                         alice.weak_topics, alice.strong_topics),
            reverse=True
        )
        for r in scored:
            s = score_resource(r, alice.learning_style, alice.weak_topics, alice.strong_topics)
            print(f"    Score {s:2}  [{r['type']:8}]  {r['title']}  ({r['duration']} min)")

        path = generate_learning_path(alice, topic, resources)
        display_path(path, topic, level, alice.name)


# ─────────────────────────────────────────────────────────────

def demo_4_full_plan_bob(bob: Student):
    section("DEMO 4: Full Daily Plan for Bob (Hands-On, 90 min budget)")

    print(f"\n  Bob's weak topics (shown first in plan): {bob.weak_topics}")
    print(f"  Bob's strong topics: {bob.strong_topics}")
    print(f"\n  Bob's Quiz Scores — All 15 Topics:")
    line()
    for topic, result in bob.quiz_scores.items():
        bar   = make_bar(result['score'], width=15)
        level = result['level'].upper()
        print(f"  {topic:<38} {result['score']:>3}%  [{bar}]  {level}")
    line()

    ordered = prioritise_topics(ALL_TOPICS, bob.weak_topics)
    print(f"\n  Topic Order After Prioritisation (weak topics first):")
    for i, t in enumerate(ordered, 1):
        marker = "  ← WEAK" if any(w.lower() in t.lower() for w in bob.weak_topics) else ""
        print(f"    {i:>2}. {t}{marker}")

    print(f"\n  Generating today's full plan (90 min budget)...")
    plan = generate_full_plan(bob, ALL_TOPICS, get_resources)

    if not plan:
        print("\n  All resources complete for today!")
    else:
        for topic, path in plan.items():
            level = bob.get_level(topic)
            display_path(path, topic, level, bob.name)


# ─────────────────────────────────────────────────────────────

def demo_5_full_plan_priya(priya: Student):
    section("DEMO 5: Full Daily Plan for Priya (Reading Learner, 75 min budget)")

    print(f"\n  Priya's weak topics (shown first in plan): {priya.weak_topics}")
    print(f"  Priya's strong topics: {priya.strong_topics}")
    print(f"\n  Priya's Quiz Scores — All 15 Topics:")
    line()
    for topic, result in priya.quiz_scores.items():
        bar   = make_bar(result['score'], width=15)
        level = result['level'].upper()
        print(f"  {topic:<38} {result['score']:>3}%  [{bar}]  {level}")
    line()

    print(f"\n  Generating today's full plan (75 min budget)...")
    plan = generate_full_plan(priya, ALL_TOPICS, get_resources)

    if not plan:
        print("\n  All resources complete for today!")
    else:
        for topic, path in plan.items():
            level = priya.get_level(topic)
            display_path(path, topic, level, priya.name)


# ─────────────────────────────────────────────────────────────

def demo_6_progress_tracking(alice: Student):
    section("DEMO 6: Progress Tracking as Resources Are Completed")

    for topic in ["Control Flow", "Loops", "Object-Oriented Programming"]:
        resources = get_resources(topic, alice.get_level(topic))
        total     = len(resources)

        # Reset completions for this topic so demo is clean
        for r in resources:
            if r["id"] in alice.completed:
                alice.completed.remove(r["id"])

        print(f"\n  Topic: {topic}  |  Level: {alice.get_level(topic).upper()}  |  Total Resources: {total}")
        line()

        initial = alice.calculate_progress(topic, resources)
        print(f"  Start  → [{make_bar(initial)}] {initial:>3}%  (0 / {total} done)")

        for i, resource in enumerate(resources, 1):
            alice.mark_done(resource["id"])
            progress = alice.calculate_progress(topic, resources)
            bar      = make_bar(progress)
            title    = resource['title'][:32]
            print(f"  +'{title}...'")
            print(f"         → [{bar}] {progress:>3}%  ({i} / {total} done)")

        if progress == 100:
            print(f"\n  ✓ All {total} resources complete for '{topic}'!")
            print(f"  → Alice can now unlock ADVANCED content for this topic!")
        print()


# ─────────────────────────────────────────────────────────────

def demo_7_student_comparison(alice: Student, bob: Student, priya: Student):
    section("DEMO 7: Student Comparison — Quiz Scores Across All 15 Topics")

    col_w = 38
    print(f"\n  {'Topic':<{col_w}} {'Alice':>7} {'Bob':>7} {'Priya':>7}  Best")
    line(width=72)

    for topic in ALL_TOPICS:
        a = alice.get_score(topic)
        b = bob.get_score(topic)
        p = priya.get_score(topic)

        best_score = max(a, b, p)
        if best_score == p:
            best = "Priya"
        elif best_score == b:
            best = "Bob  "
        else:
            best = "Alice"

        # Flag topics where everyone scored below 70
        flag = "  ⚠ All need work" if max(a, b, p) < 70 else ""
        print(f"  {topic:<{col_w}} {a:>6}% {b:>6}% {p:>6}%  {best}{flag}")

    line(width=72)

    avg_a = sum(ALICE_SCORES[t][0] for t in ALL_TOPICS) // len(ALL_TOPICS)
    avg_b = sum(BOB_SCORES[t][0]   for t in ALL_TOPICS) // len(ALL_TOPICS)
    avg_p = sum(PRIYA_SCORES[t][0] for t in ALL_TOPICS) // len(ALL_TOPICS)
    print(f"  {'CLASS AVERAGE':<{col_w}} {avg_a:>6}% {avg_b:>6}% {avg_p:>6}%")
    line(width=72)

    adv_a = sum(1 for _, (_, lvl) in ALICE_SCORES.items() if lvl == "advanced")
    adv_b = sum(1 for _, (_, lvl) in BOB_SCORES.items()   if lvl == "advanced")
    adv_p = sum(1 for _, (_, lvl) in PRIYA_SCORES.items() if lvl == "advanced")
    print(f"  {'Topics at ADVANCED level':<{col_w}} {adv_a:>6}  {adv_b:>6}  {adv_p:>6}")
    print(f"  {'Topics at CORE level':<{col_w}} {len(ALL_TOPICS)-adv_a:>6}  {len(ALL_TOPICS)-adv_b:>6}  {len(ALL_TOPICS)-adv_p:>6}")
    line(width=72)


# ─────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 62)
    print("  ADAPTIVE LEARNING ENGINE — AUTOMATED DEMO")
    print("  Python Programming Core & Advanced | 2nd Year")
    print("=" * 62)
    print("  No user input required. Running all demos automatically.")
    print("  3 Students  |  15 Topics  |  7 Demos\n")

    alice, bob, priya = demo_1_student_profiles()
    demo_2_quiz_conditional_logic()
    demo_3_adaptive_path(alice)
    demo_4_full_plan_bob(bob)
    demo_5_full_plan_priya(priya)
    demo_6_progress_tracking(alice)
    demo_7_student_comparison(alice, bob, priya)

    print("=" * 62)
    print("  Demo complete!  Run 'python main.py' for the interactive version.")
    print("=" * 62 + "\n")


if __name__ == "__main__":
    main()
