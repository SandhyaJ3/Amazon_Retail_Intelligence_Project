"""
=========================================================
Application Configuration

Central place for all dashboard constants.

Author : Sandhya J
=========================================================
"""

import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Application
# ==========================================================

APP_TITLE = "Amazon Retail Intelligence"

PAGE_ICON = "🛒"

CURRENCY = "₹"

DASHBOARD_TITLE = "📋 Executive Dashboard Summary"

# ==========================================================
# OpenAI Configuration
# ==========================================================
# ==========================================================
# Gemini Configuration
# ==========================================================
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENROUTER_MODEL = "openai/gpt-4o"

# ==========================================================
# Filter Keys
# ==========================================================

FILTER_KEYS = [
    "date_filter",
    "city_filter",
    "category_filter",
    "product_filter",
    "customer_filter",
]

# ==========================================================
# Filter Default State
# ==========================================================

FILTER_DEFAULTS = {}

print("=" * 50)
print("OPENROUTER_API_KEY =", OPENROUTER_API_KEY)
print("OPENROUTER_MODEL =", OPENROUTER_MODEL)
print("=" * 50)