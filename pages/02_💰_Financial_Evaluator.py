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
