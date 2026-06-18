from ddgs import DDGS
import requests
import os

IMAGE_DIR = "assets/images"

os.makedirs(
    IMAGE_DIR,
    exist_ok=True
)

def download_image(keyword):

    try:

        results = DDGS().images(
            keyword,
            max_results=1
        )

        results = list(results)

        if not results:
            return None

        image_url = results[0]["image"]

        filename = (
            keyword.replace(" ", "_")
            + ".jpg"
        )

        path = os.path.join(
            IMAGE_DIR,
            filename
        )

        img = requests.get(
            image_url,
            timeout=15
        ).content

        with open(path, "wb") as f:
            f.write(img)

        return path

    except Exception as e:

        print(e)

        return None