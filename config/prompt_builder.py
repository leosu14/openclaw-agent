from pathlib import Path

from config.levels import LEVEL_RULES
from config.personas import PERSONAS

PROMPT_DIR = Path("prompts")


def load_prompt(name: str):

    path = PROMPT_DIR / f"{name}.md"

    with open(path, encoding="utf-8") as f:

        return f.read()


def build_prompt(
    prompt_name,
    level=None,
    student=None,
    memory=None,
    reflection=None,
    article=None,
    lesson=None,
    extra=""
):

    sections = []

    # ==========================
    # Base Prompt
    # ==========================

    sections.append(
        load_prompt(prompt_name)
    )

    # ==========================
    # Teacher Persona
    # ==========================

    sections.append(
        PERSONAS["default"]
    )

    # ==========================
    # Level Rules
    # ==========================

    if level:

        sections.append(
            LEVEL_RULES[level]
        )

    # ==========================
    # Student Profile
    # ==========================

    if student:

        sections.append(

            f"""
Student Profile

{student}
"""

        )

    # ==========================
    # Memory
    # ==========================

    if memory:

        sections.append(

            f"""
Previous Memory

{memory}
"""

        )

    # ==========================
    # Reflection
    # ==========================

    if reflection:

        sections.append(

            f"""
Previous Reflection

{reflection}
"""

        )

    # ==========================
    # Today's Article
    # ==========================

    if article:

        sections.append(

            f"""
Today's News

{article}
"""

        )

    # ==========================
    # Lesson
    # ==========================

    if lesson:

        sections.append(

            f"""
Lesson

{lesson}
"""

        )

    # ==========================
    # Extra
    # ==========================

    if extra:

        sections.append(extra)

    return "\n\n".join(sections)


def build_teacher_prompt(
    level,
    article,
    student=None,
    memory=None,
    reflection=None
):

    return build_prompt(
        "teacher",
        level=level,
        student=student,
        memory=memory,
        reflection=reflection,
        article=article
    )


def build_notes_prompt(
    level,
    lesson,
    student=None
):

    return build_prompt(
        "notes",
        level=level,
        lesson=lesson,
        student=student
    )


def build_homework_prompt(
    level,
    lesson
):

    return build_prompt(
        "homework",
        level=level,
        lesson=lesson
    )


def build_quiz_prompt(
    level,
    lesson
):

    return build_prompt(
        "quiz",
        level=level,
        lesson=lesson
    )


def build_planner_prompt(
    article,
    level
):

    return build_prompt(
        "planner",
        level=level,
        article=article
    )


def build_reflection_prompt(
    lesson,
    result
):

    return build_prompt(
        "reflection",
        lesson=lesson,
        extra=f"""
Execution Result

{result}
"""
    )


def build_reviewer_prompt(
    lesson
):

    return build_prompt(
        "reviewer",
        lesson=lesson
    )
