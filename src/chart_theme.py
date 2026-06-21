"""
=========================================================
Chart Theme

Centralized visualization theme for the
Amazon Retail Intelligence Platform.

Author : Sandhya J
=========================================================
"""
import matplotlib.pyplot as plt
# --------------------------------------------------------
# Brand Colors
# --------------------------------------------------------

AMAZON_ORANGE = "#FF9900"
AMAZON_BLUE = "#146EB4"
AMAZON_NAVY = "#232F3E"

BACKGROUND = "#FFFFFF"
GRID = "#E5E7EB"

TEXT = "#232F3E"
LABEL = "#5F6B7A"

SUCCESS = "#2E7D32"
WARNING = "#FFB300"

# --------------------------------------------------------
# Font Sizes
# --------------------------------------------------------

TITLE_SIZE = 15
LABEL_SIZE = 11
TICK_SIZE = 10
VALUE_SIZE = 9

# --------------------------------------------------------
# Figure Size
# --------------------------------------------------------

FIG_WIDTH = 8
FIG_HEIGHT = 4.5
DPI = 120

# --------------------------------------------------------
# Bar Settings
# --------------------------------------------------------

BAR_COLOR = AMAZON_ORANGE
BAR_ALPHA = 0.95
BAR_EDGE = AMAZON_NAVY

# --------------------------------------------------------
# Line Settings
# --------------------------------------------------------

LINE_COLOR = AMAZON_BLUE
LINE_WIDTH = 3
MARKER = "o"

# --------------------------------------------------------
# Grid
# --------------------------------------------------------

GRID_ALPHA = 0.30

# --------------------------------------------------------
# Apply Amazon theme
# --------------------------------------------------------

def apply_amazon_theme(ax):
    """
    Applies the Amazon executive dashboard theme
    to any matplotlib axis.
    """

    # Background
    ax.set_facecolor(BACKGROUND)

    # Grid
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.8,
        alpha=GRID_ALPHA,
        color=GRID,
    )

    # Remove unnecessary borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)

    # Tick styling
    ax.tick_params(
        axis="both",
        labelsize=TICK_SIZE,
        colors=LABEL,
    )

    # Axis Labels
    ax.xaxis.label.set_size(LABEL_SIZE)
    ax.yaxis.label.set_size(LABEL_SIZE)

    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)

    # Chart Title
    ax.title.set_size(TITLE_SIZE)
    ax.title.set_weight("bold")
    ax.title.set_color(AMAZON_NAVY)

# --------------------------------------------------------
# Export
# --------------------------------------------------------

__all__ = [
    "AMAZON_ORANGE",
    "AMAZON_BLUE",
    "AMAZON_NAVY",
    "BACKGROUND",
    "GRID",
    "TEXT",
    "LABEL",
    "TITLE_SIZE",
    "LABEL_SIZE",
    "TICK_SIZE",
    "VALUE_SIZE",
    "FIG_WIDTH",
    "FIG_HEIGHT",
    "DPI",
    "BAR_COLOR",
    "BAR_ALPHA",
    "BAR_EDGE",
    "LINE_COLOR",
    "LINE_WIDTH",
    "MARKER",
    "GRID_ALPHA",
]