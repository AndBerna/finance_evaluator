import json

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def save_as_default_button(default, default_file_path):
    if st.button("Save as Default", key=default_file_path):
        with open(default_file_path, "w") as f:
            json.dump(default, f)
