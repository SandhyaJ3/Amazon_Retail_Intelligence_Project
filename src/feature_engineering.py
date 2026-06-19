"""
feature_engineering.py

Contains all feature engineering logic for the Retail Intelligence System.
"""

from pathlib import Path
import pandas as pd
from pandas import DataFrame

# -------------------------------------------------------------------
# Project Paths (kept for future use if processed files are written)
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


# -------------------------------------------------------------------
# Feature Engineering Functions
# -------------------------------------------------------------------

def create_sales(df: DataFrame) -> DataFrame:
    """
    Create Sales column.

    Formula:
        Sales = Quantity × Price
    """

    df = df.copy()

    df["Sales"] = df["Quantity"] * df["price"]

    return df


def create_date_features(df: DataFrame) -> DataFrame:
    """
    Create date-based features for analytics.
    """

    df = df.copy()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    df["Year"] = df["Order_Date"].dt.year

    df["Month"] = df["Order_Date"].dt.month_name()

    df["Month_Number"] = df["Order_Date"].dt.month

    df["Quarter"] = df["Order_Date"].dt.quarter

    df["Week"] = df["Order_Date"].dt.isocalendar().week.astype(int)

    df["Day"] = df["Order_Date"].dt.day

    df["Day_Name"] = df["Order_Date"].dt.day_name()

    df["Year_Month"] = df["Order_Date"].dt.to_period("M").astype(str)

    df["Year_Week"] = (
        df["Order_Date"].dt.isocalendar().year.astype(str)
        + "-W"
        + df["Order_Date"].dt.isocalendar().week.astype(str).str.zfill(2)
    )

    return df


def create_customer_features(df: DataFrame) -> DataFrame:
    """
    Create customer-related engineered features.
    """

    df = df.copy()

    df["signup_date"] = pd.to_datetime(df["signup_date"])

    df["Customer_Tenure_Days"] = (
        df["Order_Date"] - df["signup_date"]
    ).dt.days

    return df


def create_features(df: DataFrame) -> DataFrame:
    """
    Execute complete feature engineering pipeline.
    """

    df = create_sales(df)

    df = create_date_features(df)

    df = create_customer_features(df)

    return df