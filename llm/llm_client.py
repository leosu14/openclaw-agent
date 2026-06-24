import os

from dotenv import load_dotenv
from openai import OpenAI

from llm.providers import (
    PROVIDER,
    MODEL
)

load_dotenv()


def ask_llm(prompt):

    if PROVIDER == "deepseek":

        client = OpenAI(
            api_key=os.getenv(
                "DEEPSEEK_API_KEY"
            ),
            base_url="https://api.deepseek.com"
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response
            .choices[0]
            .message.content
        )

    elif PROVIDER == "openrouter":

        client = OpenAI(
            api_key=os.getenv(
                "OPENROUTER_API_KEY"
            ),
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response
            .choices[0]
            .message.content
        )

    elif PROVIDER == "ollama":

        client = OpenAI(
            api_key="ollama",
            base_url="http://localhost:11434/v1"
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response
            .choices[0]
            .message.content
        )

    else:

        raise Exception(
            f"Unknown provider: {PROVIDER}"
        )
