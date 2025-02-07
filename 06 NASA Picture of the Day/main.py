import requests
import streamlit as st


def get_nasa_information():
    url = "https://api.nasa.gov/planetary/apod?api_key=GoxBN9MRGlyiMfB7w8dzSfnEWkFAe36ChlKAGtod"

    response = requests.get(url, timeout=5)
    response = response.json()

    explanation = response["explanation"]
    pic_url = response["hdurl"]
    title = response["title"]
    return explanation, pic_url, title


# Get the data from NASA
explanation, pic_url, title = get_nasa_information()


# Build the Sreamlit Website
st.title(title)
st.image(pic_url)
st.write(explanation)
st.write("")
st.write(f"Source: {pic_url}")
