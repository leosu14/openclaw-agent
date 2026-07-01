import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "OpenClaw"

VERSION = "2.0"

OUTPUT_DIR = "output"

IMAGE_DIR = "assets/images"

NEWS_NUMBER = 5

LEVELS = [

    "A1",

    "A2",

    "B1"

]

DEFAULT_THEME = "education"

DEFAULT_PERSONA = "default"

DEFAULT_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "deepseek"
)