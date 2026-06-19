"""
dashboard.py

Executive Dashboard Builder

This module acts as the main controller (or orchestrator) of the
Amazon Retail Intelligence System.

Responsibilities:
1. Load data
2. Perform feature engineering
3. Calculate business KPIs
4. Generate visualizations
5. Generate business insights
6. Present the complete executive dashboard

Author : Sandhya J
Project: Amazon Retail Intelligence System
"""

# ==========================================================
# Import Data Loading Functions
# ==========================================================

# Loads CSV files and merges Orders, Customers and Products
from src.data_loader import load_data

# Creates derived columns such as Sales, Year, Month,
# Week, Quarter etc., which are required for analytics
from src.feature_engineering import create_features


# ==========================================================
# Import Business Metric Functions
# ==========================================================

# These functions calculate all business KPIs used
# throughout the dashboard.

from src.metrics import (

    # Executive KPIs
    total_revenue,
    total_orders,
    total_customers,
    average_order_value,

    # Revenue Trend Metrics
    weekly_revenue,
    monthly_revenue,
    wow_growth,
    mom_growth,

    # Product Metrics
    top_products,
    category_sales,

    # Customer Metrics
    customer_revenue,
    city_sales,
)


# ==========================================================
# Import Visualization Functions
# ==========================================================

# These functions generate charts using Matplotlib.

from src.visualization import (

    plot_monthly_revenue,
    plot_weekly_revenue,

    plot_mom_growth,
    plot_wow_growth,

    plot_top_products,
    plot_category_sales,

    plot_customer_revenue,
    plot_city_sales,
)


# ==========================================================
# Import Business Insight Functions
# ==========================================================

# These functions convert raw metrics into
# executive-level insights and recommendations.

from src.business_insights import (

    executive_summary,

    revenue_growth_insights,

    top_product_insights,

    city_insights,

    recommendations,
)


# ==========================================================
# Dashboard Builder
# ==========================================================

def build_dashboard():
    """
    Build the complete Executive Dashboard.

    Workflow:

    Load Data
        ↓
    Feature Engineering
        ↓
    Calculate KPIs
        ↓
    Create Visualizations
        ↓
    Generate Business Insights
    """

    # ======================================================
    # STEP 1 : Load Data
    # ======================================================

    # Read CSV files and merge them into a single dataframe.
    df = load_data()

    # Create calculated columns that are required
    # for reporting and analytics.
    df = create_features(df)


    # ======================================================
    # STEP 2 : Calculate Executive KPIs
    # ======================================================

    # Calculate total sales generated.
    revenue = total_revenue(df)

    # Count total unique orders.
    orders = total_orders(df)

    # Count unique customers.
    customers = total_customers(df)

    # Calculate Average Order Value.
    aov = average_order_value(df)


    # ======================================================
    # Display Executive KPIs
    # ======================================================

    print("=" * 60)
    print(" AMAZON RETAIL INTELLIGENCE DASHBOARD ")
    print("=" * 60)

    # Display revenue with currency formatting.
    print(f"Total Revenue       : ₹{revenue:,.2f}")

    # Display total number of orders.
    print(f"Total Orders        : {orders:,}")

    # Display customer count.
    print(f"Total Customers     : {customers:,}")

    # Display Average Order Value.
    print(f"Average Order Value : ₹{aov:,.2f}")


    # ======================================================
    # STEP 3 : Calculate Revenue Metrics
    # ======================================================

    # Weekly revenue trend.
    weekly_df = weekly_revenue(df)

    # Monthly revenue trend.
    monthly_df = monthly_revenue(df)

    # Week-over-Week growth.
    wow_df = wow_growth(df)

    # Month-over-Month growth.
    mom_df = mom_growth(df)


    # ======================================================
    # STEP 4 : Calculate Product Metrics
    # ======================================================

    # Top revenue generating products.
    product_df = top_products(df)

    # Revenue by product category.
    category_df = category_sales(df)


    # ======================================================
    # STEP 5 : Calculate Customer Metrics
    # ======================================================

    # Revenue by customer.
    customer_df = customer_revenue(df)

    # Revenue by city.
    city_df = city_sales(df)


    # ======================================================
    # STEP 6 : Create Dashboard Visualizations
    # ======================================================

    # Revenue Trend Charts
    plot_monthly_revenue(monthly_df)

    plot_weekly_revenue(weekly_df)

    plot_mom_growth(mom_df)

    plot_wow_growth(wow_df)


    # Product Charts
    plot_top_products(product_df)

    plot_category_sales(category_df)


    # Customer Charts
    plot_customer_revenue(customer_df)

    plot_city_sales(city_df)


    # ======================================================
    # STEP 7 : Generate Executive Insights
    # ======================================================

    print("\n")
    print("=" * 60)
    print("EXECUTIVE BUSINESS INSIGHTS")
    print("=" * 60)

    # Create an empty list to store all insights.
    insights = []


    # ------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------

    # Add KPI summary insights.
    insights.extend(
        executive_summary(
            revenue,
            orders,
            customers,
            aov,
        )
    )


    # ------------------------------------------------------
    # Revenue Insights
    # ------------------------------------------------------

    insights.extend(
        revenue_growth_insights(mom_df)
    )


    # ------------------------------------------------------
    # Product Insights
    # ------------------------------------------------------

    insights.extend(
        top_product_insights(product_df)
    )


    # ------------------------------------------------------
    # Customer Insights
    # ------------------------------------------------------

    insights.extend(
        city_insights(city_df)
    )


    # ------------------------------------------------------
    # Business Recommendations
    # ------------------------------------------------------

    insights.extend(
        recommendations()
    )


    # ======================================================
    # Display Insights
    # ======================================================

    # Loop through every insight and print it
    # as a bullet point.
    for insight in insights:

        print(f"• {insight}")


# ==========================================================
# Program Entry Point
# ==========================================================

# This block executes only when this file is run directly.
#
# Example:
# python dashboard.py
#
# If dashboard.py is imported into another module,
# this block will NOT execute.

if __name__ == "__main__":

    build_dashboard()