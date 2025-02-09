import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Country Analysis App")
# Index(['country', 'happiness', 'gdp', 'social_support', 'life_expectancy', 'freedom_to_make_life_choices', 'generosity', 'corruption'],

df = pd.read_csv("data/happy.csv", index_col=0)

st.header("Country Analysis App")
x_axis = st.selectbox("X-Axis", options=df.columns)
y_axis = st.selectbox("y-Axis", options=df.columns)



x_data = df[x_axis]
y_data = df[y_axis]
title = f"{x_axis} vs {y_axis}"
labels={"x": x_axis, "y": y_axis}

figure = px.scatter(x=x_data, y=y_data, labels=labels, title=title, hover_name=df.index)
figure.update_traces(textposition='top center')
st.plotly_chart(figure)
    