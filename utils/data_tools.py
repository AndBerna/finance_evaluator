# Give me a function that loads the data in pandas from csv file in the data folder

import pandas as pd
import streamlit as st


def load_csv(
    file, existing_headers, csv_separator, thousands_separator, decimal_separator
):
    if existing_headers:
        df = pd.read_csv(
            file,
            sep=csv_separator,
            thousands=thousands_separator,
            decimal=decimal_separator,
        )
    else:
        df = pd.read_csv(
            file,
            sep=csv_separator,
            thousands=thousands_separator,
            decimal=decimal_separator,
            header=None,
        )

    return df


def format_dataframe(df, date_format):
    # Drop columns starting with "other_"
    cols_to_drop = [col for col in df.columns if col.startswith("other_")]
    df.drop(columns=cols_to_drop, inplace=True)
    # Convert the date column to datetime
    df["date"] = pd.to_datetime(df["date"], format=date_format)
    # sort values by date min to max
    df = df.sort_values(by="date", ascending=True).reset_index(drop=True)
    return df
