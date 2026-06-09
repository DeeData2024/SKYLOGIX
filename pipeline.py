import pandas as pd
import requests 
import os
import time
from dotenv import load_dotenv
import logging
from sqlalchemy import create_engine

# Setup logging
logging.basicConfig(level=logging.INFO)
load_dotenv()
#API_KEY and CONNECTION STRING
API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.weatherstack.com/current"
CITIES = ["Nairobi", "Johannesburg", "Lagos", "Accra"]
CONN_STRING = os.getenv("CONN_STRING")

#FUNCTION TO EXTRACT DATA FROM WEATHERSTACK API
def extract():
    responses = []
    with requests.Session() as session:
        session.params = {'access_key': API_KEY}
        for city in CITIES:
            try:
                resp = session.get(BASE_URL, params={'query': city})
                if resp.status_code == 429:
                    logging.warning(f"Rate limit hit. Skipping {city}.")
                    continue
                
                data = resp.json()
                if 'error' in data:
                    logging.error(f"API Error: {data['error'].get('info')}")
                    continue

                responses.append(data)
                logging.info(f"Fetched data for {city}")
                time.sleep(2) # Prevent 429 errors
            except Exception as e:
                logging.error(f"Request failed: {e}")
    return responses

# TRANSFORM THE RAW DATA INTO A STRUCTURED FORMAT

def transform(raw_data):
    data_records = []
    if not raw_data:
        return pd.DataFrame()

    for response in raw_data:
        # Weatherstack returns data in two main dictionaries: 'location' and 'current'
        location = response.get('location', {})
        current = response.get('current', {})

        record = {
            'city': location.get('name'),
            'country': location.get('country'),
            'latitude': location.get('lat'),
            'longitude': location.get('lon'),
            'observation_time': current.get('observation_time'),
            'temperature': current.get('temperature'),
            'humidity': current.get('humidity'),
            'wind_speed': current.get('wind_speed'),
            'pressure': current.get('pressure'),
            'cloudcover': current.get('cloudcover'),
            'Today_date': pd.to_datetime('today').date()
        }
        data_records.append(record)
    
    return pd.DataFrame(data_records)

# LOAD THE TRANSFORMED DATA INTO A DATABASE
def load(df, table_name: str):
    if not df.empty:
        engine = create_engine(CONN_STRING)
        # We use 'append' so the line chart in Streamlit can show history
        df.to_sql(table_name, engine, if_exists='append', index=False)
        logging.info("Data successfully sent to Database.")

if __name__ == "__main__":
    data = extract()
    df = transform(data)
    load(df)

