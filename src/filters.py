"""
===========================================================
Dashboard Filters

Contains reusable Streamlit sidebar filters.

Author : Sandhya J
===========================================================
"""

import streamlit as st

def get_filter_defaults(df):
    """
    Returns the default values for all dashboard filters.
    """

    return {

        "date_filter": (
            df["Order_Date"].min().date(),
            df["Order_Date"].max().date(),
        ),

        "city_filter":
            sorted(df["city"].dropna().unique()),

        "category_filter":
            sorted(df["category"].dropna().unique()),

        "product_filter":
            sorted(df["product_name"].dropna().unique()),

        "customer_filter":
            sorted(df["customer_name"].dropna().unique()),
    }

def dashboard_filters(df):
    """
    Creates dashboard sidebar filters and
    returns the filtered dataframe.
    """

    filtered_df = df.copy()

   # -------------------------------------------------------
# Initialize Session State (Run Only Once)
# Store original dashboard defaults
# -------------------------------------------------------

    defaults = get_filter_defaults(df)

    if "filter_defaults" not in st.session_state:
       st.session_state.filter_defaults = defaults

# Initialize widget state only once
    for key, value in defaults.items():
       st.session_state.setdefault(key, value)

    st.sidebar.header("🔍 Dashboard Filters")

    # -------------------------------------------------------
    # Date Filter
    # -------------------------------------------------------
    if "Order_Date" in df.columns:

        min_date, max_date = st.session_state.filter_defaults["date_filter"]

        selected_dates = st.sidebar.date_input(
            "📅 Select Order Date Range",
            value=st.session_state["date_filter"],
            min_value=min_date,
            max_value=max_date,
            key="date_filter"
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
    if "city" in df.columns:

        cities = sorted(df["city"].dropna().unique())

        selected_cities = st.sidebar.multiselect(
           "🏙️ Select City",
            options=cities,
            default=st.session_state["city_filter"],
            key="city_filter",
        )

        filtered_df = filtered_df[
            filtered_df["city"].isin(selected_cities)
        ]
    
    # -------------------------------------------------------
    # Category Filter
    # -------------------------------------------------------
    if "category" in df.columns:

        categories = sorted(df["category"].dropna().unique())

        selected_categories = st.sidebar.multiselect(
            "📦 Select Category",
            options=categories,
            default=st.session_state["category_filter"],
            key="category_filter",
        )
        

        filtered_df = filtered_df[
            filtered_df["category"].isin(selected_categories)
        ]
    #st.sidebar.warning("Reached Product Filter Section")
   
    if "product_name" in df.columns:

        #st.sidebar.write(
        #    f"Rows before Product Filter: {len(filtered_df)}"
        #)

        products = sorted(df["product_name"].dropna().unique())

        selected_products = st.sidebar.multiselect(
           "🛍️ Select Product",
           options=products,
           default=st.session_state["product_filter"],
           key="product_filter",
        )


        filtered_df = filtered_df[
            filtered_df["product_name"].isin(selected_products)
        ]

    # -------------------------------------------------------
    # Customer Filter
    # -------------------------------------------------------

    if "customer_name" in df.columns:

        customers = sorted(df["customer_name"].dropna().unique())

        selected_customers = st.sidebar.multiselect(
            "👤 Select Customer",
            options=customers,
            default=st.session_state["customer_filter"],
            key="customer_filter",
        )


        filtered_df = filtered_df[
           filtered_df["customer_name"].isin(selected_customers)
        ]

    return (
    filtered_df,
    selected_dates,
    selected_cities,
    selected_categories,
    selected_products,
    selected_customers,
)
