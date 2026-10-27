# Automated Media ETL Pipeline

## Overview
An end-to-end data engineering project that extracts trending movie and TV data from the TMDB API, transforms it using Python and Pandas, and loads it into Google BigQuery for analytics.

## Architecture

TMDB API → Python Extraction → Pandas Transformation → CSV → Google BigQuery → Power BI

## Technologies Used
- **Python** — data extraction and processing
- **Pandas** — data cleaning and transformation
- **TMDB API** — media data source
- **Google BigQuery** — cloud data warehouse
- **Git and GitHub** — version control

## Pipeline Workflow
1. Extract trending media data from TMDB.
2. Clean and normalize the data using Pandas.
3. Save the transformed data as `clean_media.csv`.
4. Load the cleaned data into BigQuery.
5. Query the data for reporting and analysis.

## Current Results
- Successfully loaded 20 records into BigQuery.
- Created a table named `trending_media`.
- Verified that the data can be queried in BigQuery.

## BigQuery Destination
- **Dataset:** `media_analytics`
- **Table:** `trending_media`

## How to Run Locally

1. Clone this repository.
2. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Configure your TMDB API credentials locally. Never commit API keys or credential files.
4. Run extraction:

   ```bash
   python extract.py
   ```

5. Run transformation:

   ```bash
   python transform.py
   ```

6. Authenticate with Google Cloud Application Default Credentials and run:

   ```bash
   python load_to_bigquery.py
   ```

## Planned Improvements
- Automate the workflow using Apache Airflow.
- Build a Power BI dashboard.
- Add data validation and logging.
- Schedule regular data refreshes.
