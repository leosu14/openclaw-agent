from pptx import Presentation
from pptx.util import Inches
import os
from tools.image_tools import (
    download_image
)

def create_ppt(title, content, output):

    prs = Presentation()

    slides = content.split("SLIDE:")

    for block in slides:

        if not block.strip():
            continue

        lines = block.strip().split("\n")

        slide_title = ""

        slide_content = []

        for line in lines:

            if line.startswith("TITLE:"):

                slide_title = (
                    line.replace("TITLE:", "")
                    .strip()
                )

            elif line.startswith("-"):

                slide_content.append(line)

        slide_layout = prs.slide_layouts[1]

        slide = prs.slides.add_slide(
            slide_layout
        )

        slide.shapes.title.text = slide_title

        body = slide.placeholders[1]

        body.text = "\n".join(slide_content)

    prs.save(output)

    print(f"✅ PPT saved: {output}")
