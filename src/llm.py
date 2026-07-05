"""
=========================================================
LLM Integration (Google Gemini)

This module communicates with Google's Gemini model.

The rest of the application only calls ask_llm(),
making it easy to replace Gemini with another LLM later.

Author : Sandhya J
=========================================================
"""

# =========================================================
# Imports
# =========================================================

#from google import genai

#from src.config import GEMINI_API_KEY
from openai import OpenAI
from src.config import OPENROUTER_API_KEY, OPENROUTER_MODEL

# =========================================================
# Create Open router  Client
# =========================================================




client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


# =========================================================
# Ask Gemini
# =========================================================

def ask_llm(prompt: str) -> str:
    """
    Sends the prompt to OpenRouter and returns
    the AI generated response.
    """

    try:

        response = client.chat.completions.create(

            # Model configured in config.py
            model=OPENROUTER_MODEL,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an Executive Business Analyst "
                        "specialized in retail analytics."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            # Lower temperature = more factual responses
            temperature=0.3,

            # Maximum response length
            max_tokens=700,
        )

        return response.choices[0].message.content

    except Exception as e:

        return (
            "❌ Unable to generate AI insights.\n\n"
            f"Reason: {e}"
        )