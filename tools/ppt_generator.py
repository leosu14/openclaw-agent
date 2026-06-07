from pptx import Presentation
from pptx.util import Inches


def create_ppt(title, content, output_path, images=None):
    prs = Presentation()
    blocks = content.split("# ")
    image_index = 0
    for block in blocks:
        if not block.strip():
            continue
        lines = block.strip().split("\n")
        slide_title = lines[0]

        slide_body = "".join(lines[1:])
        layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(layout)
        slide.shapes.title.text = slide_title
        body = slide.placeholders[1]
        body.text = slide_body
        # ===== 自动插入图片 =====
        if images and image_index < len(images):
            try:
                slide.shapes.add_picture(
                    images[image_index],
                    Inches(5),
                    Inches(1.5),
                    width=Inches(3)
                )
                image_index += 1
            except:
                pass
    prs.save(output_path)
