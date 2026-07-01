import os

PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "deepseek"
)

BASE_URLS = {

"deepseek":

"https://api.deepseek.com",

"openrouter":

"https://openrouter.ai/api/v1",

"ollama":

"http://localhost:11434/v1"

}