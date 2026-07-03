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

from google import genai

from src.config import GEMINI_API_KEY

# =========================================================
# Create Gemini Client
# =========================================================
print(GEMINI_API_KEY)
client = genai.Client(
    api_key=GEMINI_API_KEY
)


# =========================================================
# Ask Gemini
# =========================================================

def ask_llm(prompt: str) -> str:
    """
    Sends the prompt to Gemini and returns
    the generated business response.

    Parameters
    ----------
    prompt : str
        Complete prompt created in prompts.py

    Returns
    -------
    str
        AI generated response
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt,
        )

        return response.text

    except Exception as e:

        return (
            "❌ Unable to generate AI insights.\n\n"
            f"Reason: {e}"
        )