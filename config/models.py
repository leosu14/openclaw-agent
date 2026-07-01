import os

MODELS = {

    "planner":

        os.getenv(
            "PLANNER_MODEL",
            "deepseek-chat"
        ),

    "teacher":

        os.getenv(
            "TEACHER_MODEL",
            "deepseek-chat"
        ),

    "reviewer":

        os.getenv(
            "REVIEWER_MODEL",
            "deepseek-chat"
        ),

    "notes":

        os.getenv(
            "NOTES_MODEL",
            "deepseek-chat"
        ),

    "homework":

        os.getenv(
            "HOMEWORK_MODEL",
            "deepseek-chat"
        ),

    "quiz":

        os.getenv(
            "QUIZ_MODEL",
            "deepseek-chat"
        ),

    "reflection":

        os.getenv(
            "REFLECTION_MODEL",
            "deepseek-chat"
        )

}