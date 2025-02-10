import streamlit as st
import plotly.express as px
from backend import get_data

# Title
st.title("Weather Forecast for the Next Days")


# Get the city name, the amount of days and the data to display
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


try:
    # Plot the data
    dates, temperature, weather = get_data(num_days, place)

    # Temperature Plot
    if option == "Temperature":
        labels = {"x": "Date", "y": "Temperature (°C)"}
        figure = px.line(x=dates, y=temperature, labels=labels)
        st.plotly_chart(figure)

    # Sky Plot
    if option == "Sky":
        weather_images = {
            "Clear": "images/clear.png",
            "Clouds": "images/clouds.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png",
        }

        col = st.columns(len(dates))
        for i, (date, condition) in enumerate(zip(dates, weather)):
            with col[i]:
                st.image(weather_images[condition], caption=date, width=100)
except Exception as e:
    st.error(f"Location does not exist")
