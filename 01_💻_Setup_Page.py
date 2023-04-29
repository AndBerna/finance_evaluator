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
