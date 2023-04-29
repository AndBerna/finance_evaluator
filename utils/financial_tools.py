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


def get_trend(data, column, retun_model=False):
    X = data.index.values.reshape(-1, 1)
    y = data[column].values.reshape(-1, 1)
    regressor = LinearRegression()
    regressor.fit(X, y)

    coef = regressor.coef_[0][0]
    data[f"{column}_trend"] = regressor.predict(X)

    return (coef, data, regressor) if retun_model else (coef, data)


# def get_polynomial_trend(data, column):
#     X = data.index.values.reshape(-1, 1)
#     y = data[column].values.reshape(-1, 1)

#     best_score = -float("inf")
#     best_degree = 0

#     # Try polynomial degrees from 1 to 10
#     for degree in range(1, 11):
#         poly_features = PolynomialFeatures(degree=degree)
#         X_poly = poly_features.fit_transform(X)

#         regressor = LinearRegression()

#         # Use 5-fold cross-validation to evaluate the model
#         scores = cross_val_score(regressor, X_poly, y, cv=5, scoring="r2")
#         mean_score = scores.mean()

#         # If the current model is better than the previous best, save it
#         if mean_score > best_score:
#             best_score = mean_score
#             best_degree = degree

#     # Use the best degree to fit the final model
#     poly_features = PolynomialFeatures(degree=best_degree)
#     X_poly = poly_features.fit_transform(X)

#     regressor = LinearRegression()
#     regressor.fit(X_poly, y)

#     coef = regressor.coef_[0][1]
#     data[f"{column}_trend"] = regressor.predict(X_poly)

#     return coef, data, regressor


# def get_last_year_data(data):
#     return data[data["date"] > data["date"].max() - pd.DateOffset(months=12)]
