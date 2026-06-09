import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Page Configuration
st.set_page_config(page_title="Weather Analytics", layout="wide")

# 2. Load Data from SQL
@st.cache_data(ttl=600) # Refresh data every 10 minutes
def load_data_from_db():
    engine = create_engine(os.getenv("CONN_STRING"))
    # Query the database
    query = "SELECT * FROM weather_readings"
    df = pd.read_sql(query, engine)
    # Ensure date format is correct for the chart
    df['Today_date'] = pd.to_datetime(df['Today_date']).dt.date
    return df

df = load_data_from_db()

# 3. Header
st.title("🌦️ Weather Intelligence & Trends")

# 4. City Selection Dropdown
cities = df['city'].unique()
selected_city = st.selectbox("Select a City", options=cities)

# 5. Filter Data
city_df = df[df['city'] == selected_city].sort_values('Today_date')

# Get the latest entry for the metrics
latest_data = city_df.iloc[-1] 

st.divider()

# Top Row: Metrics
st.subheader(f"Current Conditions: {selected_city}")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Temperature", f"{latest_data['temperature']}°C")
m2.metric("Humidity", f"{latest_data['humidity']}%")
m3.metric("Wind", f"{latest_data['wind_speed']} km/h")
m4.metric("Cloud Cover", f"{latest_data['cloudcover']}%")

# 6. Temperature Chart
st.subheader("📈 Temperature Trend")
st.line_chart(data=city_df, x='Today_date', y='temperature', color="#FF4B4B")

# 7. Download Section
csv_data = city_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download City Data", csv_data, f"{selected_city}_weather.csv")