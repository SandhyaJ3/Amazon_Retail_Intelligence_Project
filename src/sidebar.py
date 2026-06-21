"""
=========================================================
Sidebar Components

Reusable sidebar widgets.

Author : Sandhya J
=========================================================
"""

import streamlit as st

# ==========================================================
# Filter Keys
# ==========================================================

from src.config import FILTER_KEYS

def display_filter(icon, singular, plural, values):
    """
    Display active filters intelligently.
    """

    if not values:
        return

    if len(values) == 1:
        st.sidebar.write(
            f"{icon} {singular} : {values[0]}"
        )
    else:
        st.sidebar.write(
            f"{icon} {plural} : {len(values)} selected"
        )

def active_filters(
    dates,
    cities,
    categories,
    products,
    customers,
):
    """
    Displays the currently applied dashboard filters.
    """

    st.sidebar.markdown("---")
    st.sidebar.subheader("📌 Active Filters")

    # Date
    if len(dates) == 2:
        st.sidebar.write(f"📅 Date : {dates[0]} → {dates[1]}")

    display_filter(
    "🏙️",
    "City",
    "Cities",
    cities,
)

    # Category
    display_filter(
    "📦",
    "Category",
    "Categories",
    categories,
)

    # Product
    display_filter(
    "🛍️",
    "Product",
    "Products",
    products,
)

    # Customer
    display_filter(
    "👤",
    "Customer",
    "Customers",
    customers,
)

import streamlit as st
from src.config import CURRENCY

def dashboard_statistics(
    revenue,
    orders,
    customers,
    products,
    cities,
):
    """
    Compact dashboard statistics.
    """

    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Dashboard Statistics")

    st.sidebar.write(
        f"💰 **Revenue** &nbsp;&nbsp;&nbsp;&nbsp; {CURRENCY}{revenue:,.0f}"
    )

    st.sidebar.write(
        f"🛒 **Orders** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {orders:,}"
    )

    st.sidebar.write(
        f"👥 **Customers** &nbsp;&nbsp; {customers:,}"
    )

    st.sidebar.write(
        f"📦 **Products** &nbsp;&nbsp;&nbsp;&nbsp; {products:,}"
    )

    st.sidebar.write(
        f"🏙️ **Cities** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {cities:,}"
    )


def reset_filters():
    """
    Reset all dashboard filters.
    """

    st.sidebar.markdown("---")

    if st.sidebar.button(
        "🔄 Reset Filters",
        use_container_width=True,
    ):

        for key in FILTER_KEYS:
            st.session_state.pop(key, None)
        
        st.toast("Filters reset successfully.")
        st.rerun()