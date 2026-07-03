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

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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