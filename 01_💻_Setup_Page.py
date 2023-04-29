import json
import os
import sys

import pandas as pd
import streamlit as st

# get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))
# add the parent directory of the current script to sys.path
sys.path.append(os.path.join(dir_path, ".."))

import text.setup_text as text
from utils.data_tools import format_dataframe, load_csv
from utils.streamlit_utils import save_as_default_button

default_file_path = "data\default_csv_format.json"

# Get the default value from session state or set an empty dict as the default
try:
    with open(default_file_path, "r") as f:
        default_values = json.load(f)
except FileNotFoundError:
    default_values = {}

# Setup the page
st.set_page_config(
    page_title="Financial Evaluator",
    page_icon=":moneybag:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Setup the sidebar
st.sidebar.title("")

# Load  intro text
st.title("Financial Evaluator")
st.write(text.intro_text)
st.write(text.load_file_title)

# Load the file
file = st.file_uploader("", type=["csv"], key="file_uploader")


# Initialize session state variables : This will allow sharing the data between pages

if "df" not in st.session_state:
    st.session_state["df"] = None


# Once the file is loaded, load the rest of the setup instructions

if file is not None or st.session_state.df is not None:
    # ASK THE USER FOR THE FORMAT OF THE FILE
    st.write(text.format_file_title)
    st.write(text.format_file_text)

    # CSV SEPARATOR
    st.write(text.csv_separator_text)

    with st.expander("Expand for more info"):
        st.info(text.csv_separator_extra_text)

    csv_separator = st.text_input(
        "CSV Separator", value=default_values.get("csv_separator")
    )

    # THOUSANDS AND DECIMAL SEPARATOR

    st.write(text.thousands_decimals_separator_title)

    with st.expander("Expand for more info"):
        st.info(text.thousands_decimals_separator_extra_text)

    thousands_separator = st.text_input(
        "Thousands separator", value=default_values.get("thousands_separator")
    )
    decimal_separator = st.text_input(
        "Decimal separator", value=default_values.get("decimal_separator")
    )
