import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures


def add_income_and_expenses(data):
    data["income"] = data["amount"].apply(lambda x: x if x > 0 else 0)
    data["expenses"] = data["amount"].apply(lambda x: x if x < 0 else 0)
    data["positive_expenses"] = data["expenses"] * -1
    return data


def calculate_monthly_data(data=pd.DataFrame):
    return (
        data.resample("M", on="date")["income", "expenses", "positive_expenses"]
        .sum()
        .reset_index()
    )


def calculate_rolling_statistic(data, column, window=3, statistic="median"):
    rolling_func = getattr(
        data[column].rolling(window=window, min_periods=1), statistic
    )
    return rolling_func()


def add_savings(data):
    data["savings"] = data["income"] + data["expenses"]
    data["saving_rate"] = (data["savings"] / data["income"]) * 100

    return data


def calculate_averages(data):
    data["rolling_positive_expenses"] = calculate_rolling_statistic(
        data, "positive_expenses"
    )
    data["rolling_income"] = calculate_rolling_statistic(data, "income")
    data["rolling_savings"] = calculate_rolling_statistic(data, "savings")
    data["rolling_saving_rate"] = calculate_rolling_statistic(data, "saving_rate")
    return data
