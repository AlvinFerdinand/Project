# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df_days = pd.read_csv('Bike-sharing-dataset/day.csv')
df_hours = pd.read_csv('Bike-sharing-dataset/hour.csv')

# Clean the data (if necessary)
df_days_cleaned = df_days.dropna()
df_hours_cleaned = df_hours.dropna()

# Set the title of the app
st.title("Bike Sharing Data Analysis Dashboard")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a page:", ("Overview", "Weather Impact", "Weekday vs Weekend"))

if options == "Overview":
    st.header("Overview")
    st.write("This dashboard presents an analysis of bike sharing data.")
    
    st.subheader("Bike Sharing Data Summary")
    st.write(df_days_cleaned.describe())

elif options == "Weather Impact":
    st.header("Weather Impact on Bike Usage")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df_days_cleaned)
    plt.title('Impact of Weather on Bike Usage')
    plt.xlabel('Weather Condition')
    plt.ylabel('Number of Bike Rentals')
    st.pyplot()

elif options == "Weekday vs Weekend":
    st.header("Usage Patterns: Weekdays vs Weekends")
    df_days_cleaned['is_weekend'] = df_days_cleaned['weekday'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='is_weekend', y='cnt', data=df_days_cleaned, estimator=sum)
    plt.title('Bike Usage on Weekdays vs Weekends')
    plt.xlabel('Day Type')
    plt.ylabel('Total Bike Rentals')
    st.pyplot()
