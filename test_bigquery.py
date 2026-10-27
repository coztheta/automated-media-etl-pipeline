
from google.cloud import bigquery

PROJECT_ID = "sacred-garden-456904-t6"
DATASET_ID = "media_analytics"

try:
    client = bigquery.Client(project=PROJECT_ID)

    dataset = client.get_dataset(
        f"{PROJECT_ID}.{DATASET_ID}"
    )

    print("BigQuery connection successful!")
    print(f"Project: {PROJECT_ID}")
    print(f"Dataset: {dataset.dataset_id}")
    print(f"Location: {dataset.location}")

except Exception as error:
    print("BigQuery connection failed.")
    print(f"Error: {error}")
