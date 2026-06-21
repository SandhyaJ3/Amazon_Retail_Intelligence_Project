"""
=============================================================
UI Components

Reusable UI widgets for the Retail Intelligence Platform.

Author : Sandhya J
=============================================================
"""

import streamlit as st

from src.config import (
    CURRENCY,
    DASHBOARD_TITLE
) 

def dashboard_summary(
    revenue,
    orders,
    customers,
    products,
    cities,
    start_date,
    end_date,
):
    """
    Displays an executive dashboard summary.
    """

    
    st.markdown(f"## {DASHBOARD_TITLE}")

    with st.container(border=True):

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"💰 Revenue : {CURRENCY}{revenue:,.0f}")
            st.write(f"🛒 Orders : {orders:,}")

        with col2:
            st.write(f"👥 Customers : {customers:,}")
            st.write(f"📦 Products : {products:,}")

        with col3:
            st.write(f"🏙 Cities : {cities:,}")
            st.write(
                f"📅 Period : {start_date.strftime('%d %b %Y')} "
                f"→ {end_date.strftime('%d %b %Y')}"
            )