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
from utils.streamlit_utils import colorize, create_multiselect_box, plot_bar

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

# drop the expenses and income selected by the user in the sidebar
index_to_drop = data[
    data["concept"].isin(expenses_to_drop) | data["concept"].isin(income_to_drop)
].index

data_custom = data.drop(index_to_drop)

# Monthly data : Raw data
# For the savings we need the raw data since it is the global balance of inoome - expenses
monthly_data = ft.calculate_monthly_data(data)
monthly_data = ft.add_savings(
    monthly_data,
)
monthly_data = ft.calculate_averages(monthly_data)

# Monthly data : Custom data
# For the income and expenses analysis we use the custom user data

monthly_data_custom = ft.calculate_monthly_data(data_custom)
monthly_data_custom = ft.add_savings(monthly_data_custom)
monthly_data_custom = ft.calculate_averages(monthly_data_custom)

# Monthly data : Savings account
# For the savings account we need to take the last value available for each month
account_balance = data.resample("M", on="date")["account"].last().reset_index()


# CURRENT STATUS ANALYSIS

status = f"""
Your average income right now is {colorize(monthly_data_custom["rolling_income"].iloc[-1])} {currency} per month

Your average expenses right now are {colorize(monthly_data_custom["rolling_positive_expenses"].iloc[-1], is_expenses=True)} {currency} per month

You are currently saving, on average, {colorize(monthly_data["rolling_savings"].iloc[-1])} {currency} per month

Your average saving rate (savings/income) is {colorize(monthly_data["rolling_saving_rate"].iloc[-1])}%
"""


st.write(text.current_status_title)
with st.expander("Expand for more info"):
    st.info(text.current_status_text)
st.write(status, unsafe_allow_html=True)


# Plot graph of the savings account

account_balance_graph = plot_bar(
    data=account_balance,
    xdata="date",
    ydata="account",
    title=f"Savings account evolution in {currency}",
    color=["green"],
    xaxis_title="Date",
    yaxis_title="Account Balance",
)

st.plotly_chart(account_balance_graph, use_container_width=True)


# Add graph with the savings each months

savings_graph = plot_bar(
    data=monthly_data,
    xdata="date",
    ydata="rolling_savings",
    title="Average Savings per month",
    color_setup=monthly_data["rolling_savings"] > 0,
    color=["green", "red"],
    xaxis_title="Date",
    yaxis_title="Amount",
)

st.plotly_chart(savings_graph, use_container_width=True)


# TRENDS

# Calculate the trends for the different variables

# For income and expenses we use the custom data
income_trend, monthly_data_custom = ft.get_trend(monthly_data_custom, "rolling_income")
expenses_trend, monthly_data_custom = ft.get_trend(
    monthly_data_custom, "rolling_positive_expenses"
)
# For savings we use the raw data
savings_trend, monthly_data = ft.get_trend(monthly_data, "savings")
saving_rate_trend, monthly_data = ft.get_trend(monthly_data, "rolling_saving_rate")

# For the account balance predictions we use the account balance data
acount_trend, account_balance, account_model = ft.get_trend(
    account_balance, "account", retun_model=True
)

# To estimate the account balance at the end of the year we need to add the months that are missing
months_to_end_of_year = 12 - account_balance.date.max().month
target = np.array(account_balance.index.max() + months_to_end_of_year).reshape(-1, 1)
predicted_account_balance = account_model.predict(target)[0, 0]

trends = """

Your income has been  increasing/decreasing in average by {colorize(income_trend)} {currency} each month  since {monthly_data_custom.date.min().strftime("%B %Y")}

Your expenses has been  increasing/decreasing in average by {colorize(expenses_trend, is_expenses=True)} {currency}  each month  since {monthly_data_custom.date.min().strftime("%B %Y")}

Your savings has been  increasing/decreasing in average by  {colorize(savings_trend)} {currency}  each month  since {monthly_data_custom.date.min().strftime("%B %Y")}

Your expected total savings in your account are  {colorize(predicted_account_balance)} {currency}  by the end of the year {account_balance.date.max().year}
"""


st.write(text.trends_title)
with st.expander("Expand for more info"):
    st.info(text.trends_extra)
st.write(trends, unsafe_allow_html=True)

# Add graph with the average income and their trends

income_expenses_graph = plot_bar(
    data=monthly_data_custom,
    xdata="date",
    ydata=["rolling_income", "rolling_positive_expenses"],
    title=" Average Income and Expenses per month",
    color=["green", "red"],
    xaxis_title="Date",
    yaxis_title="Amount",
    data_labels=["Average Income ", "Average Expenses"],
    # Optional parameters to add the trend lines
    add_trace=True,
    ytrend=[
        monthly_data_custom["rolling_income_trend"],
        monthly_data_custom["rolling_positive_expenses_trend"],
    ],
    trend_labels=["Income Trend", "Expenses Trend"],
    trendcolor=["lightgreen", "orange"],
    showlegend=True,
)

st.plotly_chart(income_expenses_graph, use_container_width=True)
