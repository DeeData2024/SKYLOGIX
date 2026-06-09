# SkyLogix Weather Data Warehouse & Analytics Dashboard
### 📊 Data Engineering Cohort Training Project | 10Alytics
A simplified implementation of an automated data engineering pipeline and analytics dashboard for SkyLogix Transportation, a logistics and delivery company headquartered in Nairobi, Kenya. With operations across Lagos, Accra, and Johannesburg. This project was built as part of a structured training cohort to showcase skills in automated API ingestion, programmatic data transformation, relational storage, and interactive business intelligence.
## Project Overview
This project is a modular data operations solution designed to address real-world logistical disruptions caused by unpredictable weather variations across major sub-Saharan shipping hubs, including Nairobi, Lagos, Accra, and Johannesburg.  The system ingests data from a live weather API, restructures and normalizes the raw payloads into an analytics-ready schema, archives entries in a centralized PostgreSQL warehouse layer, and presents actionable risk metrics to logistics dispatch teams via a live Streamlit interface.  
<img width="1380" height="469" alt="image" src="https://github.com/user-attachments/assets/12c8c3e4-057f-45dc-a0fd-aa4b5379f2e4" />
## Features
* Automated Ingestion
* Modular pipeline design
* Centralized Storage
* Interactive Business Intelligence
# Technologies Used
* Python: Scripting and Data Processing
* Pandas: Data manipulation and cleanup
* Requests: pulls real-time transaction data from live websites
* SQLAlchemy: Connects Python code to a PostgreSQL database
* PostgreSQL: open source object-relational database system
* Streamlit: client application framework delivering near real-time metrics dashboards.
* Python-Dotenv: maps local parameter keys safely away from code.
## Why These Technologies?
* Python & Pandas offer flexible data transformation capabilities, making them perfect for cleaning and nested API structures.
* PostgreSQL enables robust querying, analytical indexing, and a foundation for future historical forecasting dashboards.
* Streamlit simplifies the process of creating interactive dashboards, making it easy to visualize business metrics.
## Key Features
### Data Pipeline & ETL Process
* Extraction: Data is extracted from source systems(API)
* Transformation: The system flattens the dual-nested object sections (location and current)
* Loading: Data is loaded into a relational database
* Dashboard Exposure: Data is exposed through an interactive Streamlit dashboard to provide stakeholders with actionable insights.
## Data Quality
### This implementation includes several data quality checks:
* Null and Consistency Checks: Ensuring there are no missing or inconsistent values in the data.
* Temporal Auditing: Injects runtime time stamps (Today_date) generated at the moment of ingestion, ensuring flawless data audit trails.
* Rate-Limit Safeguards: Incorporates intentional 2-second cooldown intervals between city request loops to proactively avoid server-side rate-limiting (HTTP 429).
# Dashboard
<img width="968" height="896" alt="image" src="https://github.com/user-attachments/assets/41ccac11-42da-49b3-a5fd-48f56debdbe2" />

## Analytics Structure
* City Intelligence Selection: Filter operational data dynamically by selected supply chain nodes.
* KPI Metrics Layer: Temperature, Humidity, Wind Speed, and Cloud Cover.
* Time-Series Monitoring: Dynamic trend graphing to help supply chain managers analyze seasonal deviations and forecast route disruptions.
* Operational Data Hook: Direct CSV download integration to let dispatch teams export regional logs for offline manifest planning.

## Project Structure
```bash
├── app.py                  # Main Streamlit analytics dashboard web application
├── pipeline.py             # Core ETL module housing extract(), transform(), and load() functions
├── main.py                 # Pipeline orchestrator managing logging and end-to-end execution
├── .env                    # Secure local configuration file for API credentials and connection strings
├── Requirements.txt        # The project dependencies
```

## Getting Started
### Prerequisites
* Python 3.9 or higher installed locally.
* An active PostgreSQL database server instance.
* A valid API Access Key obtained from Weatherstack.
## 1. Installation
### Clone the project repository to your workstation environment and step into the base path:
```bash
git clone https://github.com/DeeData2024/SKYLOGIX.git
cd SKYLOGIX
```
## Install the project dependencies via pip:
```bash
pip install pandas requests python-dotenv sqlalchemy psycopg2-binary streamlit
```
## 2. Environment Configuration
Create a secure .env parameter file in the base path root:
```bash
API_KEY=your_weatherstack_secret_api_key
CONN_STRING=postgresql://your_user:your_password@localhost:5432/your_database
```
## 3. Pipeline Ingestion Execution
```bas
python main.py
```
## 4. Running the Dashboard Application
```bash
streamlit run app.py
```
## Acknowledgments
This project  was developed as a programmatic cohort project during the 10Alytics Data Engineering  Training. Extended appreciation goes out to program mentors for providing the technical frameworks, case constraints, and delivery guidance throughout the training path.







