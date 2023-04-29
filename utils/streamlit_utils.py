import json

import plotly.express as px
import plotly.graph_objects as go
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


def plot_bar(
    data, xdata, ydata, title, xaxis_title, yaxis_title, color="green", **kwargs
):
    dtick = data[ydata[0]].max() / 10 if type(ydata) == list else data[ydata].max() / 10
    axis_title_font_size = 18
    axis_tickfont_size = 15

    real_labels = kwargs.get("data_labels", None)

    fig = px.bar(
        data,
        x=xdata,
        y=ydata,
        title=title,
        height=500,
        color=kwargs.get("color_setup", None),
        color_discrete_sequence=color,
        barmode="overlay",
        opacity=0.9,
    )

    if real_labels:
        labels_dict = {k: v for k, v in zip(data[ydata], real_labels)}
        fig.for_each_trace(lambda t: t.update(name=labels_dict[t.name]))

    fig.update_layout(
        title_font_size=20,
        xaxis_title=xaxis_title,
        xaxis_title_font_size=axis_title_font_size,
        xaxis_tickfont_size=axis_tickfont_size,
        yaxis_title=yaxis_title,
        yaxis_tickfont_size=axis_tickfont_size,
        yaxis_title_font_size=axis_title_font_size,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True, dtick=dtick),
    )

    for i, ytrend in enumerate(kwargs.get("ytrend", [])):
        fig.add_trace(
            go.Scatter(
                x=data[xdata] if kwargs.get("add_trace", True) else None,
                y=ytrend,
                mode="lines",
                line=dict(color=kwargs.get("trendcolor", None)[i], width=3),
                name=kwargs.get("trend_labels", None)[i],
            )
        )

    currency = st.session_state["currency"]
    # Add hoover information to the plot
    fig.update_traces(
        # hovertemplate="<br> Date: %{x|%b %Y}<br> Amount: %{y:,.2f} {currency}<extra></extra>",
        hovertemplate=f"<br>Date: %{{x|%b %Y}}<br>Amount: %{{y:.2f}} {currency} <extra></extra>",
    )

    fig.update_layout(
        showlegend=kwargs.get("showlegend", False),
        legend=dict(
            x=0.01,
            y=1,
            font=dict(size=14),
            bgcolor="rgba(0,0,0,0)",
        ),
        # hovermode="x unified",
    )

    return fig
