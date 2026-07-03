"""
=========================================================
AI Executive Assistant

Reusable AI Assistant component for the
Amazon Retail Intelligence Platform.

Author : Sandhya J
=========================================================
"""

import streamlit as st

# Prompt Builder
from src.prompts import build_prompt

# LLM Call
from src.llm import ask_llm


def executive_ai_assistant(
    revenue,
    orders,
    customers,
    products,
    cities,
):
    """
    Displays the Executive AI Assistant.

    Parameters
    ----------
    revenue
    orders
    customers
    products
    cities

    These KPI values are passed into the prompt
    so the AI can answer using current dashboard
    metrics.
    """

    # ---------------------------------------------------
    # Section Heading
    # ---------------------------------------------------

    st.markdown("## 🤖 Executive AI Copilot")

    st.caption(
        "Ask business questions and receive AI-powered executive insights."
    )

    st.divider()

    # ---------------------------------------------------
    # User Question Input
    # ---------------------------------------------------

    question = st.text_area(
        "Business Question",
        height=100,
        placeholder=(
            "Example:\n"
            "Why is revenue growing?\n"
            "What should leadership focus on?\n"
            "What risks do you see?"
        ),
    )

    # ---------------------------------------------------
    # Ask AI Button
    # ---------------------------------------------------

    ask = st.button(
        "🚀 Ask AI",
        use_container_width=True,
    )

    # ---------------------------------------------------
    # Response Section
    # ---------------------------------------------------

    st.markdown("### AI Executive Response")

    response_container = st.container(border=True)

    with response_container:

        if ask:

            # Prevent empty questions
            if question.strip() == "":

                st.warning(
                    "Please enter a business question."
                )

            else:

                # Show loading spinner
                with st.spinner("Analyzing business data..."):

                    # -----------------------------------------
                    # Build prompt for the LLM
                    # -----------------------------------------

                    prompt = build_prompt(
                        question=question,
                        revenue=revenue,
                        orders=orders,
                        customers=customers,
                        products=products,
                        cities=cities,
                    )

                    # -----------------------------------------
                    # Call GPT
                    # -----------------------------------------

                    response = ask_llm(prompt)

                # -----------------------------------------
                # Display AI Response
                # -----------------------------------------

                st.markdown(response)

        else:

            st.info(
                "Ask a business question to receive executive insights."
            )