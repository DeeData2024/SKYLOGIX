"""from pipeline import extract, transform, load

if __name__ == "__main__":
    #extract data
    raw_data = extract()
    if raw_data:
        transformed_data = transform(raw_data)
        load(transformed_data, table_name="weather_readings")"""

from pipeline import extract, transform, load
import logging

# Set up logging to see progress in your terminal
logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("Starting Weather ETL Pipeline...")

    # 1. EXTRACT: Fetch data from API
    raw_data = extract()
    
    if not raw_data:
        logging.error("No data extracted. Pipeline aborted.")
        return

    # 2. TRANSFORM: Process the raw JSON into a clean DataFrame
    transformed_data = transform(raw_data)
    
    if transformed_data is None or transformed_data.empty:
        logging.error("Transformation failed or returned empty data.")
        return

    # 3. LOAD: Save to SQL Database
    load(transformed_data, table_name="weather_readings")
    
    logging.info("Pipeline execution completed successfully!")

if __name__ == "__main__":
    run_pipeline()