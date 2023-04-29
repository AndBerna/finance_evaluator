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

import text.financial_evaluator_text as text
import utils.financial_tools as ft
from utils.streamlit_utils import create_multiselect_box

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

# Calculate income and expenses

data = ft.add_income_and_expenses(data)

# SETUP THE SIDEBAR

st.sidebar.title("Optional Settings")

with st.sidebar:
    # Create a user interface to drop expenses

    with st.sidebar.expander("Expenses to drop"):
        expenses_to_drop = create_multiselect_box(
            df=data,
            value_col="expenses",
            label_col="concept",
            default_file_path=expenses_to_drop_file_path,
        )

    # Create a user interface to drop incomes

    with st.sidebar.expander("Income to drop"):
        income_to_drop = create_multiselect_box(
            df=data,
            value_col="income",
            label_col="concept",
            default_file_path=income_to_drop_file_path,
        )


# MAIN PAGE

st.title("Financial Evaluator")

st.write(text.intro_text)
with st.expander("Important information"):
    st.info(text.to_drop_text)
