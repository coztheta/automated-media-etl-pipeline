import pendulum
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_DIR = "/opt/airflow/project"

with DAG(
    dag_id="media_etl_pipeline",
    description="Extract, transform, and load trending media into BigQuery",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Kolkata"),
    schedule="0 9 * * *",
    catchup=False,
    tags=["media", "etl", "bigquery"],
) as dag:

    extract = BashOperator(
        task_id="extract_media",
        bash_command=f"cd {PROJECT_DIR} && python extract.py",
    )

    transform = BashOperator(
        task_id="transform_media",
        bash_command=f"cd {PROJECT_DIR} && python transform.py",
    )

    load = BashOperator(
        task_id="load_to_bigquery",
        bash_command=f"cd {PROJECT_DIR} && python load_to_bigquery.py",
    )

    extract >> transform >> load
