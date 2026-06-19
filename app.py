import streamlit as st

from src.data_loader import load_data
from src.feature_engineering import create_features

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

# -------------------------------
# Page Config (Power BI feel)
# -------------------------------
st.set_page_config(page_title="Retail Intelligence Dashboard",
                   layout="wide")

st.title("📊 Amazon Retail Intelligence Dashboard")

# -------------------------------
# Load Data
# -------------------------------
df = load_data()
df = create_features(df)

# -------------------------------
# Sidebar Filters (Power BI slicers)
# -------------------------------
st.sidebar.header("Filters")

# If you have date/category columns you can extend here later
# Example placeholder:
# selected_year = st.sidebar.selectbox("Year", df["Year"].unique())

# -------------------------------
# KPIs
# -------------------------------
revenue = total_revenue(df)
orders = total_orders(df)
customers = total_customers(df)
aov = average_order_value(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{revenue:,.0f}")
col2.metric("Total Orders", f"{orders:,}")
col3.metric("Customers", f"{customers:,}")
col4.metric("Avg Order Value", f"₹{aov:,.2f}")

st.divider()

# -------------------------------
# Revenue Trends
# -------------------------------
st.subheader("📈 Revenue Trends")

weekly_df = weekly_revenue(df)
monthly_df = monthly_revenue(df)
mom_df = mom_growth(df)
wow_df = wow_growth(df)

st.pyplot(plot_monthly_revenue(monthly_df))
st.pyplot(plot_weekly_revenue(weekly_df))
st.pyplot(plot_mom_growth(mom_df))
st.pyplot(plot_wow_growth(wow_df))



st.divider()

# -------------------------------
# Product Analysis
# -------------------------------
st.subheader("🛍 Product Performance")

product_df = top_products(df)
category_df = category_sales(df)

st.pyplot(plot_top_products(product_df))
st.pyplot(plot_category_sales(category_df))

st.divider()

# -------------------------------
# Customer Analysis
# -------------------------------
st.subheader("👥 Customer & City Insights")

customer_df = customer_revenue(df)
city_df = city_sales(df)

st.pyplot(plot_customer_revenue(customer_df))
st.pyplot(plot_city_sales(city_df))

st.divider()

# -------------------------------
# Insights Section
# -------------------------------
st.subheader("🧠 Executive Insights")

insights = []
insights.extend(executive_summary(revenue, orders, customers, aov))
insights.extend(revenue_growth_insights(mom_df))
insights.extend(top_product_insights(product_df))
insights.extend(city_insights(city_df))
insights.extend(recommendations())

for i in insights:
    st.write("•", i)