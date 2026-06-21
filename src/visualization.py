"""
visualization.py

Reusable visualization library for the
Amazon Retail Intelligence System.

This module contains reusable charts for dashboards,
executive reporting, and business analysis.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pandas import DataFrame

from src.dashboard_utils import (
    apply_chart_style,
    add_bar_labels,
    highlight_max_bar,
)

from src.chart_theme import (
    BAR_COLOR,
    BAR_EDGE,
    BAR_ALPHA,
    LINE_COLOR,
    LINE_WIDTH,
    MARKER,
    FIG_HEIGHT,
    FIG_WIDTH,
    DPI,
    apply_amazon_theme,
)

# ==========================================================
# Revenue Trend Charts
# ==========================================================

def plot_monthly_revenue(monthly_df: DataFrame):
    """
    Plot Monthly Revenue Trend.
    """

    monthly_df = monthly_df.sort_values("Year_Month")

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.plot(
       monthly_df["Year_Month"],
       monthly_df["Monthly_Revenue"],
       color=LINE_COLOR,
       marker=MARKER,
       linewidth=LINE_WIDTH,
    )

    apply_chart_style(
        ax,
        title="Monthly Revenue Trend",
        xlabel="Month",
        ylabel="Revenue",
    )

    apply_amazon_theme(ax)

    plt.xticks(rotation=45)
    fig.tight_layout()

    return fig


def plot_weekly_revenue(weekly_df: DataFrame):
    """
    Plot Weekly Revenue Trend.
    """

    weekly_df = weekly_df.sort_values("Year_Week")

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.plot(
        weekly_df["Year_Week"],
        weekly_df["Weekly_Revenue"],
        color=LINE_COLOR,
        marker=MARKER,
        linewidth=LINE_WIDTH,
    )

    apply_chart_style(
        ax,
        title="Weekly Revenue Trend",
        xlabel="Week",
        ylabel="Revenue",
    )

    apply_amazon_theme(ax)
    
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=8))
    plt.xticks(rotation=45, ha='right')
    #plt.xticks(rotation=45)
    fig.tight_layout()

    return fig


def plot_mom_growth(monthly_df: DataFrame):
    """
    Plot Month-over-Month Revenue Growth.
    """

    monthly_df = monthly_df.sort_values("Year_Month")

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.plot(
        monthly_df["Year_Month"],
        monthly_df["MoM_Growth_%"],
        color=LINE_COLOR,
        marker=MARKER,
        linewidth=LINE_WIDTH,
    )

    apply_chart_style(
        ax,
        title="Month-over-Month Growth %",
        xlabel="Month",
        ylabel="Growth %",
    )

    apply_amazon_theme(ax)

    plt.xticks(rotation=45)
    fig.tight_layout()

    return fig


def plot_wow_growth(weekly_df: DataFrame):
    """
    Plot Week-over-Week Revenue Growth.
    """

    weekly_df = weekly_df.sort_values("Year_Week")

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.plot(
        weekly_df["Year_Week"],
        weekly_df["WoW_Growth_%"],
        color=LINE_COLOR,
        marker=MARKER,
        linewidth=LINE_WIDTH,
    )

    apply_chart_style(
        ax,
        title="Week-over-Week Growth %",
        xlabel="Week",
        ylabel="Growth %",
    )
    
    apply_amazon_theme(ax)
    
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=8))
    plt.xticks(rotation=45, ha='right')

    #plt.xticks(rotation=45)
    fig.tight_layout()

    return fig


# ==========================================================
# Product Analysis Charts
# ==========================================================

def plot_top_products(product_df: DataFrame):
    """
    Plot Top Products by Revenue.
    """

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.bar(
       product_df["product_name"],
       product_df["Sales"],
       color=BAR_COLOR,
       edgecolor=BAR_EDGE,
       alpha=BAR_ALPHA,
    )

    apply_chart_style(
        ax,
        title="Top Products by Revenue",
        xlabel="Product",
        ylabel="Revenue",
    )
    apply_amazon_theme(ax)
    add_bar_labels(ax)
    highlight_max_bar(ax)

    plt.xticks(rotation=60)
    fig.tight_layout()

    return fig


def plot_category_sales(category_df: DataFrame):
    """
    Plot Revenue by Product Category.
    """

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.bar(
        category_df["category"],
        category_df["Sales"],
        color=BAR_COLOR,
        edgecolor=BAR_EDGE,
        alpha=BAR_ALPHA,
    )

    apply_chart_style(
        ax,
        title="Revenue by Category",
        xlabel="Category",
        ylabel="Revenue",
    )
    apply_amazon_theme(ax)
    add_bar_labels(ax)
    highlight_max_bar(ax)

    fig.tight_layout()

    return fig


# ==========================================================
# Customer Analysis Charts
# ==========================================================

def plot_customer_revenue(customer_df: DataFrame):
    """
    Plot Revenue by Customer.
    """

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.bar(
        customer_df["customer_name"],
        customer_df["Sales"],
        color=BAR_COLOR,
        edgecolor=BAR_EDGE,
        alpha=BAR_ALPHA,
    )

    apply_chart_style(
        ax,
        title="Top Customers by Revenue",
        xlabel="Customer",
        ylabel="Revenue",
    )
    apply_amazon_theme(ax)
    add_bar_labels(ax)
    highlight_max_bar(ax)

    plt.xticks(rotation=90)
    fig.tight_layout()

    return fig


def plot_city_sales(city_df: DataFrame):
    """
    Plot Revenue by City.
    """

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT),dpi=DPI,)

    ax.bar(
        city_df["city"],
        city_df["Sales"],
        color=BAR_COLOR,
        edgecolor=BAR_EDGE,
        alpha=BAR_ALPHA,
    )

    apply_chart_style(
        ax,
        title="Revenue by City",
        xlabel="City",
        ylabel="Revenue",
    )
    apply_amazon_theme(ax)
    add_bar_labels(ax)
    highlight_max_bar(ax)

    fig.tight_layout()

    return fig