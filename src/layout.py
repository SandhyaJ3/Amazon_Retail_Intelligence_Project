"""
Reusable UI components for the dashboard.
"""

import streamlit as st


def section_header(title, subtitle=""):
    """
    Displays a consistent section header.
    """
    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)

    st.divider()


def dashboard_header(last_updated=None):
    """
    Executive dashboard header.
    """

    left, right = st.columns([7,2])

    with left:

        st.title("🛒 Amazon Retail Intelligence Platform")

        st.caption(
            "Executive Sales Dashboard | Retail Analytics | Business Intelligence"
        )

    with right:

        if last_updated is not None:

            st.metric(
                "Last Updated",
                last_updated.strftime("%d %b %Y")
            )

    st.divider()