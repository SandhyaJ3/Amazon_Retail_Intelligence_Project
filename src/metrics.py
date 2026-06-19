"""
Business KPI calculations for the Amazon Retail Intelligence System.

This module contains reusable business metrics used by
dashboards, reporting, and machine learning workflows.
"""
from pathlib import Path
from pandas import DataFrame

# -------------------------------------------------------------------
# Project Paths (kept for future use if processed files are written)
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"



##Executive KPIs
##These are the metrics that would appear at the top of an executive dashboard."""

def total_revenue(df: DataFrame) -> float:
    """
    Calculate total revenue.
    """
    return df["Sales"].sum()


def total_orders(df: DataFrame) -> int:
    """
    Calculate total number of unique orders.
    """
    return df["Order_ID"].nunique()


def total_customers(df: DataFrame) -> int:
    """
    Calculate total number of unique customers.
    """
    return df["customer_id"].nunique()


def average_order_value(df: DataFrame) -> float:
    """
    Average Order Value (AOV).

    Formula:
        Revenue / Orders
    """

    revenue = total_revenue(df)
    orders = total_orders(df)

    return round(revenue / orders, 2)

def average_items_per_order(df: DataFrame) -> float:
    """
    Calculate the average number of items per order.

    Returns:
        float: Average quantity purchased per order.
    """

    if df.empty:
        return 0.0

    return round(df["Quantity"].sum() / total_orders(df), 2)

## *************** Revenue Trends ***************************"""

def weekly_revenue(df: DataFrame) -> DataFrame:
    """
    Weekly Revenue
    """

    return (
        df.groupby("Year_Week", as_index=False)["Sales"]
        .sum()
        .rename(columns={"Sales": "Weekly_Revenue"})
    )


def monthly_revenue(df: DataFrame) -> DataFrame:
    """
    Monthly Revenue
    """

    return (
        df.groupby("Year_Month", as_index=False)["Sales"]
        .sum()
        .rename(columns={"Sales": "Monthly_Revenue"})
    )


def wow_growth(df: DataFrame) -> DataFrame:
    """
    Week-over-Week Revenue Growth
    """

    weekly = (
    weekly_revenue(df)
    .sort_values("Year_Week")
    .reset_index(drop=True)
)


    weekly["WoW_Growth_%"] = (
        weekly["Weekly_Revenue"]
        .pct_change() * 100
    )

    return weekly


def mom_growth(df: DataFrame) -> DataFrame:
    """
    Month-over-Month Revenue Growth
    """

    monthly = (
        monthly_revenue(df).
        sort_values("Year_Month").
        reset_index(drop=True)
        )

    monthly["MoM_Growth_%"] = (
        monthly["Monthly_Revenue"]
        .pct_change() * 100
    )

    return monthly

## ************* Product Metrics **********************

def top_products(df: DataFrame, top_n: int = 10) -> DataFrame:
    """
    Top N Products by Revenue.
    """

    return (
        df.groupby("product_name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(top_n)
    )


def category_sales(df: DataFrame) -> DataFrame:
    """
    Revenue by Product Category.
    """

    return (
        df.groupby("category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

##******************* Customer Metrics ************************"""


def customer_revenue(df: DataFrame) -> DataFrame:
    """
    Revenue by Customer.
    """

    return (
        df.groupby("customer_name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )


def city_sales(df: DataFrame) -> DataFrame:
    """
    Revenue by City.
    """

    return (
        df.groupby("city", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )