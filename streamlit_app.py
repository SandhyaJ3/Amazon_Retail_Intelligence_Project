"""
===============================================================
Amazon Retail Intelligence Platform
Version : 2.0
Sprint 2 - Step 1

Objective:
- Professional UI
- Executive Header
- Better Layout
- Clean Code Structure

Author : Sandhya J
===============================================================
"""

# ===============================================================
# Imports
# ===============================================================

import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.feature_engineering import create_features
from src.filters import dashboard_filters
from src.ui import dashboard_summary


from src.layout import (
    dashboard_header,
    section_header
)

from src.metrics import (
    total_revenue,
    total_orders,
    total_customers,
    average_order_value,
    weekly_revenue,
    monthly_revenue,
    wow_growth,
    mom_growth,
    top_products,
    category_sales,
    customer_revenue,
    city_sales,
)

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

from src.business_insights import (
    executive_summary,
    revenue_growth_insights,
    top_product_insights,
    city_insights,
    recommendations,
)
from pathlib import Path

from src.sidebar import (
    active_filters,
    dashboard_statistics,
    reset_filters,
)

from src.config import (
    APP_TITLE,
    PAGE_ICON
)

# ===============================================================
# Page Configuration
# Must be the first Streamlit command
# ===============================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)


# ===============================================================
# Load Custom CSS
# ===============================================================

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"

    if css_path.exists():
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.error(f"CSS not found: {css_path}")

load_css()


# ===============================================================
# Load & Prepare Data
# ===============================================================
with st.spinner("Loading Retail Intelligence Dashboard..."):
    df = load_data()
    df = create_features(df)
    if "Order_Date" in df.columns:
      df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Apply filters after the data is ready
#df = dashboard_filters(df)
(
    df,
    selected_dates,
    selected_cities,
    selected_categories,
    selected_products,
    selected_customers,
) = dashboard_filters(df)


# ===============================================================
# Executive Header
# ===============================================================

last_updated = None

# Update this column name if your dataset uses a different name
if "Order_Date" in df.columns:
    last_updated = df["Order_Date"].max()

dashboard_header(last_updated)

# ===============================================================
# KPI Calculations
# ===============================================================

revenue = total_revenue(df)
orders = total_orders(df)
customers = total_customers(df)
aov = average_order_value(df)
products = df["product_name"].nunique()
cities = df["city"].nunique()

dashboard_summary(
    revenue=revenue,
    orders=orders,
    customers=customers,
    products=products,
    cities=cities,
    start_date=df["Order_Date"].min(),
    end_date=df["Order_Date"].max(),
)

# ===============================================================
# Sidebar
# Filters will be added in Sprint 2 - Step 2
# ===============================================================

reset_filters()

active_filters(
    dates=selected_dates,
    cities=selected_cities,
    categories=selected_categories,
    products=selected_products,
    customers=selected_customers,
)

dashboard_statistics(
    revenue=revenue,
    orders=orders,
    customers=customers,
    products=products,
    cities=cities,
)
#with st.sidebar:

#    st.title("🔍 Dashboard Filters")

#    st.markdown("---")

#    st.info("Interactive filters will be added in Sprint 2.")

#    st.markdown("---")

#    st.subheader("Dashboard Status")

#    st.success("Data Loaded Successfully")

#    st.write(f"📦 Orders : {orders:,}")
#    st.write(f"👥 Customers : {customers:,}")



# ===============================================================
# KPI Cards
# ===============================================================

#section_header(
#    "📊 Executive Summary",
#    "Key Business Performance Indicators"
#)

#kpi1, kpi2, kpi3, kpi4 = st.columns(4)

#kpi1.metric(
#    "💰 Total Revenue",
#    f"₹{revenue:,.0f}"
#)

#kpi2.metric(
#    "🛒 Total Orders",
#    f"{orders:,}"
#)

#kpi3.metric(
#    "👥 Customers",
#    f"{customers:,}"
#)

#kpi4.metric(
#    "💳 Avg Order Value",
#    f"₹{aov:,.2f}"
#)

#st.divider()

# ===============================================================
# Revenue Analytics
# ===============================================================

section_header(
    "📈 Revenue Analytics",
    "Revenue trends across weeks and months"
)

weekly_df = weekly_revenue(df)
monthly_df = monthly_revenue(df)
mom_df = mom_growth(df)
wow_df = wow_growth(df)

col1, col2 = st.columns(2)

with col1:
    st.pyplot(plot_monthly_revenue(monthly_df))

with col2:
    st.pyplot(plot_weekly_revenue(weekly_df))

col3, col4 = st.columns(2)

with col3:
    st.pyplot(plot_mom_growth(mom_df))

with col4:
    st.pyplot(plot_wow_growth(wow_df))

#st.divider()

# ===============================================================
# Product Analytics
# ===============================================================

section_header(
    "🛍 Product Analytics",
    "Product and category performance"
)

product_df = top_products(df)
category_df = category_sales(df)

col5, col6 = st.columns(2)

with col5:
    st.pyplot(plot_top_products(product_df))

with col6:
    st.pyplot(plot_category_sales(category_df))

#st.divider()

# ===============================================================
# Customer Analytics
# ===============================================================

section_header(
    "👥 Customer Analytics",
    "Customer and city-wise sales"
)

customer_df = customer_revenue(df)
city_df = city_sales(df)

col7, col8 = st.columns(2)

with col7:
    st.pyplot(plot_customer_revenue(customer_df))

with col8:
    st.pyplot(plot_city_sales(city_df))

#st.divider()

# ===============================================================
# Executive Insights
# ===============================================================

section_header(
    "🧠 Executive Insights",
    "Automatically generated business insights"
)

insights = []

insights.extend(
    executive_summary(
        revenue,
        orders,
        customers,
        aov
    )
)

insights.extend(
    revenue_growth_insights(mom_df)
)

insights.extend(
    top_product_insights(product_df)
)

insights.extend(
    city_insights(city_df)
)

insights.extend(
    recommendations()
)

with st.container(border=True):
    for insight in insights:
        st.markdown(f"✅ {insight}")