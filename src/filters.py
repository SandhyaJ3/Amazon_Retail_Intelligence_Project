"""
===========================================================
Dashboard Filters

Contains reusable Streamlit sidebar filters.

Author : Sandhya J
===========================================================
"""

import streamlit as st


def dashboard_filters(df):
    """
    Creates dashboard sidebar filters and
    returns the filtered dataframe.
    """

    filtered_df = df.copy()

    st.sidebar.header("🔍 Dashboard Filters")

    # -------------------------------------------------------
    # Date Filter
    # -------------------------------------------------------
    if "Order_Date" in filtered_df.columns:

        min_date = filtered_df["Order_Date"].min().date()
        max_date = filtered_df["Order_Date"].max().date()

        selected_dates = st.sidebar.date_input(
            "📅 Select Order Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )

        if len(selected_dates) == 2:

            start_date, end_date = selected_dates

            filtered_df = filtered_df[
                (filtered_df["Order_Date"].dt.date >= start_date)
                & (filtered_df["Order_Date"].dt.date <= end_date)
            ]
    
    # -------------------------------------------------------
    # City Filter
    # -------------------------------------------------------
    if "city" in filtered_df.columns:

        cities = sorted(filtered_df["city"].dropna().unique())

        selected_cities = st.sidebar.multiselect(
            "🏙️ Select City",
            options=cities,
            default=cities
        )

        filtered_df = filtered_df[
            filtered_df["city"].isin(selected_cities)
        ]
    
    # -------------------------------------------------------
    # Category Filter
    # -------------------------------------------------------
    if "category" in filtered_df.columns:

        categories = sorted(filtered_df["category"].dropna().unique())

        selected_categories = st.sidebar.multiselect(
            "📦 Select Category",
            options=categories,
            default=categories
        )

        filtered_df = filtered_df[
            filtered_df["category"].isin(selected_categories)
        ]
    #st.sidebar.warning("Reached Product Filter Section")
   
    if "product_name" in filtered_df.columns:

        #st.sidebar.write(
        #    f"Rows before Product Filter: {len(filtered_df)}"
        #)

        products = sorted(
            filtered_df["product_name"].dropna().unique()
        )

        selected_products = st.sidebar.multiselect(
            "🛍️ Select Product",
            options=products,
            default=products,
            placeholder="Choose one or more products..."
        )

        filtered_df = filtered_df[
            filtered_df["product_name"].isin(selected_products)
        ]

    # Customer Filter

    if "customer_name" in filtered_df.columns:

        customers = sorted(filtered_df["customer_name"].dropna().unique())

        selected_customers = st.sidebar.multiselect(
           "👤 Select Customer",
           options=customers,
           default=customers,
           placeholder="Choose customer(s)..."
        )

        filtered_df = filtered_df[
           filtered_df["customer_name"].isin(selected_customers)
        ]

    return filtered_df
