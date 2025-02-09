import streamlit as st
import numpy as np
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("City:", value="Zurich")

num_days = st.slider(
    "Number of days for forecast:",
    min_value=1,
    max_value=5,
    step=1,
    help="Select the number of days for which you want to see the forecast",
)

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {num_days} days in {place}")


def get_data(days):
    dates = [f"2021-09-{day}" for day in range(1, days + 1)]
    temperatures = [20 + np.random.randint(5, 10) for _ in range(days)]
    return dates, temperatures


# Generate random data for the plot
days = np.arange(1, num_days + 1)
if option == "Temperature":
    data = np.random.randint(low=-10, high=30, size=num_days)
    fig = px.line(x=days, y=data, labels={"x": "Day", "y": "Temperature (°C)"}, title="Temperature Forecast")
else:
    sky_conditions = ["Sunny", "Cloudy", "Rainy", "Snowy"]
    data = np.random.choice(sky_conditions, size=num_days)
    fig = px.bar(x=days, y=data, labels={"x": "Day", "y": "Sky Condition"}, title="Sky Condition Forecast")

dates, temperatures = get_data(num_days)
labels = {"x": "Date", "y": "Temperature (°C)"}
figure = px.line(x=dates, y=temperatures, labels=labels)

st.plotly_chart(figure)
