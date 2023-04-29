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

if "currency" not in st.session_state:
    st.session_state["currency"] = None


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

    # HEADERS

    st.write(text.headers_title)

    with st.expander("Expand for more info"):
        st.info(text.headers_extra_text)

    st.write(text.headers_text)

    # Ask the user if the file already has headers
    existing_headers = st.checkbox("Check the box if your file already has headers")

    # load the csv as a dataframe

    if st.session_state.df is None:
        df = load_csv(
            file=file,
            csv_separator=csv_separator,
            thousands_separator=thousands_separator,
            decimal_separator=decimal_separator,
            existing_headers=existing_headers,
        )

    else:
        # keep the dataframe if it is already laoded in the session state
        df = st.session_state.df

    with st.expander("Data preview"):
        st.write(df.head(5))

    # Set default values for selected columns
    default_selected_columns = default_values.get("selected_columns", {})
    selected_columns = {}

    #  Ask the user to map the columns to the right names
    # THis are the names that we want to map the columns to. We will use them in the rest of the app
    column_names = ["date", "concept", "amount", "account"]

    # Iterate over the column names and ask the user to select the corresponding column
    for name in column_names:
        # Check if the column is already mapped
        available_columns = [
            col for col in df.columns if col not in selected_columns.values()
        ]
        # load the default value if it exists
        default_col = default_selected_columns.get(name)

        # Add the default value to the list of available columns if it is not already there
        if default_col is not None and default_col not in available_columns:
            available_columns.append(default_col)

        # Ask the user to select the column
        selected_col = st.selectbox(
            f"Which column corresponds to {name}? ",
            available_columns,
        )

        # Save the selected column
        selected_columns[name] = selected_col

    # Assign column names to dataframe
    for name, col in selected_columns.items():
        df = df.rename(columns={col: name})

    # Label remaining columns as "other_X" where X is a number
    for i, col in enumerate(df.columns):
        if col not in column_names:
            df = df.rename(columns={col: f"other_{i}"})

    # Show the data to the user for validation
    st.write(text.headers_validation_text)

    with st.expander("Data preview"):
        st.write(df.head(5))

    #  DATE FORMAT
    st.write(text.date_title)
    st.write(text.date_text)

    with st.expander("Expand for more info"):
        st.info(text.date_text_extra)

    date_format = st.text_input("", value=default_values.get("date_format"))

    # Format the dataframe with the date format

    if date_format != "None":
        df = format_dataframe(df, date_format=date_format)

    else:
        st.error("Please input a date format")

    # CURRENCY

    st.write(text.currency_title)
    st.write(text.currency_text)

    currency = st.text_input("", value=default_values.get("currency"))

    # Default values for the next time the user loads the app
    default_values = {
        "csv_separator": csv_separator,
        "thousands_separator": thousands_separator,
        "decimal_separator": decimal_separator,
        "existing_headers": existing_headers,
        "selected_columns": selected_columns,
        "date_format": date_format,
        "currency": currency,
    }

    # Final instructions
    st.write(text.final_title)
    st.write(text.final_text)
