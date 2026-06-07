from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

if not API_KEY:

    raise ValueError(
        "Missing OPENROUTER_API_KEY"
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

def ask_llm(prompt):

    response = client.chat.completions.create(

        model="openai/gpt-3.5-turbo",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content