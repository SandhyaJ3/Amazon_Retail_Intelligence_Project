"""
visualization.py

Reusable visualization library for the
Amazon Retail Intelligence System.

This module contains reusable charts for dashboards,
executive reporting, and business analysis.
"""

import matplotlib.pyplot as plt
from pandas import DataFrame

from src.dashboard_utils import (
    FIG_SIZE,
    apply_chart_style,
    add_bar_labels,
    highlight_max_bar,
)

# ==========================================================
# Revenue Trend Charts
# ==========================================================

def plot_monthly_revenue(monthly_df: DataFrame):
    """
    Plot Monthly Revenue Trend.
    """

    monthly_df = monthly_df.sort_values("Year_Month")

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.plot(
        monthly_df["Year_Month"],
        monthly_df["Monthly_Revenue"],
        marker="o",
        linewidth=2,
    )

    apply_chart_style(
        ax,
        title="Monthly Revenue Trend",
        xlabel="Month",
        ylabel="Revenue",
    )

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def plot_weekly_revenue(weekly_df: DataFrame):
    """
    Plot Weekly Revenue Trend.
    """

    weekly_df = weekly_df.sort_values("Year_Week")

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.plot(
        weekly_df["Year_Week"],
        weekly_df["Weekly_Revenue"],
        marker="o",
        linewidth=2,
    )

    apply_chart_style(
        ax,
        title="Weekly Revenue Trend",
        xlabel="Week",
        ylabel="Revenue",
    )

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def plot_mom_growth(monthly_df: DataFrame):
    """
    Plot Month-over-Month Revenue Growth.
    """

    monthly_df = monthly_df.sort_values("Year_Month")

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.plot(
        monthly_df["Year_Month"],
        monthly_df["MoM_Growth_%"],
        marker="o",
        linewidth=2,
    )

    apply_chart_style(
        ax,
        title="Month-over-Month Growth %",
        xlabel="Month",
        ylabel="Growth %",
    )

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def plot_wow_growth(weekly_df: DataFrame):
    """
    Plot Week-over-Week Revenue Growth.
    """

    weekly_df = weekly_df.sort_values("Year_Week")

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.plot(
        weekly_df["Year_Week"],
        weekly_df["WoW_Growth_%"],
        marker="o",
        linewidth=2,
    )

    apply_chart_style(
        ax,
        title="Week-over-Week Growth %",
        xlabel="Week",
        ylabel="Growth %",
    )

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


# ==========================================================
# Product Analysis Charts
# ==========================================================

def plot_top_products(product_df: DataFrame):
    """
    Plot Top Products by Revenue.
    """

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.bar(
        product_df["product_name"],
        product_df["Sales"],
    )

    apply_chart_style(
        ax,
        title="Top Products by Revenue",
        xlabel="Product",
        ylabel="Revenue",
    )

    add_bar_labels(ax)
    highlight_max_bar(ax)

    plt.xticks(rotation=60)
    plt.tight_layout()

    return fig


def plot_category_sales(category_df: DataFrame):
    """
    Plot Revenue by Product Category.
    """

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.bar(
        category_df["category"],
        category_df["Sales"],
    )

    apply_chart_style(
        ax,
        title="Revenue by Category",
        xlabel="Category",
        ylabel="Revenue",
    )

    add_bar_labels(ax)
    highlight_max_bar(ax)

    plt.tight_layout()

    return fig


# ==========================================================
# Customer Analysis Charts
# ==========================================================

def plot_customer_revenue(customer_df: DataFrame):
    """
    Plot Revenue by Customer.
    """

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.bar(
        customer_df["customer_name"],
        customer_df["Sales"],
    )

    apply_chart_style(
        ax,
        title="Revenue by Customer",
        xlabel="Customer",
        ylabel="Revenue",
    )

    add_bar_labels(ax)
    highlight_max_bar(ax)

    plt.xticks(rotation=90)
    plt.tight_layout()

    return fig


def plot_city_sales(city_df: DataFrame):
    """
    Plot Revenue by City.
    """

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    ax.bar(
        city_df["city"],
        city_df["Sales"],
    )

    apply_chart_style(
        ax,
        title="Revenue by City",
        xlabel="City",
        ylabel="Revenue",
    )

    add_bar_labels(ax)
    highlight_max_bar(ax)

    plt.tight_layout()

    return fig