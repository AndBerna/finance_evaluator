"""
Streamlit App

This is a Streamlit app for evaluating your own finances

Usage:
    - Run the app: streamlit run app.py

Author: AndBerna
Date: 17/04/2023
"""


# Imports

import numpy as np
import streamlit as st

# for k, v in st.session_state.items():
#     st.session_state[k] = v
st.set_page_config(
    page_title="Financial Evaluator",
    page_icon=":moneybag:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Define the default file paths

expenses_to_drop_file_path = "data\default_expenses_to_drop.json"
income_to_drop_file_path = "data\default_income_to_drop.json"


# Load the data from the session state
try:
    df = st.session_state["df"]
    data = df.copy()
except (KeyError, AttributeError):
    st.error("Please load a file first")
    st.stop()

currency = st.session_state["currency"]
