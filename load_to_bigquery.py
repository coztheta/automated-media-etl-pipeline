
from google.cloud import bigquery
from pathlib import Path

PROJECT_ID = "sacred-garden-456904-t6"
DATASET_ID = "media_analytics"
TABLE_ID = "trending_media"

# Find the cleaned CSV file in this project folder
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "clean_media.csv"

def load_to_bigquery():
    if not CSV_FILE.exists():
        raise FileNotFoundError(
            f"Cannot find {CSV_FILE}. Run transform.py first."
        )

    client = bigquery.Client(project=PROJECT_ID)

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    with open(CSV_FILE, "rb") as file:
        job = client.load_table_from_file(
            file,
            table_ref,
            job_config=job_config,
        )

    job.result()

    table = client.get_table(table_ref)

    print("Data loaded successfully!")
    print(f"Table: {table.full_table_id}")
    print(f"Rows loaded: {table.num_rows}")
    print(f"Columns: {len(table.schema)}")


if __name__ == "__main__":
    load_to_bigquery()
