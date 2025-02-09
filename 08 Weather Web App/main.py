import streamlit as st

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
