"""
dashboard_utils.py

Utility functions for formatting dashboard metrics and charts.

These helper functions ensure consistent formatting across
the Amazon Retail Intelligence Dashboard.
"""

from matplotlib.axes import Axes


# ==========================================================
# Dashboard Configuration
# ==========================================================


TITLE_SIZE = 16

LABEL_SIZE = 12

GRID_ALPHA = 0.3

LINE_WIDTH = 2

MARKER_SIZE = 8

BAR_ROTATION = 45

CURRENCY_SYMBOL = "₹"


# ==========================================================
# Number Formatting
# ==========================================================

def format_currency(value: float) -> str:
    """
    Format a number as currency.

    Example:
        1234567 -> ₹1,234,567.00
    """
    return f"{CURRENCY_SYMBOL}{value:,.2f}"


def format_number(value: int) -> str:
    """
    Format an integer with thousand separators.

    Example:
        1234567 -> 1,234,567
    """
    return f"{value:,}"


def format_percentage(value: float) -> str:
    """
    Format a percentage value.

    Example:
        15.4567 -> 15.46%
    """
    return f"{value:.2f}%"


# ==========================================================
# Chart Styling
# ==========================================================

def apply_chart_style(
    ax: Axes,
    title: str,
    xlabel: str,
    ylabel: str
) -> None:
    """
    Apply a consistent style to all charts.
    """

    ax.set_title(
        title,
        fontsize=TITLE_SIZE,
        fontweight="bold"
    )

    ax.set_xlabel(
        xlabel,
        fontsize=LABEL_SIZE
    )

    ax.set_ylabel(
        ylabel,
        fontsize=LABEL_SIZE
    )

    ax.grid(alpha=GRID_ALPHA)


# ==========================================================
# Value Labels
# ==========================================================

def add_bar_labels(ax: Axes) -> None:
    """
    Display values above each bar.
    """

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.0f",
            padding=3
        )


# ==========================================================
# Highlight Maximum Value
# ==========================================================

def highlight_max_bar(ax: Axes) -> None:
    """
    Highlight the highest bar in a bar chart.
    """

    heights = [bar.get_height() for bar in ax.patches]

    if not heights:
        return

    max_height = max(heights)

    for bar in ax.patches:
        if bar.get_height() == max_height:
            bar.set_edgecolor("black")
            bar.set_linewidth(2)