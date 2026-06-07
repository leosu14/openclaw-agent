import requests
import os
from duckduckgo_search import DDGS

IMAGE_DIR = "assets/images"

os.makedirs(
    IMAGE_DIR,
    exist_ok=True
)

def download_image(keyword):

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.images(
                    keywords=keyword,
                    max_results=1
                )
            )

        if not results:
            return None

        image_url = results[0]["image"]

        img = requests.get(
            image_url,
            timeout=10
        ).content

        filename = (
            keyword
            .replace(" ", "_")
            + ".jpg"
        )

        path = os.path.join(
            IMAGE_DIR,
            filename
        )

        with open(path, "wb") as f:

            f.write(img)

        return path

    except Exception as e:

        print(
            f"Image error: {e}"
        )

        return None