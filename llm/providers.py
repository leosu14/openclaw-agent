import os

PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "deepseek"
)

MODEL = os.getenv(
    "LLM_MODEL",
    "deepseek-chat"
)
