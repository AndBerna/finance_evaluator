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
