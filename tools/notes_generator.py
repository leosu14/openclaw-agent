import os


def save_notes(
    level,
    notes
):

    os.makedirs(
        "output/notes",
        exist_ok=True
    )

    path = (
        f"output/notes/"
        f"{level}_notes.md"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(notes)

    print(
        f"✅ Notes saved: {path}"
    )

    return path