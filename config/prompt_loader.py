from pathlib import Path

PROMPT_DIR = Path("prompts")


def load_prompt(name):

    with open(

        PROMPT_DIR /

        f"{name}.md",

        encoding="utf-8"

    ) as f:

        return f.read()