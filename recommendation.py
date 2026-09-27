"""
recommendation.py
=================
The Adaptive Recommendation Engine — selects and orders resources
dynamically based on each student's profile.

Key adaptive decisions made here (ALL using conditional logic):
  1. Which LEVEL to use per topic   → quiz result or default
  2. Which RESOURCE TYPE to prefer  → based on learning style
  3. Which topics to PRIORITISE     → based on weak topics
  4. HOW MANY resources to include  → based on daily time budget
  5. Whether to ADD a challenge     → if budget allows

Concepts demonstrated:
  - Functions with multiple parameters
  - Lists: sorting, filtering, appending, slicing
  - Dictionaries: looking up style preferences
  - for loops: iterating over resources
  - if/elif/else: all adaptive decisions
  - List comprehensions: filtering completed resources
  - Lambda with sorted(): custom resource sorting
  - Constants: STYLE_PREFERENCE, TYPE_ICON
"""

# ─────────────────────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────────────────────

# Maps each learning style to its preferred resource types (in priority order).
# Index 0 = most preferred, Index 4 = least preferred.
# Used in score_resource() to give a higher score to preferred types.
STYLE_PREFERENCE = {
    "visual":    ["video",    "exercise", "quiz",     "reading", "project"],
    "reading":   ["reading",  "quiz",     "video",    "exercise","project"],
    "hands_on":  ["exercise", "project",  "video",    "reading", "quiz"],
}

# Icons for displaying resource types in the terminal
TYPE_ICON = {
    "video":    "[VIDEO]",
    "reading":  "[READ] ",
    "exercise": "[EXS]  ",
    "quiz":     "[QUIZ] ",
    "project":  "[PROJ] ",
}


# ─────────────────────────────────────────────────────────────
#  SCORING FUNCTION
# ─────────────────────────────────────────────────────────────

def score_resource(resource: dict, learning_style: str,
                   weak_topics: list, strong_topics: list) -> int:
    """
    Calculate a priority score for a single resource.

    Higher score = should appear earlier in the recommended path.

    Scoring formula:
        score = style_score + weak_bonus - strong_penalty + duration_bonus

    Parameters:
        resource       : a resource dict (id, title, type, duration, ...)
        learning_style : "visual", "reading", or "hands_on"
        weak_topics    : list of topics the student finds difficult
        strong_topics  : list of topics the student is confident in

    Returns:
        Integer score
    """
    score = 0

    # ── 1. Style score (0–4) ─────────────────────────────────────
    # Resources matching the student's preferred style get a higher score
    preference_list = STYLE_PREFERENCE.get(learning_style, STYLE_PREFERENCE["reading"])

    resource_type = resource.get("type", "reading")

    if resource_type in preference_list:
        # Resources earlier in the list (more preferred) get higher score
        # Score = 4 for top preference, 3 for second, etc.
        position = preference_list.index(resource_type)
        score += (4 - position)    # max 4, min 0
    # If type not in list at all, score stays 0

    # ── 2. Weak-topic bonus (+3) ─────────────────────────────────
    # Resources whose title contains a weak keyword get a boost
    # This ensures struggling students see these resources first
    title_lower = resource.get("title", "").lower()

    for weak_word in weak_topics:
        if weak_word.lower() in title_lower:
            score += 3    # significant boost for weak-topic resources
            break         # only add bonus once per resource

    # ── 3. Strong-topic penalty (-1) ────────────────────────────
    # Don't push resources the student already knows well
    for strong_word in strong_topics:
        if strong_word.lower() in title_lower:
            score -= 1
            break

    # ── 4. Duration bonus (+1 for short resources) ───────────────
    # Slightly favour shorter resources to keep momentum going
    duration = resource.get("duration", 60)
    if duration <= 20:
        score += 1    # short & sweet

    return score


# ─────────────────────────────────────────────────────────────
#  TOPIC PRIORITISATION
# ─────────────────────────────────────────────────────────────

def prioritise_topics(all_topics: list, weak_topics: list) -> list:
    """
    Re-order topics so weak topics appear first.

    Uses conditional logic: a topic with a matching weak keyword
    is considered high priority (scored higher).

    Parameters:
        all_topics  : the full ordered list of Python topics
        weak_topics : topics the student finds difficult

    Returns:
        Reordered list (weak topics first, rest in original order)
    """
    high_priority = []   # topics matching a weak keyword
    low_priority  = []   # all other topics

    for topic in all_topics:
        topic_lower = topic.lower()

        # Check if any weak keyword appears in this topic name
        is_weak = False
        for weak_word in weak_topics:
            if weak_word.lower() in topic_lower:
                is_weak = True
                break

        if is_weak:
            high_priority.append(topic)
        else:
            low_priority.append(topic)

    # Weak topics first, then the rest in original order
    return high_priority + low_priority


# ─────────────────────────────────────────────────────────────
#  LEARNING PATH GENERATOR
# ─────────────────────────────────────────────────────────────

def generate_learning_path(student, topic: str, all_resources: list) -> list:
    """
    Build a personalised, time-fitted learning path for ONE topic.

    Steps:
      1. Get the student's level for this topic (core/advanced)
      2. Filter out already-completed resources
      3. Score each remaining resource
      4. Sort by score (highest first)
      5. Select resources until daily time budget is used up
      6. If student is on core and budget remains → add 1 advanced teaser
      7. Return the final ordered path

    Parameters:
        student       : Student object (from student.py)
        topic         : topic name string
        all_resources : list of resource dicts for this topic + level

    Returns:
        Ordered list of resource dicts to study today
    """

    # ── Step 1: Determine level ────────────────────────────────────
    level = student.get_level(topic)   # "core" or "advanced"

    # ── Step 2: Filter completed resources ────────────────────────
    # Only keep resources the student hasn't finished yet
    # List comprehension: concise filtering
    pending = [r for r in all_resources if not student.is_done(r["id"])]

    if not pending:
        return []    # all resources at this level are done

    # ── Step 3: Score each resource ───────────────────────────────
    # Use sorted() with a lambda key to rank by score (highest first)
    scored_resources = sorted(
        pending,
        key=lambda r: score_resource(r, student.learning_style,
                                     student.weak_topics, student.strong_topics),
        reverse=True    # highest score first
    )

    # ── Step 4: Fit resources into the daily time budget ──────────
    path = []
    time_remaining = student.daily_budget   # minutes left for today

    for resource in scored_resources:
        duration = resource.get("duration", 30)

        # Conditional: only add resource if it fits in remaining time
        if duration <= time_remaining:
            path.append(resource)
            time_remaining -= duration

        # Stop if no meaningful time remains (less than 10 min)
        if time_remaining < 10:
            break

    return path


def generate_full_plan(student, all_topics: list, resources_by_level) -> dict:
    """
    Generate a complete daily study plan across multiple topics.

    Strategy:
      1. Prioritise weak topics
      2. Split budget equally across topics that have pending resources
      3. Generate a path for each topic within its time slice
      4. Skip topics with no pending content

    Parameters:
        student          : Student object
        all_topics       : list of all topic names
        resources_by_level : function(topic, level) → list of resources

    Returns:
        dict: { topic_name: [list of resources] }
    """
    # ── Step 1: Prioritise topics by weakness ─────────────────────
    ordered_topics = prioritise_topics(all_topics, student.weak_topics)

    # ── Step 2: Find topics that actually have pending resources ──
    topics_with_content = []

    for topic in ordered_topics:
        level     = student.get_level(topic)
        resources = resources_by_level(topic, level)
        pending   = [r for r in resources if not student.is_done(r["id"])]

        if pending:
            topics_with_content.append(topic)

    if not topics_with_content:
        return {}   # nothing left to study

    # ── Step 3: Split budget across topics ────────────────────────
    # Each topic gets an equal share of today's budget
    # Conditional: if more than 5 topics, cap per-topic time at 30 min
    topic_count = len(topics_with_content)
    per_topic   = student.daily_budget // topic_count

    if per_topic < 15:
        per_topic = 15    # ensure at least 15 minutes per topic

    # ── Step 4: Build paths ────────────────────────────────────────
    full_plan = {}
    original_budget = student.daily_budget

    for topic in topics_with_content:
        # Temporarily set a per-topic budget for this topic
        student.daily_budget = per_topic

        level     = student.get_level(topic)
        resources = resources_by_level(topic, level)
        path      = generate_learning_path(student, topic, resources)

        if path:    # only include topics that have something to study
            full_plan[topic] = path

    # Restore original budget
    student.daily_budget = original_budget

    return full_plan


# ─────────────────────────────────────────────────────────────
#  DISPLAY FUNCTION
# ─────────────────────────────────────────────────────────────

def display_path(path: list, topic: str, level: str, student_name: str):
    """
    Print a nicely formatted learning path for one topic.

    Parameters:
        path         : list of resource dicts
        topic        : topic name
        level        : "core" or "advanced"
        student_name : for personalised header
    """
    total_mins = sum(r.get("duration", 0) for r in path)

    print("\n" + "=" * 62)
    print(f"  LEARNING PATH:  {topic}")
    print("=" * 62)
    print(f"  Student : {student_name}")
    print(f"  Level   : {level.upper()}")
    print(f"  Items   : {len(path)}  |  Est. time: {total_mins} min")
    print("─" * 62)

    if not path:
        print("  All resources at this level are complete!")
        print("  Move to the next level or pick another topic.")
    else:
        for i, resource in enumerate(path, start=1):
            icon     = TYPE_ICON.get(resource.get("type", "reading"), "[----] ")
            title    = resource.get("title", "Untitled")
            duration = resource.get("duration", 0)
            desc     = resource.get("description", "")
            url      = resource.get("url", "")

            print(f"\n  {i}. {icon} {title}  ({duration} min)")
            print(f"       {desc}")
            print(f"       {url}")

    print("\n" + "=" * 62 + "\n")
