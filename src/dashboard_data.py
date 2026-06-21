import streamlit as st

from src.metrics import *

@st.cache_data(show_spinner=False)
def get_dashboard_data(df):

    return {
        "weekly": weekly_revenue(df),
        "monthly": monthly_revenue(df),
        "mom": mom_growth(df),
        "wow": wow_growth(df),
        "products": top_products(df),
        "categories": category_sales(df),
        "customers": customer_revenue(df),
        "cities": city_sales(df),
    }