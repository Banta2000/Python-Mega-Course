import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Download the VADER lexicon if not already downloaded
nltk.download("vader_lexicon")

# Get the list of filenames in the data directory
filenames = os.listdir("data")
res = []
for filename in filenames:
    with open(f"data/{filename}") as file:
        day = filename.replace(".txt", "")
        data = file.read().strip()
        res.append((day, data))

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Lists to store the days and sentiment scores
days = []
pos = []
neg = []
for day, data in res:
    sentiment = analyzer.polarity_scores(data)
    days.append(day)
    pos.append(sentiment["pos"])
    neg.append(sentiment["neg"])

# Create a DataFrame with the sentiment data
df = pd.DataFrame({"Day": days, "Positive": pos, "Negative": neg})

# Set the title of the Streamlit app
st.title("Daily Mood")

# Plot the line chart
st.line_chart(df.set_index("Day"))
