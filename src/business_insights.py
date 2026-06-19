"""
business_insights.py

Generate executive business insights and recommendations
for the Amazon Retail Intelligence System.
"""

#============================
#Executive KPIs
#=============================

from pandas import DataFrame


def executive_summary(
    revenue: float,
    orders: int,
    customers: int,
    aov: float,
) -> list[str]:
    """
    Generate executive KPI summary.
    """

    insights = []

    insights.append(
        f"Total Revenue generated is ₹{revenue:,.2f}."
    )

    insights.append(
        f"{orders:,} orders were placed by {customers:,} unique customers."
    )

    insights.append(
        f"Average Order Value is ₹{aov:,.2f}."
    )

    return insights

#====================
#Revenue Insights
#====================

def revenue_growth_insights(monthly_df: DataFrame) -> list[str]:
    """
    Generate revenue growth insights.
    """

    insights = []

    latest = monthly_df.iloc[-1]

    growth = latest["MoM_Growth_%"]

    if growth > 0:
        insights.append(
            f"Revenue increased by {growth:.2f}% compared to the previous month."
        )
    elif growth < 0:
        insights.append(
            f"Revenue decreased by {abs(growth):.2f}% compared to the previous month."
        )
    else:
        insights.append(
            "Revenue remained stable compared to the previous month."
        )

    return insights


#====================
#Product Insights
#====================

def top_product_insights(product_df: DataFrame) -> list[str]:
    """
    Generate top product insights.
    """

    top = product_df.iloc[0]

    return [
        f"{top['product_name']} generated the highest revenue of ₹{top['Sales']:,.2f}."
    ]

#====================
#Customer Insights
#====================

def city_insights(city_df: DataFrame) -> list[str]:
    """
    Generate city performance insights.
    """

    top_city = city_df.iloc[0]

    return [
        f"{top_city['city']} is the highest revenue-generating city with ₹{top_city['Sales']:,.2f} in sales."
    ]

#====================
#Recommendations
#====================

def recommendations() -> list[str]:
    """
    Generate strategic recommendations.
    """

    return [

        "Increase inventory for top-selling products.",

        "Expand marketing campaigns in high-performing cities.",

        "Launch loyalty programs for repeat customers.",

        "Monitor low-performing categories for pricing or assortment improvements.",

        "Track monthly revenue trends to identify seasonality."
    ]