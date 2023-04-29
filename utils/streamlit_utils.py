import json

import streamlit as st


def save_as_default_button(default, default_file_path):
    if st.button("Save as Default", key=default_file_path):
        with open(default_file_path, "w") as f:
            json.dump(default, f)


def create_multiselect_box(df, value_col, label_col, default_file_path):
    # Get the default value from session state or set an empty list as the default
    try:
        with open(default_file_path, "r") as f:
            default_value = json.load(f)
    except FileNotFoundError:
        default_value = []

    # Filter out the values with zero amount, so we only have the real expenses
    values = df.loc[df[value_col] != 0, label_col].unique()
    values = sorted(values)

    # Create a multiselect box with the filtered options and default value

    try:
        selected = st.multiselect(
            f"Select {value_col} to drop",
            values,
            default=st.session_state.get(f"{value_col}_to_drop", default_value),
        )

        save_as_default_button(selected, default_file_path)

        return selected

    except st.errors.StreamlitAPIException:
        st.error(
            f""" You can not use the defaults of another bank account. 
            Please delete the file  {default_file_path}"""
        )
        return []
